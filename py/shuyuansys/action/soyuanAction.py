
from dao.soyuanDao import soyuanDao
from flask import Blueprint, request, session

soyuan = Blueprint('soyuan', __name__)
dao = soyuanDao()


@soyuan.route("/soyuan/querySoyuanAll", methods=['GET', 'POST'])
def querySoyuanAll():
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
    totalCount = soyuanDao.count(dao, sql)  # 总条数
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
    datalist = soyuanDao.find(dao, sql + " order by id desc " + limitstr)
    data = {
        'action': 'querySoyuanAll',
        'msg': '666666',
        'enlist': list(datalist),
        "entity": {"sumpage": totalPage, "count": totalCount, "page": pageIndex},
    }
    return data


@soyuan.route("/soyuan/querySoyuanById", methods=['GET', 'POST'])
def querySoyuanById():
    if request.method == 'POST':
        id = request.form.get('id', type=str)
    else:
        id = request.args.get('id', type=str)

    datalist = soyuanDao.find(dao, " and id=" + id)
    print(datalist)
    if len(datalist) > 0:
        data = {
            'action': 'querySoyuanById',
            'msg': '666666',
            'enlist': list(datalist),
            "entity": {"sumpage": 1, "count": 1, "page": 1},
        }
    else:
        data = {
            'action': 'querySoyuanById',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }

    # 返回结果
    return data


@soyuan.route("/soyuan/deleteSoyuanByIds", methods=['GET', 'POST'])
def deleteSoyuanByIds():
    if request.method == 'POST':
        id = request.form.get('ids', type=str)
    else:
        id = request.args.get('ids', type=str)
    d = soyuanDao.delete(dao, " and id in (" + id + ")")
    data = {
            'action': 'deleteSoyuanByIds',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }

    # 返回结果
    return data


@soyuan.route("/soyuan/topSoyuanNumList", methods=['GET', 'POST'])
def topSoyuanNumList():  # 按top
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
    totalCount = soyuanDao.count(dao, sql)  # 总条数
    datalist = soyuanDao.find(dao, sql)
    if len(datalist) > 0:
        data = {
            'action': 'topSoyuanNumList',
            'msg': '666666',
            'enlist': list(datalist),
            "entity": {"sumpage": 1, "count": totalCount , "page": 1},
        }
    else:
        data = {
            'action': 'topSoyuanNumList',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }
    return data


@soyuan.route("/soyuan/addSoyuanSubmit", methods=['GET', 'POST'])
def addSoyuanSubmit():  # 添加
    msg = "000000"
    if request.method == 'POST':
        nong = request.form.get('nong')
        picurl = request.form.get('picurl')
        bo = request.form.get('bo')
        chetime = request.form.get('chetime')
        shi = request.form.get('shi')
        sheng = request.form.get('sheng')
        shou = request.form.get('shou')
        yun = request.form.get('yun')
        er = request.form.get('er')
        uptime = request.form.get('uptime')
        bh = request.form.get('bh')
        img1 = request.form.get('img1')
        img2 = request.form.get('img2')
        img3 = request.form.get('img3')

    else:
        nong = request.args.get('nong', type=str)
        picurl = request.args.get('picurl', type=str)
        bo = request.args.get('bo', type=str)
        chetime = request.args.get('chetime', type=str)
        shi = request.args.get('shi', type=str)
        sheng = request.args.get('sheng', type=str)
        shou = request.args.get('shou', type=str)
        yun = request.args.get('yun', type=str)
        er = request.args.get('er', type=str)
        uptime = request.args.get('uptime', type=str)
        bh = request.args.get('bh', type=str)
        img1 = request.args.get('img1', type=str)
        img2 = request.args.get('img2', type=str)
        img3 = request.args.get('img3', type=str)

    try:
        if 1 == 1 and nong != '' and picurl != '' and bo != '' and chetime != '' and shi != '' and sheng != '' and shou != '' and yun != '' and er != '' and uptime != '' and bh != '' and img1 != '' and img2 != '' and img3 != '':
            dao.SetNong(nong)
            dao.SetPicurl(picurl)
            dao.SetBo(bo)
            dao.SetChetime(chetime)
            dao.SetShi(shi)
            dao.SetSheng(sheng)
            dao.SetShou(shou)
            dao.SetYun(yun)
            dao.SetEr(er)
            dao.SetUptime(uptime)
            dao.SetBh(bh)
            dao.SetImg1(img1)
            dao.SetImg2(img2)
            dao.SetImg3(img3)

            soyuanDao.add(dao)
            msg = "666666"
        else:
            msg = "100008"
    except:
        msg = "000000"
    data = {
        'action': 'addSoyuanSubmit',
        'msg': msg,

    }
    return data


@soyuan.route("/soyuan/updateSoyuanSubmit", methods=['GET', 'POST'])
def updateSoyuanSubmit():  # 修改
    msg = "000000"
    if request.method == 'POST':
        id = request.form.get('id', type=str)
        nong = request.form.get('nong')
        picurl = request.form.get('picurl')
        bo = request.form.get('bo')
        chetime = request.form.get('chetime')
        shi = request.form.get('shi')
        sheng = request.form.get('sheng')
        shou = request.form.get('shou')
        yun = request.form.get('yun')
        er = request.form.get('er')
        uptime = request.form.get('uptime')
        bh = request.form.get('bh')
        img1 = request.form.get('img1')
        img2 = request.form.get('img2')
        img3 = request.form.get('img3')

    else:
        id = request.args.get('id', type=str)
        nong = request.args.get('nong', type=str)
        picurl = request.args.get('picurl', type=str)
        bo = request.args.get('bo', type=str)
        chetime = request.args.get('chetime', type=str)
        shi = request.args.get('shi', type=str)
        sheng = request.args.get('sheng', type=str)
        shou = request.args.get('shou', type=str)
        yun = request.args.get('yun', type=str)
        er = request.args.get('er', type=str)
        uptime = request.args.get('uptime', type=str)
        bh = request.args.get('bh', type=str)
        img1 = request.args.get('img1', type=str)
        img2 = request.args.get('img2', type=str)
        img3 = request.args.get('img3', type=str)

    try:
        if 1 == 1 and nong != '' and picurl != '' and bo != ''   and img1 != '' and img2 != '' and img3 != '':
            dao.SetNong(nong)
            dao.SetPicurl(picurl)
            dao.SetBo(bo)
            dao.SetChetime(chetime)
            dao.SetShi(shi)
            dao.SetSheng(sheng)
            dao.SetShou(shou)
            dao.SetYun(yun)
            dao.SetEr(er)
            dao.SetUptime(uptime)
            dao.SetBh(bh)
            dao.SetImg1(img1)
            dao.SetImg2(img2)
            dao.SetImg3(img3)

            dao.SetId(id)
            soyuanDao.edit(dao, " ")
            msg = "666666"
        else:
            msg = "100008"
    except:
        msg = "000000"
    data = {
        'action': 'updateSoyuanSubmit',
        'msg': msg,

    }
    return data


