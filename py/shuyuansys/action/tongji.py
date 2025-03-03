
import re
import time
import urllib.request
import json

import lxml

import parsel
import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request, session
 	
from dao.useradminDao import useradminDao  # 管理员
from dao.userlistDao import userlistDao  # 用户
from dao.soyuanDao import soyuanDao  # 溯源信息
from dao.jilvDao import jilvDao  # 检测记录
from dao.liuyanDao import liuyanDao  # 留言
from dao.wenfeiDao import wenfeiDao  # 文章分类
from dao.articleDao import articleDao  # 文章


tj = Blueprint('tj', __name__)

soyuandao = soyuanDao()  # 溯源信息
jilvdao = jilvDao()  # 检测记录
liuyandao = liuyanDao()  # 留言
wenfeidao = wenfeiDao()  # 文章分类
articledao = articleDao()  # 文章



# 统计溯源信息数据
@tj.route("/soyuanTj", methods=['GET', 'POST'])
def soyuanTj():  # 
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

    # nong,picurl,bo,chetime,shi,sheng,shou,yun,er,uptime,bh,img1,img2,img3,
    act = request.args.get('act') 
    datalist = list(soyuandao.db.query("select * from soyuan where 1=1 order by id desc"))
    # --------------
    msg = "666666"
    data = {
        'action': 'soyuanTj',
        'enlist': list(datalist),
        'msg': msg,
    }
    return data

# 统计检测记录数据
@tj.route("/jilvTj", methods=['GET', 'POST'])
def jilvTj():  # 
    msg = "000000"
    title = "" # 标题
    uptime = "" # 检测时间
    uid = "" # 用户
    jie = "" # 结果
    picurl = "" # 图片

    # title,uptime,uid,jie,picurl,
    act = request.args.get('act') 
    datalist = list(jilvdao.db.query("select * from jilv where 1=1 order by id desc"))
    # --------------
    msg = "666666"
    data = {
        'action': 'jilvTj',
        'enlist': list(datalist),
        'msg': msg,
    }
    return data

# 统计留言数据
@tj.route("/liuyanTj", methods=['GET', 'POST'])
def liuyanTj():  # 
    msg = "000000"
    uid = "" # 用户
    memo = "" # 内容
    huimemo = "" # 回复
    uptime = "" # 时间

    # uid,memo,huimemo,uptime,
    act = request.args.get('act') 
    datalist = list(liuyandao.db.query("select * from liuyan where 1=1 order by id desc"))
    # --------------
    msg = "666666"
    data = {
        'action': 'liuyanTj',
        'enlist': list(datalist),
        'msg': msg,
    }
    return data

# 统计文章分类数据
@tj.route("/wenfeiTj", methods=['GET', 'POST'])
def wenfeiTj():  # 
    msg = "000000"
    fenleiname = "" # 分类名

    # fenleiname,
    act = request.args.get('act') 
    datalist = list(wenfeidao.db.query("select * from wenfei where 1=1 order by id desc"))
    # --------------
    msg = "666666"
    data = {
        'action': 'wenfeiTj',
        'enlist': list(datalist),
        'msg': msg,
    }
    return data

# 统计文章数据
@tj.route("/articleTj", methods=['GET', 'POST'])
def articleTj():  # 
    msg = "000000"
    cid = "" # 分类
    title = "" # 标题
    picurl = "" # 图片
    memo = "" # 内容
    uptime = "" # 发布时间

    # cid,title,picurl,memo,uptime,
    act = request.args.get('act') 
    datalist = list(articledao.db.query("select * from article where 1=1 order by id desc"))
    # --------------
    msg = "666666"
    data = {
        'action': 'articleTj',
        'enlist': list(datalist),
        'msg': msg,
    }
    return data


