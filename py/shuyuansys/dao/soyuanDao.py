

from cls.db.mysqlhelp import MySql
from model.soyuanModel import soyuanModel


# 溯源信息
class soyuanDao(soyuanModel):
    db = MySql()

    def count(self, wherestr):
        res = self.db.query("select count(*) as c from  " + self.vbiao + " where 1=1 " + wherestr)
        c = res[0]['c']
        return c

    def find(self, wherestr):
        res = self.db.query("select * from " + self.vbiao + " where 1=1 " + wherestr)
        return res

    def delete(self, wherestr):
        sql = "delete  from " + self.biao + " where 1=1 " + wherestr
        self.db.delete(sql)
        return 1

    def add(self):
        sql = "insert into  "+self.biao+"  (nong,picurl,bo,chetime,shi,sheng,shou,yun,er,uptime,bh,img1,img2,img3) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (self.GetNong(), self.GetPicurl(), self.GetBo(), self.GetChetime(), self.GetShi(), self.GetSheng(), self.GetShou(), self.GetYun(), self.GetEr(), self.GetUptime(), self.GetBh(), self.GetImg1(), self.GetImg2(), self.GetImg3())
        self.db.add(sql, args)

    def addreplace(self):
        sql = "replace into  "+self.biao+"  (nong,picurl,bo,chetime,shi,sheng,shou,yun,er,uptime,bh,img1,img2,img3) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (self.GetNong(), self.GetPicurl(), self.GetBo(), self.GetChetime(), self.GetShi(), self.GetSheng(), self.GetShou(), self.GetYun(), self.GetEr(), self.GetUptime(), self.GetBh(), self.GetImg1(), self.GetImg2(), self.GetImg3())
        self.db.add(sql, args)

    def edit(self, wherestr):
        sql = "update "+self.biao+" set  nong=%s,picurl=%s,bo=%s,chetime=%s,shi=%s,sheng=%s,shou=%s,yun=%s,er=%s,uptime=%s,bh=%s,img1=%s,img2=%s,img3=%s  where id=%s"
        args = (self.GetNong(), self.GetPicurl(), self.GetBo(), self.GetChetime(), self.GetShi(), self.GetSheng(), self.GetShou(), self.GetYun(), self.GetEr(), self.GetUptime(), self.GetBh(), self.GetImg1(), self.GetImg2(), self.GetImg3(), self.GetId())
        self.db.edit(sql, args)
