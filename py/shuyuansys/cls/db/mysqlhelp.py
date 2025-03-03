
import pymysql

from model.Config import Config


class MySql:
    config = Config()

    # return: 连接，游标
    def get_conn(self):
        # 创建连接
        conn = pymysql.connect(host=self.config.host,
                               port=int(self.config.port),
                               user=self.config.user,
                               password=self.config.password,
                               db=self.config.db,
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor
                               )
        # 创建游标
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        return conn, cursor

    def close_conn(self, conn, cursor):
        cursor.close()
        conn.close()

    def query(self, sql):
        """
        封装通用查询
        :param sql:
        :param args:
        :return: 返回查询到的结果，((),(),)的形式
        """
        conn, cursor = self.get_conn()
        cursor.execute(sql)
        res = cursor.fetchall()
        self.close_conn(conn, cursor)
        # print(res)
        return res

    def add(self, sql, args):
        """
        添加数据
        :param sql:
        :param args:
        :return: 返回查询到的结果，((),(),)的形式
        """

        connarr = self.get_conn()
        cursor = connarr[1]
        cursor.execute(sql, args)
        connarr[0].commit()
        # self.close_conn(connarr, cursor)
        return 1

    def edit(self, sql, args):
        """
        修改数据
        :param sql:
        :param args:
        :return: 返回查询到的结果，((),(),)的形式
        """
        connarr = self.get_conn()
        cursor = connarr[1]
        cursor.execute(sql, args)
        connarr[0].commit()
        return 1

    def replaceedit(self, sql,args):
        """
        替换数据
        :param sql:
        :param args:
        :return: 返回查询到的结果，((),(),)的形式
        """
        connarr = self.get_conn()
        cursor = connarr[1]
        cursor.execute(sql, args)
        connarr[0].commit()
        return 1

    def delete(self, sql):
        """
        删除数据
        :param sql:
        :param args:
        :return: 返回查询到的结果，((),(),)的形式
        """
        conn, cursor = self.get_conn()
        cursor.execute(sql)
        conn.commit()
        self.close_conn(conn, cursor)
        return 1

    def exsql(self, sql):
        """
        执行SqL
        :param sql:
        :param args:
        :return: 返回查询到的结果，((),(),)的形式
        """
        conn, cursor = self.get_conn()
        cursor.execute(sql)
        conn.commit()
        self.close_conn(conn, cursor)
        return 1 
