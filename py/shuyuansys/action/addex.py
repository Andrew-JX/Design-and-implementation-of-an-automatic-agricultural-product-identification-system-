
import datetime
import random
import re
import time
import urllib.request
import json

import lxml
import pandas as pd

import parsel
import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request
import os

from dao.useradminDao import useradminDao  # 管理员
from dao.userlistDao import userlistDao  # 用户
from dao.soyuanDao import soyuanDao  # 溯源信息
from dao.jilvDao import jilvDao  # 检测记录
from dao.liuyanDao import liuyanDao  # 留言
from dao.wenfeiDao import wenfeiDao  # 文章分类
from dao.articleDao import articleDao  # 文章


ex = Blueprint('ex', __name__)
path = os.path.abspath('.') + '\\static\\upload\\'

# 导入管理员数据
@ex.route("/useradminEx", methods=['GET', 'POST'])
def useradminEx():  # 导入添加
    msg = "000000"
    username = "" # 用户名
    password = "" # 密码
    name1 = "" # 姓名
    tel = "" # 手机

    exfilename = ""
    if request.method == 'POST':
        exfilename = request.args.get('exfilename')
    elif request.method == 'GET':
        exfilename = request.args.get('exfilename', type=str)
    print(path + exfilename)
    df = pd.DataFrame()
    if ".csv" in exfilename:
        df = pd.read_csv(path + exfilename, encoding='gbk')
    df.fillna(0, inplace=True)
    print(df)
    for dt in df.itertuples():
        if 1 == 1 and dt.用户名 != 0 and dt.密码 != 0 and dt.姓名 != 0 and dt.手机 != 0:
            username = dt.用户名
            password = dt.密码
            name1 = dt.姓名
            tel = dt.手机
            if 1 == 1 and username != '' and password != '' and name1 != '' and tel != '':
                # 入库----
                useradmindao = useradminDao()
                useradmindao.SetUsername(username)
                useradmindao.SetPassword(password)
                useradmindao.SetName1(name1)
                useradmindao.SetTel(tel)
                useradminDao.addreplace(useradmindao)
    # --------------
    msg = "666666"
    data = {
        'action': 'useradminSp',
        'msg': msg,
    }
    return data

# 导入用户数据
@ex.route("/userlistEx", methods=['GET', 'POST'])
def userlistEx():  # 导入添加
    msg = "000000"
    username = "" # 用户名
    password = "" # 密码
    cname = "" # 姓名
    sex = "" # 性别
    tel = "" # 手机
    email = "" # 邮箱

    exfilename = ""
    if request.method == 'POST':
        exfilename = request.args.get('exfilename')
    elif request.method == 'GET':
        exfilename = request.args.get('exfilename', type=str)
    print(path + exfilename)
    df = pd.DataFrame()
    if ".csv" in exfilename:
        df = pd.read_csv(path + exfilename, encoding='gbk')
    df.fillna(0, inplace=True)
    print(df)
    for dt in df.itertuples():
        if 1 == 1 and dt.用户名 != 0 and dt.密码 != 0 and dt.姓名 != 0 and dt.性别 != 0 and dt.手机 != 0 and dt.邮箱 != 0:
            username = dt.用户名
            password = dt.密码
            cname = dt.姓名
            sex = dt.性别
            tel = dt.手机
            email = dt.邮箱
            if 1 == 1 and username != '' and password != '' and cname != '' and sex != '' and tel != '' and email != '':
                # 入库----
                userlistdao = userlistDao()
                userlistdao.SetUsername(username)
                userlistdao.SetPassword(password)
                userlistdao.SetCname(cname)
                userlistdao.SetSex(sex)
                userlistdao.SetTel(tel)
                userlistdao.SetEmail(email)
                userlistDao.addreplace(userlistdao)
    # --------------
    msg = "666666"
    data = {
        'action': 'userlistSp',
        'msg': msg,
    }
    return data

