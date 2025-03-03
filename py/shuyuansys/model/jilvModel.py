
import re


class jilvModel:
    vbiao ="vjilv"
    biao = "jilv"
    id = 0  # 编号
    title = ""  # 标题
    uptime = ""  # 检测时间
    uid = 0  # 用户
    jie = ""  # 结果
    picurl = ""  # 图片

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetTitle(self, title):
        self.title = title

    def GetTitle(self):
        return self.title

    def SetUptime(self, uptime):
        self.uptime = uptime

    def GetUptime(self):
        return self.uptime

    def SetUid(self, uid):
        self.uid = uid

    def GetUid(self):
        return self.uid

    def SetJie(self, jie):
        self.jie = jie

    def GetJie(self):
        return self.jie

    def SetPicurl(self, picurl):
        self.picurl = picurl

    def GetPicurl(self):
        return self.picurl




