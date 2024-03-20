import pandas as pd
import mysql.connector as sqlc
c=sqlc.connect(host='local host',user='root',passwd='2020',database='smhs')
dff=pd.read_sql('select * from result',c)
print(dff)
c.close()