# 导入溯源信息数据
@ex.route("/soyuanEx", methods=['GET', 'POST'])
def soyuanEx():  # 导入添加
    msg = "000000"
    nong = "" # 农产品
    picurl = "" # 产品图片
    bo = "" # 播种
    chetime = "" # 上市时间
    shi = "" # 施肥
    sheng = "" # 生长
    shou = "" # 收购
    yun = "" # 运输
    er = "" # 码
    uptime = "" # 上传时间
    bh = "" # 序号
    img1 = "" # 图片1
    img2 = "" # 图片2
    img3 = "" # 图片3

    exfilename = ""
    if request.method == 'POST':
        exfilename = request.args.get('exfilename')
    elif request.method == 'GET':
        exfilename = request.args.get('exfilename', type=str)
    print(path + exfilename)
    df = pd.DataFrame()
    if ".csv" in exfilename:
        df = pd.read_csv(path + exfilename, encoding='gbk')
    df.fillna(0, inplace=True)
    print(df)
    for dt in df.itertuples():
        if 1 == 1 and dt.农产品 != 0 and dt.产品图片 != 0 and dt.播种 != 0 and dt.上市时间 != 0 and dt.施肥 != 0 and dt.生长 != 0 and dt.收购 != 0 and dt.运输 != 0 and dt.码 != 0 and dt.上传时间 != 0 and dt.序号 != 0 and dt.图片1 != 0 and dt.图片2 != 0 and dt.图片3 != 0:
            nong = dt.农产品
            picurl = dt.产品图片
            bo = dt.播种
            chetime = dt.上市时间
            shi = dt.施肥
            sheng = dt.生长
            shou = dt.收购
            yun = dt.运输
            er = dt.码
            uptime = dt.上传时间
            bh = dt.序号
            img1 = dt.图片1
            img2 = dt.图片2
            img3 = dt.图片3
            if 1 == 1 and nong != '' and picurl != '' and bo != '' and chetime != '' and shi != '' and sheng != '' and shou != '' and yun != '' and er != '' and uptime != '' and bh != '' and img1 != '' and img2 != '' and img3 != '':
                # 入库----
                soyuandao = soyuanDao()
                soyuandao.SetNong(nong)
                soyuandao.SetPicurl(picurl)
                soyuandao.SetBo(bo)
                soyuandao.SetChetime(chetime)
                soyuandao.SetShi(shi)
                soyuandao.SetSheng(sheng)
                soyuandao.SetShou(shou)
                soyuandao.SetYun(yun)
                soyuandao.SetEr(er)
                soyuandao.SetUptime(uptime)
                soyuandao.SetBh(bh)
                soyuandao.SetImg1(img1)
                soyuandao.SetImg2(img2)
                soyuandao.SetImg3(img3)
                soyuanDao.addreplace(soyuandao)
    # --------------
    msg = "666666"
    data = {
        'action': 'soyuanSp',
        'msg': msg,
    }
    return data

# 导入检测记录数据
@ex.route("/jilvEx", methods=['GET', 'POST'])
def jilvEx():  # 导入添加
    msg = "000000"
    title = "" # 标题
    uptime = "" # 检测时间
    uid = "" # 用户
    jie = "" # 结果
    picurl = "" # 图片

    exfilename = ""
    if request.method == 'POST':
        exfilename = request.args.get('exfilename')
    elif request.method == 'GET':
        exfilename = request.args.get('exfilename', type=str)
    print(path + exfilename)
    df = pd.DataFrame()
    if ".csv" in exfilename:
        df = pd.read_csv(path + exfilename, encoding='gbk')
    df.fillna(0, inplace=True)
    print(df)
    for dt in df.itertuples():
        if 1 == 1 and dt.标题 != 0 and dt.检测时间 != 0 and dt.用户 != 0 and dt.结果 != 0 and dt.图片 != 0:
            title = dt.标题
            uptime = dt.检测时间
            uid = dt.用户
            jie = dt.结果
            picurl = dt.图片
            if 1 == 1 and title != '' and uptime != '' and uid != '' and jie != '' and picurl != '':
                # 入库----
                jilvdao = jilvDao()
                jilvdao.SetTitle(title)
                jilvdao.SetUptime(uptime)
                jilvdao.SetUid(uid)
                jilvdao.SetJie(jie)
                jilvdao.SetPicurl(picurl)
                jilvDao.addreplace(jilvdao)
    # --------------
    msg = "666666"
    data = {
        'action': 'jilvSp',
        'msg': msg,
    }
    return data

