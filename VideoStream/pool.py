import pymysql as MYSQL
def connectionpooling():
    db=MYSQL.connect(host="localhost",port=3306,user="root",password="AlphaBravo121@",db="videostream")
    cmd=db.cursor()
    return db,cmd
