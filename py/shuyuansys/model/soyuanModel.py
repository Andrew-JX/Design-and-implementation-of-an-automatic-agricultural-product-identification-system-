
import re


class soyuanModel:
    vbiao ="soyuan"
    biao = "soyuan"
    id = 0  # 编号
    nong = ""  # 农产品
    picurl = ""  # 产品图片
    bo = ""  # 播种
    chetime = ""  # 上市时间
    shi = ""  # 施肥
    sheng = ""  # 生长
    shou = ""  # 收购
    yun = ""  # 运输
    er = ""  # 码
    uptime = ""  # 上传时间
    bh = ""  # 序号
    img1 = ""  # 图片1
    img2 = ""  # 图片2
    img3 = ""  # 图片3

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetNong(self, nong):
        self.nong = nong

    def GetNong(self):
        return self.nong

    def SetPicurl(self, picurl):
        self.picurl = picurl

    def GetPicurl(self):
        return self.picurl

    def SetBo(self, bo):
        self.bo = bo

    def GetBo(self):
        return self.bo

    def SetChetime(self, chetime):
        self.chetime = chetime

    def GetChetime(self):
        return self.chetime

    def SetShi(self, shi):
        self.shi = shi

    def GetShi(self):
        return self.shi

    def SetSheng(self, sheng):
        self.sheng = sheng

    def GetSheng(self):
        return self.sheng

    def SetShou(self, shou):
        self.shou = shou

    def GetShou(self):
        return self.shou

    def SetYun(self, yun):
        self.yun = yun

    def GetYun(self):
        return self.yun

    def SetEr(self, er):
        self.er = er

    def GetEr(self):
        return self.er

    def SetUptime(self, uptime):
        self.uptime = uptime

    def GetUptime(self):
        return self.uptime

    def SetBh(self, bh):
        self.bh = bh

    def GetBh(self):
        return self.bh

    def SetImg1(self, img1):
        self.img1 = img1

    def GetImg1(self):
        return self.img1

    def SetImg2(self, img2):
        self.img2 = img2

    def GetImg2(self):
        return self.img2

    def SetImg3(self, img3):
        self.img3 = img3

    def GetImg3(self):
        return self.img3




