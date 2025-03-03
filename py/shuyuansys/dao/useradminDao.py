

from cls.db.mysqlhelp import MySql
from model.useradminModel import useradminModel


# 管理员
class useradminDao(useradminModel):
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
        sql = "insert into  "+self.biao+"  (username,password,name1,tel) values (%s,%s,%s,%s)"
        args = (self.GetUsername(), self.GetPassword(), self.GetName1(), self.GetTel())
        self.db.add(sql, args)

    def addreplace(self):
        sql = "replace into  "+self.biao+"  (username,password,name1,tel) values (%s,%s,%s,%s)"
        args = (self.GetUsername(), self.GetPassword(), self.GetName1(), self.GetTel())
        self.db.add(sql, args)

    def edit(self, wherestr):
        sql = "update "+self.biao+" set  username=%s,password=%s,name1=%s,tel=%s  where id=%s"
        args = (self.GetUsername(), self.GetPassword(), self.GetName1(), self.GetTel(), self.GetId())
        self.db.edit(sql, args)
