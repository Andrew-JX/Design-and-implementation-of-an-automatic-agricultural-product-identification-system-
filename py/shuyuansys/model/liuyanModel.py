
import re


class liuyanModel:
    vbiao ="vliuyan"
    biao = "liuyan"
    id = 0  # 编号
    uid = 0  # 用户
    memo = ""  # 内容
    huimemo = ""  # 回复
    uptime = ""  # 时间

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetUid(self, uid):
        self.uid = uid

    def GetUid(self):
        return self.uid

    def SetMemo(self, memo):
        self.memo = memo

    def GetMemo(self):
        return self.memo

    def SetHuimemo(self, huimemo):
        self.huimemo = huimemo

    def GetHuimemo(self):
        return self.huimemo

    def SetUptime(self, uptime):
        self.uptime = uptime

    def GetUptime(self):
        return self.uptime




