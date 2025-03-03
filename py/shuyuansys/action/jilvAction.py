from dao.jilvDao import jilvDao
from flask import Blueprint, request, session

jilv = Blueprint('jilv', __name__)
dao = jilvDao()


@jilv.route("/jilv/queryJilvAll", methods=['GET', 'POST'])
def queryJilvAll():
    pageSize = int(20)  # 每页显示的条数
    if request.method == 'POST':
        pageIndex = request.form.get('page')
        filedarr = request.form.getlist('filedarr[]')
        keyarr = request.form.getlist('keyarr[]')
        hstrarr = request.form.getlist('hstrarr[]')
        ifso = request.form.get('ifso')
    elif request.method == 'GET':
        print("get")
        pageIndex = request.args.get('page', type=str)
        filedarr = request.args.getlist('filedarr[]', type=str)
        keyarr = request.args.getlist('keyarr[]', type=str)
        hstrarr = request.args.getlist('hstrarr[]', type=str)
        ifso = request.args.get('ifso', type=str)
    sql = ""
    i = 0
    if int(ifso) > 0:
        while i < len(filedarr):
            h = hstrarr[i]
            f = filedarr[i]
            k = keyarr[i]
            if "like" in h:
                sql = sql + " and " + f + " like  '%" + k + "%' "
            else:
                sql = sql + " and " + f + h + k
            i += 1
    totalCount = jilvDao.count(dao, sql)  # 总条数
    totalPage = totalCount / pageSize
    if totalCount % pageSize != 0:
        totalPage = totalCount / pageSize + 1
        # 总页数
    totalPage = int(totalPage)
    limitstr = ""
    pageIndex = int(pageIndex)  # 通过url匹配的参数都是字符串类型需要转换成int型
    # 如果当前页码小于等于1，从第一条记录开始查询
    if pageIndex <= 1:
        start = 0
    else:
        # 否则，计算开始查询的位置
        start = (pageIndex - 1) * pageSize

    # 计算查询的结束位置，实际上此处计算的是查询的数量
    end = pageSize

    # 构建 limit 子句
    limitstr = f" LIMIT {start},{end}"
    print(sql + limitstr + " order by id desc")
    datalist = jilvDao.find(dao, sql + " order by id desc " + limitstr)
    data = {
        'action': 'queryJilvAll',
        'msg': '666666',
        'enlist': list(datalist),
        "entity": {"sumpage": totalPage, "count": totalCount, "page": pageIndex},
    }
    return data


@jilv.route("/jilv/queryJilvById", methods=['GET', 'POST'])
def queryJilvById():
    if request.method == 'POST':
        id = request.form.get('id', type=str)
    else:
        id = request.args.get('id', type=str)

    datalist = jilvDao.find(dao, " and id=" + id)
    print(datalist)
    if len(datalist) > 0:
        data = {
            'action': 'queryJilvById',
            'msg': '666666',
            'enlist': list(datalist),
            "entity": {"sumpage": 1, "count": 1, "page": 1},
        }
    else:
        data = {
            'action': 'queryJilvById',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }

    # 返回结果
    return data


@jilv.route("/jilv/deleteJilvByIds", methods=['GET', 'POST'])
def deleteJilvByIds():
    if request.method == 'POST':
        id = request.form.get('ids', type=str)
    else:
        id = request.args.get('ids', type=str)
    d = jilvDao.delete(dao, " and id in (" + id + ")")
    data = {
        'action': 'deleteJilvByIds',
        'msg': '000000',
        'enlist': "",
        "entity": {"sumpage": 0, "count": 0, "page": 0},
    }

    # 返回结果
    return data


@jilv.route("/jilv/topJilvNumList", methods=['GET', 'POST'])
def topJilvNumList():  # 按top
    orderby = ""
    whstr = ""
    sql = ""
    num = 0
    if request.method == 'POST':
        num = request.form.get('num')
        whstr = request.form.get('whstr')
        orderby = request.form.get('orderby')
    else:
        num = request.args.get('num', type=str)
        whstr = request.args.get('whstr', type=str)
        orderby = request.args.get('orderby', type=str)
    if orderby == "" or orderby is None:
        orderby = " order by id desc "
    if whstr == "" or whstr is None:
        whstr = ""
    if num == "0" or num is None:
        sql = whstr + " " + orderby
    else:
        sql = whstr + " " + orderby + " limit " + str(num)
    print(sql)
    totalCount = jilvDao.count(dao, sql)  # 总条数
    datalist = jilvDao.find(dao, sql)
    if len(datalist) > 0:
        data = {
            'action': 'topJilvNumList',
            'msg': '666666',
            'enlist': list(datalist),
            "entity": {"sumpage": 1, "count": totalCount, "page": 1},
        }
    else:
        data = {
            'action': 'topJilvNumList',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }
    return data


