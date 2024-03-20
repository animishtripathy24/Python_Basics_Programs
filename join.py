import pandas as pd
d={'roll no':[1,2,3,4,5],'marks':[90,91,92,93,94]}
i=[1,3,5,7,9]
df=pd.DataFrame(data=d,index=i)
print(df)
f={'name':['ram','shyam','mohan','sohan','anand'],'class':[10,11,12,12,11],'subject':['physics','chemistry','maths','ip','english']}
g=[2,3,5,8,10]
df1=pd.DataFrame(data=f,index=g)
print(df1)
df2=df.join(df1,how='outer').fillna(0)
print(df2)


   
