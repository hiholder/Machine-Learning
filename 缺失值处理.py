# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:58:02 2020

@author: Administrator
"""

import pandas as pd
import numpy as np
data=pd.read_excel("D:Desktopdatasdata.xlsx")
#判断各变量中是否有缺失值
data.isnull().any(axis=0)
data.isnull().sum(axis=0)/data.shape[0]
'''判断数据是否为缺失值NaN，可以使用isnull“方法”，它会返回与原数据
行列数相同的矩阵，并且矩阵的元素为bool类型的值，为了得到每一列的判断结果，仍然
需要any“方法”（且设置“方法”内的axis参数为0）；统计各变量的缺失值个数可以在
isnull的基础上使用sum“方法”（同样需要设置axis参数为0）；计算缺失比例就是在缺失
数量的基础上除以总的样本量（shape方法返回数据集的行数和列数，[0]表示取出对应的
数据行数）。'''
#判断数据行是否有缺失
data.isnull().any(axis=1).any()
'''代码中使用了两次
any“方法”，第一次用于判断每一行对应的True（即行内有缺失值）或False值（即行内
没有缺失值）；第二次则用于综合判断所有数据行中是否包含缺失值。'''
#缺失观测的行数
data.isnull().any(axis = 1).sum()
#缺失观测的比例
data.isnull().any(axis = 1).sum()/data3.shape[0]

#缺失值的处理方式
data.fillna(value={'gender'=data['gender'].mode()[0],# 使用性别的众数替换缺失性别
                   'age':data['age'].mean()# 使用年龄的平均值替换缺失年龄
                   },
                   inplace = True )# 原地修改数据
# 再次查看各变量的缺失比例
data.isnull().sum(axis = 0)
#差补法填补缺失值
titanic=pd.read_csv('Titanic.csv')
# 删除缺失严重的Cabin变量
titanic.drop(labels='Cabin',axis=1,inplace=True)
# 根据Embarked变量，删除对应的缺失行
titanic.dropna(subset=['Embarked'], inplace=True)
# 删除无关紧要的变量（这些变量对后面预测年龄没有太多的帮助）
titanic.drop(labels=
['PassengerId','Name','Ticket','Embarked'], axis = 1, inplace=True)
# 将字符型的性别变量映射为数值变量
titanic.Sex = titanic.Sex.map({'male':1, 'female':0})
# 将数据拆分为两组，一是年龄缺失组，二是年龄非缺失组，后续基于非缺失值构建KNN模型，再对缺失组做预测
nomissing = titanic.loc[~titanic.Age.isnull(),]#非缺失组
missing = titanic.loc[titanic.Age.isnull(),]#缺失组
from sklearn import neighbors
X=nomissing.columns[nomissing.columns!='age']#提取所有自变量
knn = neighbors.KNeighborsRegressor()#构建模型
knn.fit(nomissing[X], nomissing.Age)#模型拟合
pred_age = knn.predict(missing[X])#年龄预测