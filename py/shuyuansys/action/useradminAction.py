
from dao.useradminDao import useradminDao
from flask import Blueprint, request, session

useradmin = Blueprint('useradmin', __name__)
dao = useradminDao()


@useradmin.route("/useradmin/queryUseradminAll", methods=['GET', 'POST'])
def queryUseradminAll():
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
    totalCount = useradminDao.count(dao, sql)  # 总条数
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
    datalist = useradminDao.find(dao, sql + " order by id desc " + limitstr)
    data = {
        'action': 'queryUseradminAll',
        'msg': '666666',
        'enlist': list(datalist),
        "entity": {"sumpage": totalPage, "count": totalCount, "page": pageIndex},
    }
    return data


@useradmin.route("/useradmin/queryUseradminById", methods=['GET', 'POST'])
def queryUseradminById():
    if request.method == 'POST':
        id = request.form.get('id', type=str)
    else:
        id = request.args.get('id', type=str)

    datalist = useradminDao.find(dao, " and id=" + id)
    print(datalist)
    if len(datalist) > 0:
        data = {
            'action': 'queryUseradminById',
            'msg': '666666',
            'enlist': list(datalist),
            "entity": {"sumpage": 1, "count": 1, "page": 1},
        }
    else:
        data = {
            'action': 'queryUseradminById',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }

    # 返回结果
    return data


@useradmin.route("/useradmin/deleteUseradminByIds", methods=['GET', 'POST'])
def deleteUseradminByIds():
    if request.method == 'POST':
        id = request.form.get('ids', type=str)
    else:
        id = request.args.get('ids', type=str)
    d = useradminDao.delete(dao, " and id in (" + id + ")")
    data = {
            'action': 'deleteUseradminByIds',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }

    # 返回结果
    return data


@useradmin.route("/useradmin/topUseradminNumList", methods=['GET', 'POST'])
def topUseradminNumList():  # 按top
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
    totalCount = useradminDao.count(dao, sql)  # 总条数
    datalist = useradminDao.find(dao, sql)
    if len(datalist) > 0:
        data = {
            'action': 'topUseradminNumList',
            'msg': '666666',
            'enlist': list(datalist),
            "entity": {"sumpage": 1, "count": totalCount , "page": 1},
        }
    else:
        data = {
            'action': 'topUseradminNumList',
            'msg': '000000',
            'enlist': "",
            "entity": {"sumpage": 0, "count": 0, "page": 0},
        }
    return data


@useradmin.route("/useradmin/addUseradminSubmit", methods=['GET', 'POST'])
def addUseradminSubmit():  # 添加
    msg = "000000"
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        name1 = request.form.get('name1')
        tel = request.form.get('tel')

    else:
        username = request.args.get('username', type=str)
        password = request.args.get('password', type=str)
        name1 = request.args.get('name1', type=str)
        tel = request.args.get('tel', type=str)

    try:
        if 1 == 1 and username != '' and password != '' and name1 != '' and tel != '':
            dao.SetUsername(username)
            dao.SetPassword(password)
            dao.SetName1(name1)
            dao.SetTel(tel)

            useradminDao.add(dao)
            msg = "666666"
        else:
            msg = "100008"
    except:
        msg = "000000"
    data = {
        'action': 'addUseradminSubmit',
        'msg': msg,

    }
    return data


@useradmin.route("/useradmin/updateUseradminSubmit", methods=['GET', 'POST'])
def updateUseradminSubmit():  # 修改
    msg = "000000"
    if request.method == 'POST':
        id = request.form.get('id', type=str)
        username = request.form.get('username')
        password = request.form.get('password')
        name1 = request.form.get('name1')
        tel = request.form.get('tel')

    else:
        id = request.args.get('id', type=str)
        username = request.args.get('username', type=str)
        password = request.args.get('password', type=str)
        name1 = request.args.get('name1', type=str)
        tel = request.args.get('tel', type=str)

    try:
        if 1 == 1 and username != '' and password != '' and name1 != '' and tel != '':
            dao.SetUsername(username)
            dao.SetPassword(password)
            dao.SetName1(name1)
            dao.SetTel(tel)

            dao.SetId(id)
            useradminDao.edit(dao, " ")
            msg = "666666"
        else:
            msg = "100008"
    except:
        msg = "000000"
    data = {
        'action': 'updateUseradminSubmit',
        'msg': msg,

    }
    return data


