# coding:utf-8
import pymysql
from shadon.testsConfig import testsConfig


class MyDB():

    db = 'null'  # 类变量，所有案例都可以进行访问
    cursor = 'null'  # 类变量，所有案例都可以进行访问

    def conn_db(self):
        #连接数据库
        try:
            r = testsConfig()
            port = r.getFile("DATABASE", "port")
            port = int(port) #类型转换
            #连接数据库
            MyDB.db = pymysql.connect(host=r.getFile("DATABASE","host"),
                                      port=port,
                                      user=r.getFile("DATABASE","username"),
                                      password=r.getFile("DATABASE","password"),
                                      charset=r.getFile("DATABASE","charset"),
                                      db=r.getFile("DATABASE","db"))
            # 创建游标
            MyDB.cursor = MyDB.db.cursor()
        except ConnectionError:
            print("connect error")

    def select_one_record(self,sql):
        #查询返回一条数据
        try:
            #执行SQL语句
            MyDB.cursor.execute(sql)
            #sql='select * FROM el_user.user_address'
            self.result = MyDB.cursor.fetchone()
          #  print(self.result)
        except:
            print("error")
        return self.result
    def select_multiterm_record(self,sql,number):
        #查询返回多条数据
        try:
            # 执行SQL语句
            MyDB.cursor.execute(sql)
            self.result = MyDB.cursor.fetchmany(number)
        except:
            print("error")
        return self.result
    def select_all_record(self,sql):
        #查询返回所有数据
        try:
            # 执行SQL语句
            MyDB.cursor.execute(sql)
            self.result = MyDB.cursor.fetchall()
        except:
            print("error")
        return self.result
    def execute_insert(self, sql):
        #插入数据
        try:
            # 执行SQL语句
            MyDB.cursor.execute(sql)
            #sql="""INSERT INTO el_user.user_entrance(ue_id,user_id,type,entrance,created_time,update_time)VALUES('11','148086','1','快速入口','13563023312','2017-11-25 15:51:38')"""
            # 提交到数据库执行
            MyDB.db.commit()
            return True
        except:
            # 发生错误时回滚
            MyDB.db.rollback()

    def execute_update(self, sql):
        # 更新数据
        try:
            # 执行SQL语句
            MyDB.cursor.execute(sql)
            #sql="UPDATE el_user.user_entrance SET ue_id = '20' WHERE ue_id = 11"
            # 提交到数据库执行
            MyDB.db.commit()
            return True
        except:
            # 发生错误时回滚
            MyDB.db.rollback()
    def execute_delete(self, sql):
        # 删除数据
        try:
            # 执行SQL语句
            MyDB.cursor.execute(sql)
            #sql="DELETE FROM el_user.user_entrance WHERE ue_id = 20"
            # 提交到数据库执行
            MyDB.db.commit()
            return True
        except:
            # 发生错误时回滚
            MyDB.db.rollback()
    def close(self):
        # 关闭数据库连接
        MyDB.db.close()


#r = MyDB()
#r.conn_db()
#r.select_one_record('select * FROM el_user.user_address')
#r.execute_insert("""INSERT INTO el_user.user_entrance(ue_id,user_id,type,entrance,created_time,update_time)VALUES('11','148086','1','快速入口','13563023312','2017-11-25 15:51:38')""")
#r.execute_update("UPDATE el_user.user_entrance SET ue_id = '20' WHERE ue_id = 11")
#r.execute_delete("DELETE FROM el_user.user_entrance WHERE ue_id = 20" )
#r.close()