
import re


class userlistModel:
    vbiao ="userlist"
    biao = "userlist"
    id = 0  # 编号
    username = ""  # 用户名
    password = ""  # 密码
    cname = ""  # 姓名
    sex = ""  # 性别
    tel = ""  # 手机
    email = ""  # 邮箱

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetUsername(self, username):
        self.username = username

    def GetUsername(self):
        return self.username

    def SetPassword(self, password):
        self.password = password

    def GetPassword(self):
        return self.password

    def SetCname(self, cname):
        self.cname = cname

    def GetCname(self):
        return self.cname

    def SetSex(self, sex):
        self.sex = sex

    def GetSex(self):
        return self.sex

    def SetTel(self, tel):
        self.tel = tel

    def GetTel(self):
        return self.tel

    def SetEmail(self, email):
        self.email = email

    def GetEmail(self):
        return self.email




