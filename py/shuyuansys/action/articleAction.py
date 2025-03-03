
from dao.articleDao import articleDao
from flask import Blueprint, request, session

article = Blueprint('article', __name__)
dao = articleDao()


@article.route("/article/queryArticleAll", methods=['GET', 'POST'])
def queryArticleAll():
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
    totalCount = articleDao.count(dao, sql)  # 总条数
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
    datalist = articleDao.find(dao, sql + " order by id desc " + limitstr)
    data = {
        'action': 'queryArticleAll',
        'msg': '666666',
        'enlist': list(datalist),
        "entity": {"sumpage": totalPage, "count": totalCount, "page": pageIndex},
    }
    return data


@article.route("/article/queryArticleById", methods=['GET', 'POST'])
def queryArticleById():
    if request.method == 'POST':
        id = request.form.get('id', type=str)
    else:
        id = request.args.get('id', type=str)

    datalist = articleDao.find(dao, " and id=" + id)
    print(datalist)
    if len(datalist) > 0:
        data = {
            'action': 'queryArticleById',
            'msg': '666666',
            'enlist': list(datalist),
            "entity": {"sumpage": 1, "count": 1, "page": 1},
        }
    else:
        data = {
            'action': 'queryArticleById',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }

    # 返回结果
    return data


@article.route("/article/deleteArticleByIds", methods=['GET', 'POST'])
def deleteArticleByIds():
    if request.method == 'POST':
        id = request.form.get('ids', type=str)
    else:
        id = request.args.get('ids', type=str)
    d = articleDao.delete(dao, " and id in (" + id + ")")
    data = {
            'action': 'deleteArticleByIds',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }

    # 返回结果
    return data


@article.route("/article/topArticleNumList", methods=['GET', 'POST'])
def topArticleNumList():  # 按top
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
    totalCount = articleDao.count(dao, sql)  # 总条数
    datalist = articleDao.find(dao, sql)
    if len(datalist) > 0:
        data = {
            'action': 'topArticleNumList',
            'msg': '666666',
            'enlist': list(datalist),
            "entity": {"sumpage": 1, "count": totalCount , "page": 1},
        }
    else:
        data = {
            'action': 'topArticleNumList',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }
    return data


@article.route("/article/addArticleSubmit", methods=['GET', 'POST'])
def addArticleSubmit():  # 添加
    msg = "000000"
    if request.method == 'POST':
        cid = request.form.get('cid')
        title = request.form.get('title')
        picurl = request.form.get('picurl')
        memo = request.form.get('memo')
        uptime = request.form.get('uptime')

    else:
        cid = request.args.get('cid', type=str)
        title = request.args.get('title', type=str)
        picurl = request.args.get('picurl', type=str)
        memo = request.args.get('memo', type=str)
        uptime = request.args.get('uptime', type=str)

    try:
        if 1 == 1 and cid != '' and title != '' and picurl != '' and memo != '' and uptime != '':
            dao.SetCid(cid)
            dao.SetTitle(title)
            dao.SetPicurl(picurl)
            dao.SetMemo(memo)
            dao.SetUptime(uptime)

            articleDao.add(dao)
            msg = "666666"
        else:
            msg = "100008"
    except:
        msg = "000000"
    data = {
        'action': 'addArticleSubmit',
        'msg': msg,

    }
    return data


@article.route("/article/updateArticleSubmit", methods=['GET', 'POST'])
def updateArticleSubmit():  # 修改
    msg = "000000"
    if request.method == 'POST':
        id = request.form.get('id', type=str)
        cid = request.form.get('cid')
        title = request.form.get('title')
        picurl = request.form.get('picurl')
        memo = request.form.get('memo')
        uptime = request.form.get('uptime')

    else:
        id = request.args.get('id', type=str)
        cid = request.args.get('cid', type=str)
        title = request.args.get('title', type=str)
        picurl = request.args.get('picurl', type=str)
        memo = request.args.get('memo', type=str)
        uptime = request.args.get('uptime', type=str)

    try:
        if 1 == 1 and cid != '' and title != '' and picurl != '' and memo != '' and uptime != '':
            dao.SetCid(cid)
            dao.SetTitle(title)
            dao.SetPicurl(picurl)
            dao.SetMemo(memo)
            dao.SetUptime(uptime)

            dao.SetId(id)
            articleDao.edit(dao, " ")
            msg = "666666"
        else:
            msg = "100008"
    except:
        msg = "000000"
    data = {
        'action': 'updateArticleSubmit',
        'msg': msg,

    }
    return data


