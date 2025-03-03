

from cls.db.mysqlhelp import MySql
from model.articleModel import articleModel


# 文章
class articleDao(articleModel):
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
        sql = "insert into  "+self.biao+"  (cid,title,picurl,memo,uptime) values (%s,%s,%s,%s,%s)"
        args = (self.GetCid(), self.GetTitle(), self.GetPicurl(), self.GetMemo(), self.GetUptime())
        self.db.add(sql, args)

    def addreplace(self):
        sql = "replace into  "+self.biao+"  (cid,title,picurl,memo,uptime) values (%s,%s,%s,%s,%s)"
        args = (self.GetCid(), self.GetTitle(), self.GetPicurl(), self.GetMemo(), self.GetUptime())
        self.db.add(sql, args)

    def edit(self, wherestr):
        sql = "update "+self.biao+" set  cid=%s,title=%s,picurl=%s,memo=%s,uptime=%s  where id=%s"
        args = (self.GetCid(), self.GetTitle(), self.GetPicurl(), self.GetMemo(), self.GetUptime(), self.GetId())
        self.db.edit(sql, args)
