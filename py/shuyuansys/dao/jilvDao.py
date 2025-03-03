

from cls.db.mysqlhelp import MySql
from model.jilvModel import jilvModel


# 检测记录
class jilvDao(jilvModel):
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
        sql = "insert into  "+self.biao+"  (title,uptime,uid,jie,picurl) values (%s,%s,%s,%s,%s)"
        args = (self.GetTitle(), self.GetUptime(), self.GetUid(), self.GetJie(), self.GetPicurl())
        self.db.add(sql, args)

    def addreplace(self):
        sql = "replace into  "+self.biao+"  (title,uptime,uid,jie,picurl) values (%s,%s,%s,%s,%s)"
        args = (self.GetTitle(), self.GetUptime(), self.GetUid(), self.GetJie(), self.GetPicurl())
        self.db.add(sql, args)

    def edit(self, wherestr):
        sql = "update "+self.biao+" set  title=%s,uptime=%s,uid=%s,jie=%s,picurl=%s  where id=%s"
        args = (self.GetTitle(), self.GetUptime(), self.GetUid(), self.GetJie(), self.GetPicurl(), self.GetId())
        self.db.edit(sql, args)