# 导入留言数据
@ex.route("/liuyanEx", methods=['GET', 'POST'])
def liuyanEx():  # 导入添加
    msg = "000000"
    uid = "" # 用户
    memo = "" # 内容
    huimemo = "" # 回复
    uptime = "" # 时间

    exfilename = ""
    if request.method == 'POST':
        exfilename = request.args.get('exfilename')
    elif request.method == 'GET':
        exfilename = request.args.get('exfilename', type=str)
    print(path + exfilename)
    df = pd.DataFrame()
    if ".csv" in exfilename:
        df = pd.read_csv(path + exfilename, encoding='gbk')
    df.fillna(0, inplace=True)
    print(df)
    for dt in df.itertuples():
        if 1 == 1 and dt.用户 != 0 and dt.内容 != 0 and dt.回复 != 0 and dt.时间 != 0:
            uid = dt.用户
            memo = dt.内容
            huimemo = dt.回复
            uptime = dt.时间
            if 1 == 1 and uid != '' and memo != '' and huimemo != '' and uptime != '':
                # 入库----
                liuyandao = liuyanDao()
                liuyandao.SetUid(uid)
                liuyandao.SetMemo(memo)
                liuyandao.SetHuimemo(huimemo)
                liuyandao.SetUptime(uptime)
                liuyanDao.addreplace(liuyandao)
    # --------------
    msg = "666666"
    data = {
        'action': 'liuyanSp',
        'msg': msg,
    }
    return data

# 导入文章分类数据
@ex.route("/wenfeiEx", methods=['GET', 'POST'])
def wenfeiEx():  # 导入添加
    msg = "000000"
    fenleiname = "" # 分类名

    exfilename = ""
    if request.method == 'POST':
        exfilename = request.args.get('exfilename')
    elif request.method == 'GET':
        exfilename = request.args.get('exfilename', type=str)
    print(path + exfilename)
    df = pd.DataFrame()
    if ".csv" in exfilename:
        df = pd.read_csv(path + exfilename, encoding='gbk')
    df.fillna(0, inplace=True)
    print(df)
    for dt in df.itertuples():
        if 1 == 1 and dt.分类名 != 0:
            fenleiname = dt.分类名
            if 1 == 1 and fenleiname != '':
                # 入库----
                wenfeidao = wenfeiDao()
                wenfeidao.SetFenleiname(fenleiname)
                wenfeiDao.addreplace(wenfeidao)
    # --------------
    msg = "666666"
    data = {
        'action': 'wenfeiSp',
        'msg': msg,
    }
    return data

# 导入文章数据
@ex.route("/articleEx", methods=['GET', 'POST'])
def articleEx():  # 导入添加
    msg = "000000"
    cid = "" # 分类
    title = "" # 标题
    picurl = "" # 图片
    memo = "" # 内容
    uptime = "" # 发布时间

    exfilename = ""
    if request.method == 'POST':
        exfilename = request.args.get('exfilename')
    elif request.method == 'GET':
        exfilename = request.args.get('exfilename', type=str)
    print(path + exfilename)
    df = pd.DataFrame()
    if ".csv" in exfilename:
        df = pd.read_csv(path + exfilename, encoding='gbk')
    df.fillna(0, inplace=True)
    print(df)
    for dt in df.itertuples():
        if 1 == 1 and dt.分类 != 0 and dt.标题 != 0 and dt.图片 != 0 and dt.内容 != 0 and dt.发布时间 != 0:
            cid = dt.分类
            title = dt.标题
            picurl = dt.图片
            memo = dt.内容
            uptime = dt.发布时间
            if 1 == 1 and cid != '' and title != '' and picurl != '' and memo != '' and uptime != '':
                # 入库----
                articledao = articleDao()
                articledao.SetCid(cid)
                articledao.SetTitle(title)
                articledao.SetPicurl(picurl)
                articledao.SetMemo(memo)
                articledao.SetUptime(uptime)
                articleDao.addreplace(articledao)
    # --------------
    msg = "666666"
    data = {
        'action': 'articleSp',
        'msg': msg,
    }
    return data

