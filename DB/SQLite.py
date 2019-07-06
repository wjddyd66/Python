# 개인용 DBMS - SQLite3

import sqlite3
print(sqlite3.sqlite_version)

print()
conn = sqlite3.connect("example.db") #파일로 생성된다.
#conn = sqlite3.connect(":memory:") #휘발성으로 생성된다.

try:
    cur = conn.cursor() #sql문 처리를 위한 객체를 생성
    cur.execute("create table if not exists friend(name text, phone text, addr text)")
    cur.execute("insert into friend values('한국인', '111-1111', '역삼동')")
    cur.execute("insert into friend values('고길동', '222-2222', '강남역 11번출구 앞')")
    cur.execute("insert into friend values(?,?,?)", ('나길동', '333-3333', '강남역 10번출구 계단'))
    mydata = ('심길동', '444-4444', '강남대로 한복판')
    cur.execute("insert into friend values(?,?,?)", mydata)
    conn.commit()
    
    #select 
    cur.execute("select * from friend")
    print(cur.fetchone()) #한 개의 레코드 읽기
    print(cur.fetchone())
    print(cur.fetchone())
    print(cur.fetchone())
    print(cur.fetchone())
    print(cur.fetchone())
    print(cur.fetchone())
    
    print(cur.fetchall()) #전체 레코드 읽기
    
    cur.execute("select name, addr, phone from friend order by name asc")
    for r in cur:
        #print(r)
        print(r[0]+"님의 주소는 "+r[1]+", 전화는 "+r[2])
    
except Exception as e:
    print("err: "+str(e))
    conn.rollback()
finally:
    conn.close()    
        