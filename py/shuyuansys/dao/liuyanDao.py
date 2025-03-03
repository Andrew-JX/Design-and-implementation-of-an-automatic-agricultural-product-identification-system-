

from cls.db.mysqlhelp import MySql
from model.liuyanModel import liuyanModel


# 留言
class liuyanDao(liuyanModel):
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
        sql = "insert into  "+self.biao+"  (uid,memo,huimemo,uptime) values (%s,%s,%s,%s)"
        args = (self.GetUid(), self.GetMemo(), self.GetHuimemo(), self.GetUptime())
        self.db.add(sql, args)

    def addreplace(self):
        sql = "replace into  "+self.biao+"  (uid,memo,huimemo,uptime) values (%s,%s,%s,%s)"
        args = (self.GetUid(), self.GetMemo(), self.GetHuimemo(), self.GetUptime())
        self.db.add(sql, args)

    def edit(self, wherestr):
        sql = "update "+self.biao+" set  uid=%s,memo=%s,huimemo=%s,uptime=%s  where id=%s"
        args = (self.GetUid(), self.GetMemo(), self.GetHuimemo(), self.GetUptime(), self.GetId())
        self.db.edit(sql, args)
