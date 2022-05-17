import pymysql
from User import User
class UserDAO:    
    def GetUserNum():
        import pymysql
        conn = pymysql.connect(host='localhost', user='root', password='tjoen', db = 'mydb', charset = 'utf8')
        curs = conn.cursor()
        sql = "SELECT usernum From users"
        curs.execute(sql)
        rows = curs.fetchall()
        if rows == ():
                return 1
        for a in rows:
            list = a
        for a in list:
            print(a)
            usenum = a+1
            return usenum
        curs.close()
        conn.close()
        
    def UserDuplicateinspection(uid):
        conn = pymysql.connect(host='localhost', user='root', password='tjoen', db = 'mydb', charset = 'utf8')
        curs = conn.cursor()
        sql = "SELECT uid From users"
        curs.execute(sql)
        rows = curs.fetchall()
        list = []
        if rows == ():
            return True
        for a in rows:
            for b in a:
                if b == uid:
                    print('중복된 아이디입니다.')
                    return False
        curs.close()
        conn.close()
        return True        
        
    def UserInput(usernum, uid, phone, email):
        conn = pymysql.connect(host='localhost', user='root', password='tjoen', db='mydb', charset='utf8')
        sql = "INSERT INTO users(usernum, uid, phone, email) VALUES (%s,%s,%s,%s)"
        with conn.cursor() as cursor:
            n = cursor.execute(sql, (usernum, uid, phone, email)) 
            if n==1:
                print('사용자 추가 성공')
                conn.commit()
            else: print('사용자 추가 실패')
        conn.close()
        
    def UserList():
        conn = pymysql.connect(host='localhost', user='root', password='tjoen', db = 'mydb', charset = 'utf8')
        curs = conn.cursor()
        sql = "SELECT usernum, uid, phone, email From users"
        curs.execute(sql)
        rows = curs.fetchall()
        for (usernum, uid, phone, email) in rows:
            user1 = User(usernum, uid, phone, email)
            print(user1)
        curs.close()
        conn.close()
        
    def FindUser(uid):
        conn = pymysql.connect(host='localhost', user='root', password='tjoen', db = 'mydb', charset = 'utf8')
        curs = conn.cursor()
        sql = "SELECT usernum, uid, phone, email From users Where uid=%s or usernum=%s"
        curs.execute(sql, (uid, uid))
        rows = curs.fetchall()
        if rows == ():
            print('찾으시는 uid가 존재하지 않습니다')
            return False
        for (usernum, uid, phone, email) in rows:
            user1 = User(usernum, uid, phone, email)
            print(user1)
            return True
        curs.close()
        conn.close()
        
    def EditUser(uid, phone, email):
        conn = pymysql.connect(host='localhost', user='root', password='tjoen',
                       db='mydb', charset='utf8')
        sql = "UPDATE users SET phone=%s, email=%s WHERE uid=%s"
        with conn.cursor() as cursor:
            n = cursor.execute(sql, (phone, email, uid))
            if n==1:
                print('수정 성공')
                conn.commit()
                conn.close()
 
    def DelUser(num):
        conn = pymysql.connect(host='localhost', user='root', password='tjoen',
                       db='mydb', charset='utf8')
        sql = "DELETE FROM users WHERE usernum=%s"
        with conn.cursor() as cursor:
            n = cursor.execute(sql, num)
            if n==1:
                print('삭제 성공')
                conn.commit()
            else: print('없는 사원 번호입니다.')
        conn.close()
        
        