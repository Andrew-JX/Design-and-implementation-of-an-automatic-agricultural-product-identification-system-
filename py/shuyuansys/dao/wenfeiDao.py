

from cls.db.mysqlhelp import MySql
from model.wenfeiModel import wenfeiModel


# 文章分类
class wenfeiDao(wenfeiModel):
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
        sql = "insert into  "+self.biao+"  (fenleiname) values (%s)"
        args = (self.GetFenleiname())
        self.db.add(sql, args)

    def addreplace(self):
        sql = "replace into  "+self.biao+"  (fenleiname) values (%s)"
        args = (self.GetFenleiname())
        self.db.add(sql, args)

    def edit(self, wherestr):
        sql = "update "+self.biao+" set  fenleiname=%s  where id=%s"
        args = (self.GetFenleiname(), self.GetId())
        self.db.edit(sql, args)
