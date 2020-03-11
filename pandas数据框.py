# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:48:36 2020

@author: Administrator
"""

import pandas as pd
import numpy as np
#创建数据框
pd.DataFrame([[1,2,3],[10,20,30],[100,200,300],[1,10,100]],columns=['V1','V2','V3'])
''' 
    V1   V2   V3
0    1    2    3
1   10   20   30
2  100  200  300
3    1   10  100
'''
#通过列表创建数据框
pd.DataFrame({'id':[1,2,3],'name':['Tom','Lily','Jim'],'age':[28,27,29]})
'''
    id  name  age
0   1   Tom   28
1   2  Lily   27
2   3   Jim   29'''

#数据读入
books=pd.read_table('books.txt',sep=',',header=None,usecols=[0,1,2],name=['book_type','title','ahthor'])
'''
read_table和read_csv两个函数都可以读文本文件数据，区别在于默认的sep参数不一
致，read_table默认以制表符Tab键为字段间的间隔符，而read_csv默认以逗号为字段间的
间隔符。'''
co2=pd.read_csv('co2.csv',sep=',')

#读取电子表格
iris=pd.read_excel('iris.xlsx')

#数据信息概览
co2.shape
co2.columns
#数值型变量的概览信息
co2.describe(include=['number'])
#离散型变量的概览信息
co2.describe(include=['object'])
#info属性则对数据集的变量类型进行简单的描述
co2.info()

#数据筛选
#名称索引法
iris['Species'].head()
#点取法
iris.Species.head()
'''如果使用点取法取出数据集中的某列，需要注意的是列的名称必须是一个整体，例如stu
age或stu.age等格式的变量名就不能使用点取法。'''
#取多列数据
#取出'setosa'花种
iris.loc[iris.Species=='setosa',:].head()#一个变量
#取出'setosa'花种'且sepal.length大于5的数据
iris.loc[(iris.Species=='setosa')&(iris['Sepal.length']>5),:]#两个变量
'''需要注意的是：多个变量的筛选，可以是或(|)关系、可以是且(&)关系还可以是非(~)关系，
一定要用圆括号把条件括起来'''

#变量删除
iris.drop(['Sepal.Length','Species'],axis=1)
'''需要注意的是，该函数默认的axis=0，表示删除行观测，如果需要删除列，就要将asix设
置为1。记住，此时虽然删除了两个变量，但iris数据集本身是没有变化的，如果你需要改变
iris数据集，需要设置inplace为True'''

#修改变量名称
iris.rename(columns={'Sepal.Length':'Sepal_Length','Sepal.Width':'Sepal_Width'},inplace=True)

#数据类型转化
#字符型转数值型
data=pd.DataFrame({'id':range(4),'age':['13','18','11','18'],'outcome':['15.3','10.8','13.7','11.4']})
data=data.astype({'outcome':'float','age':'int'})#通过astype函数实现

#数据集排序
iris.sort_values(by=['Sepal.Length','Sepal.Width'],ascending=[True,False])#可以随意按照某些变量升序或降序排列

#数据去重
data=pd.DataFrame({'name':['Lin','Li','Chen','Liu'],'age':[28,31,27,28],'gender':['M','M','M','M']})
data.drop_duplicates()#通过drop_duplicates函数对数据集的重复观测进行删除
data.drop_duplicates(subset='gender')

#频数统计
income=pd.read_excel('income.xlsx')
income.gender.value_counts()#统计性别人数
income.gender.value_counts()/sum(income.gender.value_counts())
#查看男女百分比

#缺失值处理
#构建数据集
df=pd.DataFrame([[1,2,3,4],[np.NaN,6,7,np.NaN],[11,np.NaN,6,7,np.NaN],[11,np.NaN,12,13],[100,200,300,400],[20,40,60,np.NaN]],columns=['x1','x2','x3','x4'])
#使用isnull检查数据集缺失情况
print(any(df.isnull()))
#每一列是否有缺失和缺失比例
is_null=[]
null_ratio=[]
for col in df.columns:
    is_null.append(any(pd.isnull(df[col])))
    null_ratio.append(float(round(sum(pd.isnull(df.isnull(df[col]))/df.shape[0],2))))
print(is_null,'\n',null_ratio,'\n')
#每一行是否有缺失
is_null=[]
for index in list(df.index):
    is_null.append(any(pd.isnull(df.iloc[index,:])))
print(is_null)

#缺失值处理
#删除法
df.dropna()#删除任何含缺失的数据
df.dropna(how='all')#删除所有都缺失的数据
#替补法
df.fillna(method='ffill')#前向
df.fillna(method='bfill')#后向
df.fillna(value={'x1':df.x1.mean(),'x2':df.x2.median(),'x3':df.x4.max()})
#不同的列用不同的函数

#数据映射
print(any(df.isnull()))#总览是否存在缺失
is_null=[]
null_ratio=[]
for index in list(df.index):
    is_null.append(any(pd.isnull(df.iloc[index,:])))
print(is_null)
#每一行是否有缺失
is_null=[]
for index in list(df.index):
    is_null.append(any(pd.isnull(df.iloc[index,:])))
    null_ratio.append(float(round(sum(pd.isnull(df.isnull(df[col]))/df.shape[0],2))))
print(is_null)
isnull=lambda x:any(pd.isnull(x))
df.apply(func=isnull,axis=0)
df.apply(func=isnull,axis=1)

#数据汇总
groupby_gender=income.groupby(['gender'])#根据性能作分组统计
groupby_gender.aggregate(np.mean)
#对性别和收入水平作分组统计
grouped=income.groupby(['gender','income level'])
grouped.aggregate(np.mean)
#对性别和收入水平作分组统计,但不同变量作不同聚合
grouped=income.groupby(['gender','income level'])
grouped.aggregate({'age':np.mean,'edu time':np.median})#年龄算平均值，教育时常算中位数

#离散变量的哑变量处理
user_level=pd.read_csv('user_level.csv')
pd.get_dummies(user_level,columns=['gender','level'])#使用哑变量
'''如果变量进行了哑变量处理，建模时要记得删除原离散变量
中的某一个水平，如性别中删除gender_F，等级中删除level_V1。删除的变量，就表示性
别中，以女性(F)为参照组；等级中，以V1为参照组'''
user_level.drop(['gender_F','level_V1'],axis=1)

#连续变量的分段
#生成数据
age=np.random.randint(low=12,high=80,size=1000)
age=pd.Series(age)
age.describe()
#数据切割
age_cut=pd.cut(age,bins=[0,18,45,60,80],right=False,labels=['未成年','青年','中年','老年'])
'''假如18岁以下为未成年；18~45岁为青年；45~60岁为中年；60岁以上为老年，接下来就
根据这些阈值把年龄分为4段'''
