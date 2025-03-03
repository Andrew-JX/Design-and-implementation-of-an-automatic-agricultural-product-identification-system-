
import datetime
import random
import re
import time
import urllib.request
import json

import lxml

import parsel
import requests
from bs4 import BeautifulSoup
from flask import Blueprint

from dao.useradminDao import useradminDao  # 管理员
from dao.userlistDao import userlistDao  # 用户
from dao.soyuanDao import soyuanDao  # 溯源信息
from dao.jilvDao import jilvDao  # 检测记录
from dao.liuyanDao import liuyanDao  # 留言
from dao.wenfeiDao import wenfeiDao  # 文章分类
from dao.articleDao import articleDao  # 文章


sp = Blueprint('sp', __name__)


# 返回html
def gethtml(url, ma):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/92.0.4515.107 Safari/537.36'}
    datapost = {}
    print("开始爬=" + url)
    # 2发送网络请求
    re = requests.get(url, headers=headers, data=datapost)
    re.encoding = ma
    html_data = re.text
    return html_data


def gethtmllis(url, lisstr, ma):
    html_data = gethtml(url, ma)
    # print(html_data)
    # 3数据的解析
    # 3.1 转换数据类型
    selector = parsel.Selector(html_data)  # 对象
    # 3.2数据提取
    lis = selector.xpath(lisstr)
    return lis


# 采集溯源信息数据
@sp.route("/soyuanSp", methods=['GET', 'POST'])
def soyuanSp():  # 添加
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

    url = ""  # 采集溯源信息的网址

    for page in range(1, 100): # 列表页数 
        url = f"https://place.qyer.com/china/citylist-0-0-{page}/"
        lis = gethtmllis(url, '//ul[@class="plcCitylist"]/li', "utf-8") # 数据提取

        for li in lis:



            nong = li.xpath('.//h3/a/text()').get().strip() # 农产品 
            picurl = li.xpath('.//h3/a/text()').get().strip() # 产品图片 
            bo = li.xpath('.//h3/a/text()').get().strip() # 播种 
            chetime = li.xpath('.//h3/a/text()').get().strip() # 上市时间 
            shi = li.xpath('.//h3/a/text()').get().strip() # 施肥 
            sheng = li.xpath('.//h3/a/text()').get().strip() # 生长 
            shou = li.xpath('.//h3/a/text()').get().strip() # 收购 
            yun = li.xpath('.//h3/a/text()').get().strip() # 运输 
            er = li.xpath('.//h3/a/text()').get().strip() # 码 
            uptime = li.xpath('.//h3/a/text()').get().strip() # 上传时间 
            bh = li.xpath('.//h3/a/text()').get().strip() # 序号 
            img1 = li.xpath('.//h3/a/text()').get().strip() # 图片1 
            img2 = li.xpath('.//h3/a/text()').get().strip() # 图片2 
            img3 = li.xpath('.//h3/a/text()').get().strip() # 图片3 


            print(nong,picurl,bo,chetime,shi,sheng,shou,yun,er,uptime,bh,img1,img2,img3, sep='|')

            # 保存数据
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

# 采集检测记录数据
@sp.route("/jilvSp", methods=['GET', 'POST'])
def jilvSp():  # 添加
    msg = "000000"
    title = "" # 标题
    uptime = "" # 检测时间
    uid = "" # 用户
    jie = "" # 结果
    picurl = "" # 图片

    url = ""  # 采集检测记录的网址

    for page in range(1, 100): # 列表页数 
        url = f"https://place.qyer.com/china/citylist-0-0-{page}/"
        lis = gethtmllis(url, '//ul[@class="plcCitylist"]/li', "utf-8") # 数据提取

        for li in lis:



            title = li.xpath('.//h3/a/text()').get().strip() # 标题 
            uptime = li.xpath('.//h3/a/text()').get().strip() # 检测时间 
            uid = li.xpath('.//h3/a/text()').get().strip() # 用户 
            jie = li.xpath('.//h3/a/text()').get().strip() # 结果 
            picurl = li.xpath('.//h3/a/text()').get().strip() # 图片 


            print(title,uptime,uid,jie,picurl, sep='|')

            # 保存数据
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

# 采集留言数据
@sp.route("/liuyanSp", methods=['GET', 'POST'])
def liuyanSp():  # 添加
    msg = "000000"
    uid = "" # 用户
    memo = "" # 内容
    huimemo = "" # 回复
    uptime = "" # 时间

    url = ""  # 采集留言的网址

    for page in range(1, 100): # 列表页数 
        url = f"https://place.qyer.com/china/citylist-0-0-{page}/"
        lis = gethtmllis(url, '//ul[@class="plcCitylist"]/li', "utf-8") # 数据提取

        for li in lis:



            uid = li.xpath('.//h3/a/text()').get().strip() # 用户 
            memo = li.xpath('.//h3/a/text()').get().strip() # 内容 
            huimemo = li.xpath('.//h3/a/text()').get().strip() # 回复 
            uptime = li.xpath('.//h3/a/text()').get().strip() # 时间 


            print(uid,memo,huimemo,uptime, sep='|')

            # 保存数据
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

# 采集文章分类数据
@sp.route("/wenfeiSp", methods=['GET', 'POST'])
def wenfeiSp():  # 添加
    msg = "000000"
    fenleiname = "" # 分类名

    url = ""  # 采集文章分类的网址

    for page in range(1, 100): # 列表页数 
        url = f"https://place.qyer.com/china/citylist-0-0-{page}/"
        lis = gethtmllis(url, '//ul[@class="plcCitylist"]/li', "utf-8") # 数据提取

        for li in lis:



            fenleiname = li.xpath('.//h3/a/text()').get().strip() # 分类名 


            print(fenleiname, sep='|')

            # 保存数据
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

# 采集文章数据
@sp.route("/articleSp", methods=['GET', 'POST'])
def articleSp():  # 添加
    msg = "000000"
    cid = "" # 分类
    title = "" # 标题
    picurl = "" # 图片
    memo = "" # 内容
    uptime = "" # 发布时间

    url = ""  # 采集文章的网址

    for page in range(1, 100): # 列表页数 
        url = f"https://place.qyer.com/china/citylist-0-0-{page}/"
        lis = gethtmllis(url, '//ul[@class="plcCitylist"]/li', "utf-8") # 数据提取

        for li in lis:



            cid = li.xpath('.//h3/a/text()').get().strip() # 分类 
            title = li.xpath('.//h3/a/text()').get().strip() # 标题 
            picurl = li.xpath('.//h3/a/text()').get().strip() # 图片 
            memo = li.xpath('.//h3/a/text()').get().strip() # 内容 
            uptime = li.xpath('.//h3/a/text()').get().strip() # 发布时间 


            print(cid,title,picurl,memo,uptime, sep='|')

            # 保存数据
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