import os
import pandas as pd
from PIL import Image
from sklearn.preprocessing import LabelEncoder
import torch
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights
from sklearn.model_selection import train_test_split

from dao.soyuanDao import soyuanDao

soyuandao = soyuanDao()
path = os.path.join(os.path.abspath('.'), 'static', 'upload')
print(path)
datalist = soyuandao.db.query("SELECT id, img1, img2, img3 FROM soyuan ORDER BY id DESC")
try:
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

except:
    print(0)


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
try:
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
except:
    print(0)


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


try:
    train_model(model, 50)
    torch.save(model.state_dict(), 'model_weights2.pth')
except:
    print(0)


# 使用训练好的模型来预测指定图片的ID
def predict_image(image_path):
    model = resnet18(weights=None)
    num_ftrs = model.fc.in_features
    model.fc = torch.nn.Linear(num_ftrs, len(label_encoder.classes_))
    model.load_state_dict(torch.load('model_weights2.pth'))
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


@jilv.route("/jilv/addJilvSubmit", methods=['GET', 'POST'])
def addJilvSubmit():  # 添加
    msg = "000000"
    if request.method == 'POST':
        title = request.form.get('title')
        uptime = request.form.get('uptime')
        uid = request.form.get('uid')
        jie = request.form.get('jie')
        picurl = request.form.get('picurl')

    else:
        title = request.args.get('title', type=str)
        uptime = request.args.get('uptime', type=str)
        uid = request.args.get('uid', type=str)
        jie = request.args.get('jie', type=str)
        picurl = request.args.get('picurl', type=str)
    if picurl != '':
        print(picurl)
        image_path = os.path.join(path, picurl)
        predicted_id = predict_image(image_path)
        print(predicted_id)
        solist = soyuandao.find(" and  id = " + str(int(predicted_id)) + "")
        jie = "识别中"
        nong = ""
        print(solist)
        if len(solist) > 0:
            print('predicted_id:', predicted_id)
            nong = solist[0]['nong']
            jie = str(int(predicted_id))
            print(jie)
            dao.SetTitle(title)
            dao.SetUptime(uptime)
            dao.SetUid(uid)
            dao.SetJie(jie)
            dao.SetPicurl(picurl)

            jilvDao.add(dao)
            msg = "666666"
        else:
            jie = "识别中"

    data = {
        'action': 'addJilvSubmit',
        'nong': nong,
        'list': list(solist),
        'jie': jie,
        'msg': msg,

    }
    return data


@jilv.route("/jilv/updateJilvSubmit", methods=['GET', 'POST'])
def updateJilvSubmit():  # 修改
    msg = "000000"
    if request.method == 'POST':
        id = request.form.get('id', type=str)
        title = request.form.get('title')
        uptime = request.form.get('uptime')
        uid = request.form.get('uid')
        jie = request.form.get('jie')
        picurl = request.form.get('picurl')

    else:
        id = request.args.get('id', type=str)
        title = request.args.get('title', type=str)
        uptime = request.args.get('uptime', type=str)
        uid = request.args.get('uid', type=str)
        jie = request.args.get('jie', type=str)
        picurl = request.args.get('picurl', type=str)

    try:
        if 1 == 1 and title != '' and uptime != '' and uid != '' and jie != '' and picurl != '':
            dao.SetTitle(title)
            dao.SetUptime(uptime)
            dao.SetUid(uid)
            dao.SetJie(jie)
            dao.SetPicurl(picurl)

            dao.SetId(id)
            jilvDao.edit(dao, " ")
            msg = "666666"
        else:
            msg = "100008"
    except:
        msg = "000000"
    data = {
        'action': 'updateJilvSubmit',
        'msg': msg,

    }
    return data
