import os
import pandas as pd
from PIL import Image
from sklearn.preprocessing import LabelEncoder
import torch
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights
from sklearn.model_selection import train_test_split

# Assuming database access objects (DAOs) are correctly implemented
from dao.soyuanDao import soyuanDao

soyuandao = soyuanDao()
path = os.path.join(os.path.abspath('.'), 'static', 'upload')

datalist = soyuandao.db.query("SELECT id, img1, img2, img3 FROM soyuan ORDER BY id DESC")

# Convert data to DataFrame
df = pd.DataFrame(datalist, columns=['id', 'img1', 'img2', 'img3'])
df[['img1', 'img2', 'img3']] = df[['img1', 'img2', 'img3']].applymap(lambda x: os.path.join(path, x))

image_paths = pd.DataFrame({
    'image_path': df[['img1', 'img2', 'img3']].values.flatten(),
    'label': df['id'].repeat(3).values
})

# Encode the labels (IDs)
label_encoder = LabelEncoder()
image_paths['label'] = label_encoder.fit_transform(image_paths['label'])

# Split the dataset into training and validation sets
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


# Image transformations
transformations = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Dataset and DataLoader
train_dataset = ImageDataset(train_df, transform=transformations)
val_dataset = ImageDataset(val_df, transform=transformations)
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=16, shuffle=False)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = resnet18(weights=ResNet18_Weights.DEFAULT)
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, len(label_encoder.classes_))  # Adjust for the number of classes
model.to(device)

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


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
