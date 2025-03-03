
from dao.liuyanDao import liuyanDao
from flask import Blueprint, request, session

liuyan = Blueprint('liuyan', __name__)
dao = liuyanDao()


@liuyan.route("/liuyan/queryLiuyanAll", methods=['GET', 'POST'])
def queryLiuyanAll():
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
    totalCount = liuyanDao.count(dao, sql)  # 总条数
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
    datalist = liuyanDao.find(dao, sql + " order by id desc " + limitstr)
    data = {
        'action': 'queryLiuyanAll',
        'msg': '666666',
        'enlist': list(datalist),
        "entity": {"sumpage": totalPage, "count": totalCount, "page": pageIndex},
    }
    return data


@liuyan.route("/liuyan/queryLiuyanById", methods=['GET', 'POST'])
def queryLiuyanById():
    if request.method == 'POST':
        id = request.form.get('id', type=str)
    else:
        id = request.args.get('id', type=str)

    datalist = liuyanDao.find(dao, " and id=" + id)
    print(datalist)
    if len(datalist) > 0:
        data = {
            'action': 'queryLiuyanById',
            'msg': '666666',
            'enlist': list(datalist),
            "entity": {"sumpage": 1, "count": 1, "page": 1},
        }
    else:
        data = {
            'action': 'queryLiuyanById',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }

    # 返回结果
    return data


@liuyan.route("/liuyan/deleteLiuyanByIds", methods=['GET', 'POST'])
def deleteLiuyanByIds():
    if request.method == 'POST':
        id = request.form.get('ids', type=str)
    else:
        id = request.args.get('ids', type=str)
    d = liuyanDao.delete(dao, " and id in (" + id + ")")
    data = {
            'action': 'deleteLiuyanByIds',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }

    # 返回结果
    return data


@liuyan.route("/liuyan/topLiuyanNumList", methods=['GET', 'POST'])
def topLiuyanNumList():  # 按top
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
    totalCount = liuyanDao.count(dao, sql)  # 总条数
    datalist = liuyanDao.find(dao, sql)
    if len(datalist) > 0:
        data = {
            'action': 'topLiuyanNumList',
            'msg': '666666',
            'enlist': list(datalist),
            "entity": {"sumpage": 1, "count": totalCount , "page": 1},
        }
    else:
        data = {
            'action': 'topLiuyanNumList',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }
    return data


@liuyan.route("/liuyan/addLiuyanSubmit", methods=['GET', 'POST'])
def addLiuyanSubmit():  # 添加
    msg = "000000"
    if request.method == 'POST':
        uid = request.form.get('uid')
        memo = request.form.get('memo')
        huimemo = request.form.get('huimemo')
        uptime = request.form.get('uptime')

    else:
        uid = request.args.get('uid', type=str)
        memo = request.args.get('memo', type=str)
        huimemo = request.args.get('huimemo', type=str)
        uptime = request.args.get('uptime', type=str)

    try:
        if 1 == 1 and uid != '' and memo != '' and huimemo != '' and uptime != '':
            dao.SetUid(uid)
            dao.SetMemo(memo)
            dao.SetHuimemo(huimemo)
            dao.SetUptime(uptime)

            liuyanDao.add(dao)
            msg = "666666"
        else:
            msg = "100008"
    except:
        msg = "000000"
    data = {
        'action': 'addLiuyanSubmit',
        'msg': msg,

    }
    return data


@liuyan.route("/liuyan/updateLiuyanSubmit", methods=['GET', 'POST'])
def updateLiuyanSubmit():  # 修改
    msg = "000000"
    if request.method == 'POST':
        id = request.form.get('id', type=str)
        uid = request.form.get('uid')
        memo = request.form.get('memo')
        huimemo = request.form.get('huimemo')
        uptime = request.form.get('uptime')

    else:
        id = request.args.get('id', type=str)
        uid = request.args.get('uid', type=str)
        memo = request.args.get('memo', type=str)
        huimemo = request.args.get('huimemo', type=str)
        uptime = request.args.get('uptime', type=str)

    try:
        if 1 == 1 and uid != '' and memo != '' and huimemo != '' and uptime != '':
            dao.SetUid(uid)
            dao.SetMemo(memo)
            dao.SetHuimemo(huimemo)
            dao.SetUptime(uptime)

            dao.SetId(id)
            liuyanDao.edit(dao, " ")
            msg = "666666"
        else:
            msg = "100008"
    except:
        msg = "000000"
    data = {
        'action': 'updateLiuyanSubmit',
        'msg': msg,

    }
    return data


