
import re


class articleModel:
    vbiao ="varticle"
    biao = "article"
    id = 0  # 编号
    cid = 0  # 分类
    title = ""  # 标题
    picurl = ""  # 图片
    memo = ""  # 内容
    uptime = ""  # 发布时间

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetCid(self, cid):
        self.cid = cid

    def GetCid(self):
        return self.cid

    def SetTitle(self, title):
        self.title = title

    def GetTitle(self):
        return self.title

    def SetPicurl(self, picurl):
        self.picurl = picurl

    def GetPicurl(self):
        return self.picurl

    def SetMemo(self, memo):
        self.memo = memo

    def GetMemo(self):
        return self.memo

    def SetUptime(self, uptime):
        self.uptime = uptime

    def GetUptime(self):
        return self.uptime




