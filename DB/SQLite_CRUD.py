import sqlite3

def dbFunc(dbName):
    try:
        conn = sqlite3.connect(dbName)
        c = conn.cursor()
        c.execute("drop table if exists jikwons")
        c.execute("create table if not exists jikwons(id integer primary key, name text)")
        
        #insert
        c.execute("insert into jikwons values(1, '가나다')")
        
        t_data = (2, "신기해") #tuple data
        c.execute("insert into jikwons values(?,?)", t_data)
        t_data2 = 3, "신선해" #tuple data : 괄호 없이 줘도 튜플이다.
        c.execute("insert into jikwons values(?,?)", t_data2)
        t_data3 = ((4, "신기루"), (5, "신라면"))
        c.executemany("insert into jikwons values(?,?)", t_data3)
        
        l_data = [6, "공기밥"] #list data
        c.execute("insert into jikwons values(?,?)", l_data)
        
        d_data = {"id": 7, "name":"고래밥"} #dict data : key에 의한 매핑
        c.execute("insert into jikwons values(:id, :name)", d_data)
        d_data2 = {"sabun": 8, "irum":"주먹밥"} #dict data
        c.execute("insert into jikwons values(:sabun, :irum)", d_data2)
        
        #updata
        up_data = ("박치기", 7) # ["박치기", 7] -> 이렇게도 가능하다.
        c.execute("update jikwons set name=? where id=?", up_data)
        
        #delete
        del_data = (4,) #(4) -> 4 와 같다. 
        c.execute("delete from jikwons where id=?", del_data)
        
        conn.commit()
        
        #select
        print("출력1")
        c.execute("select * from jikwons")
        for r in c:
            print(str(r[0])+" "+r[1])
            
        print("출력2 : 부분자료")    
        #c.execute("select * from jikwons where id <= 2")
        c.execute("select * from jikwons where name= '%s' " %'신기해')
        for r in c.fetchall():
            print(str(r[0])+" "+r[1])
            
        print("출력3 : 함수 사용") 
        c.execute("select count(*)  from jikwons")        
        print("건 수: "+str(c.fetchone()[0]))
    
    except Exception as e:
        print("err: "+str(e))
        conn.rollback()
    finally:
        conn.close()  
        
if __name__ == '__main__':
        dbFunc("test.db")         
        