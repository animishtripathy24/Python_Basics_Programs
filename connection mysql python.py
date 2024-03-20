import mysql.connector as sqlc
import pandas as pd
c=sqlc.connect(host="localhost",user="root",passwd="2003",database="emp")
df=pd.read_sql("select * from emp;",c)
print(df)
