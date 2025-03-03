
import re


class useradminModel:
    vbiao ="useradmin"
    biao = "useradmin"
    id = 0  # 编号
    username = ""  # 用户名
    password = ""  # 密码
    name1 = ""  # 姓名
    tel = ""  # 手机

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

    def SetName1(self, name1):
        self.name1 = name1

    def GetName1(self):
        return self.name1

    def SetTel(self, tel):
        self.tel = tel

    def GetTel(self):
        return self.tel




