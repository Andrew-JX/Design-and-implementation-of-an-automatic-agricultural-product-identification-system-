import os
import pandas as pd
from PIL import Image
from sklearn.preprocessing import LabelEncoder
import torch
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights
from sklearn.model_selection import train_test_split

# 假设数据库访问对象(DAOs)实现正确
from dao.soyuanDao import soyuanDao

soyuandao = soyuanDao()
path = os.path.join(os.path.abspath('.'), 'static', 'upload')

datalist = soyuandao.db.query("SELECT id, img1, img2, img3 FROM soyuan ORDER BY id DESC")

# 转换数据到DataFrame
df = pd.DataFrame(datalist, columns=['id', 'img1', 'img2', 'img3'])
df[['img1', 'img2', 'img3']] = df[['img1', 'img2', 'img3']].applymap(lambda x: os.path.join(path, x))

image_paths = pd.DataFrame({
    'image_path': df[['img1', 'img2', 'img3']].values.flatten(),
    'label': df['id'].repeat(3).values
})

# 编码标签 (IDs)
label_encoder = LabelEncoder()
image_paths['label'] = label_encoder.fit_transform(image_paths['label'])

# 分割数据集为训练集和验证集
train_df, val_df = train_test_split(image_paths, test_size=0.2, random_state=42)


class ImageDataset(Dataset):
    def __init__(self, dataframe, transform=None):
        self.dataframe = dataframe
        self.transform = transform

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, index):
        img_path = self.dataframe.iloc[index]['image_path']
        label = self.dataframe.iloc[index]['label']
        image = Image.open(img_path).convert('RGB')
        if self.transform:
            image = self.transform(image)
        label = torch.tensor(label, dtype=torch.long)
        return image, label


# 图片转换
transformations = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# 创建Dataset和DataLoader
train_dataset = ImageDataset(train_df, transform=transformations)
val_dataset = ImageDataset(val_df, transform=transformations)
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=16, shuffle=False)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = resnet18(weights=ResNet18_Weights.DEFAULT)
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, len(label_encoder.classes_))
model.to(device)

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


# 训练模型的函数
def train_model(model, epochs):
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for imgs, labels in train_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch + 1} completed, Avg Loss: {total_loss / len(train_loader)}")


train_model(model, 10)
torch.save(model.state_dict(), 'model_weights1.pth')


# 使用训练好的模型来预测指定图片的ID
def predict_image(image_path):
    model = resnet18(weights=None)
    num_ftrs = model.fc.in_features
    model.fc = torch.nn.Linear(num_ftrs, len(label_encoder.classes_))
    model.load_state_dict(torch.load('model_weights1.pth'))
    model.to(device)
    model.eval()

    transformations = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    image = Image.open(image_path).convert('RGB')
    image = transformations(image)
    image = image.unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
        predicted_id = label_encoder.inverse_transform([predicted.item()])[0]

    return predicted_id


image_path = os.path.join(path, '202404260110488535288.jpg')
predicted_id = predict_image(image_path)
print(f"The predicted ID for the image '1.jpg' is: {predicted_id}")