@useradmin.route("/useradmin/UseradminLogin", methods=['GET', 'POST'])
def UseradminLogin():  # 登录
    data = {
        'action': 'UseradminLogin',
        'msg':"000000",
    }
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.args.get('username', type=str)
        password = request.args.get('password', type=str)
    if 1 == 1 and username != '' and password != '':
        whstr = " and username='" + username + "' and password='" + password + "'"
        datalist = useradminDao.find(dao, whstr)
        if len(datalist) > 0:
            session['useradminLogin'] = datalist[0]
            msg = '666666'
            data = {
                'action': 'useradminGetLogin',
                'msg': msg,
                'enlist': list(datalist),
                'entity': {"sumpage": 1, "count": 1, "page": 1},
            }
    return data


@useradmin.route("/useradmin/UseradminGetLogin", methods=['GET', 'POST'])
def UseradminGetLogin():  # 是否登录
    if request.method == 'POST':
        user = "0"
        msg = "000001"
        data = {
            'action': 'useradminGetLogin',
            'msg': "000000",
        }
        try:
            user = session['useradminLogin']
            if user != "":
                msg = "666666"  # 有登录
        except:
            user = "0"
        if user == "0":
            msg = '000001'  # 没有登录
            data = {
                'action': 'useradminGetLogin',
                'msg': msg,
            }
        else:
            data = {
                'action': 'useradminGetLogin',
                'msg': msg,
                'enlist': user,
                'entity': {"sumpage": 1, "count": 1, "page": 1},
            }
    return data


@useradmin.route("/useradmin/UseradminLogout", methods=['GET', 'POST'])
def UseradminLogout():  # 退出时删除session
    session['useradminLogin'] = ""  # 删除session
    data = {
        'action': 'UseradminLogout',
        'msg': '666666',
    }
    return data


@useradmin.route("/useradmin/UseradminChagePass", methods=['GET', 'POST'])
def UseradminChagePass():  # 修改密码
    msg = '000000'
    username = session['useradminLogin']["username"]
    if request.method == 'POST':
        password = request.form.get('password')
        oldpassword = request.form.get('oldpassword')
    else:
        password = request.args.get('password', type=str)
        oldpassword = request.args.get('oldpassword', type=str)
    if 1 == 1 and username != '' and password != '' and oldpassword != '':
        whstr = " and username='" + username + "' and password='" + oldpassword + "'"
        datalist = useradminDao.find(dao, whstr)
        if len(datalist) > 0:
            dao.SetUsername(datalist[0]['username'])
            dao.SetPassword(datalist[0]['password'])
            dao.SetName1(datalist[0]['name1'])
            dao.SetTel(datalist[0]['tel'])
            dao.SetId(datalist[0]['id'])
            dao.SetPassword(password)
            useradminDao.edit(dao, " ")
            msg = '666666'
        else:
            msg = '000003'  # 旧密码输入错误
    data = {
        'action': 'UseradminChagePass',
        'msg': msg,
    }
    return data


@useradmin.route("/useradmin/UseradminRegister", methods=['GET', 'POST'])
def UseradminRegister():  # 注册
    msg = "000000"
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        name1 = request.form.get('name1')
        tel = request.form.get('tel')
    else:
        username = request.args.get('username', type=str)
        password = request.args.get('password', type=str)
        name1 = request.args.get('name1', type=str)
        tel = request.args.get('tel', type=str)
    try:
        datalist = useradminDao.find(dao, " and username='" + username + "'")
        if len(datalist) <= 0:
            if 1 == 1 and username != '' and password != '' and name1 != '' and tel != '':
                dao.SetUsername(username)
                dao.SetPassword(password)
                dao.SetName1(name1)
                dao.SetTel(tel)
                useradminDao.add(dao)
                msg = "666666"
            else:
                msg = "100008"  # 输入不能为空
        else:
            msg = "000005"  # 账号已成在
    except:
        msg = "000000"
    data = {
        'action': 'UseradminRegister',
        'msg': msg,
    }
    return data



