import MySQLdb
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}
#################################################
while(True):
    print("*********************************")
    print("1. 상품등록 / 2. 상품검색")
    menu=int(input("무엇을 하시겠습니까?"))
    
    if menu == 1:
        data=[]
        data.append(str(input("상품명을 입력하세요:")))
        data.append(int(input("수량을 입력하세요:")))
        data.append(int(input("단가를 입력하세요:")))

        print(data)
        isUpdate=str(input("상품을 등록하시겠습니까? (Y/N)"))
        if isUpdate == "Y" or isUpdate == "y":
            try:
                conn = MySQLdb.connect(**config)
                cursor = conn.cursor()
                    
                #max(c0de) 가져오기
                sql = "select 'max(code)' from sangdata"
                code = int(cursor.execute(sql))+1
                    
                #insert
                sql = "insert into sangdata values(%s, %s, %s, %s)"
                sql_data = code, data[0], data[1], data[2]
                cursor.execute(sql, sql_data)
                conn.commit()
                    
                #select
                sql = "select * from sangdata"
                sql2 = "select count(code) from sangdata"
                cursor.execute(sql)

                for (code, sang, su, dan) in cursor:    
                    print(code, sang, su, dan)
                count=cursor.execute(sql2)
                print("건 수: ", count)
                
                        
            except Exception as e:
                print("err: "+str(e))
                conn.rollback()
                
            finally:    
                cursor.close()
                conn.close()
                    
        else: 
            print("프로그램을 종료합니다.")
            break

    elif menu == 2:
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            #select
            sql = "select * from sangdata"
            sql2 = "select 'count(code)' from sangdata"
            cursor.execute(sql)

            for (code, sang, su, dan) in cursor:    
                print(code, sang, su, dan)
            count=cursor.execute(sql2)
            print("건 수: ", count)
            
        except Exception as e:
            print("err: "+str(e))
            conn.rollback()
                
        finally:    
            cursor.close()
            conn.close()    
    
    else: 
        print("1. 상품등록 / 2. 상품검색 중 선택하세요.")
        continue
    


    