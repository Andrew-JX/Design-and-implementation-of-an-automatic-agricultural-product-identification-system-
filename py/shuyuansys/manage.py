import time

import os
import argparse
from tqdm import trange


from os.path import join
from flask import Flask, redirect, url_for, request, render_template

from action.useradminAction import useradmin  # 管理员
from action.userlistAction import userlist  # 用户
from action.soyuanAction import soyuan  # 溯源信息
from action.jilvAction import jilv  # 检测记录
from action.liuyanAction import liuyan  # 留言
from action.wenfeiAction import wenfei  # 文章分类
from action.articleAction import article  # 文章

from action.spider import sp  #
from action.tongji import tj  #
from action.addex import ex  #

app = Flask(__name__, template_folder='./static')
app.config["JSON_AS_ASCII"] = False  # 防止返回中文乱码

app.register_blueprint(useradmin)  # 管理员
app.register_blueprint(userlist)  # 用户
app.register_blueprint(soyuan)  # 溯源信息
app.register_blueprint(jilv)  # 检测记录
app.register_blueprint(liuyan)  # 留言
app.register_blueprint(wenfei)  # 文章分类
app.register_blueprint(article)  # 文章

app.register_blueprint(sp)  #
app.register_blueprint(tj)  #
app.register_blueprint(ex)  #

app.config["SECRET_KEY"] = "shuyuansyssession"

project = "shuyuansys"


@app.route("/doUploadjson", methods=["POST"])
def doUploadjson():  # 上传保存
    msg = "666666"
    try:
        file = request.files.get('file')
        if file is None:
            msg = "000000"
            data = {
                'action': 'doUpload',
                'msg': msg,
            }
        else:
            current_path = os.path.abspath(os.path.dirname(__file__)).split(project)[0]  # 根路径
            file_path = current_path + project + '\\static\\upload'
            print(file_path)
            if not os.path.exists(file_path):  # 文件夹不存在则创建
                os.mkdir(file_path)
            filenameExp = file.filename.split('.')[1]  # 文件扩展名
            filenameMain = get_order_code()
            filename = filenameMain + "." + filenameExp
            urlpath = "/static/" + "upload/" + filename
            file.save(file_path + "\\" + filename)
            msg = "666666"
            data = {
                'action': 'doUpload',
                'msg': msg,
                'enlist': [filename],
                "entity": {"urlpath": urlpath, "filename": filename, "filenameMain": filenameMain,
                           "filenameExp": filenameExp},
            }
    except:
        msg = "000000"
        data = {
            'action': 'doUpload',
            'msg': msg,
        }
    return data


#  生成号
def get_order_code():
    #  年月日时分秒+time.time()的后7位
    order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + str(time.time()).replace('.', '')[-7:])
    return order_no


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)


