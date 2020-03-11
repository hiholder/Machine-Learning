# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:15:55 2020

@author: Administrator
"""

import numpy as np
import pandas as pd
#位置索引
np.random.seed(1)
s1=pd.Series(np.random.randint(size=5,low=1,high=10))
print(s1)
print(s1[0])#取第一个元素
print(s1[1:3],'\n')#取2到3个元素
print(s1[::2],'\n')#依次取数步长为2
#用ita方法倒序取数
print(s1.iat[-3],'\n')#取倒数第三个元素
print(s1[-3:],'\n')#取倒数第三个元素后所有元素

#布尔索引
np.random.seed(2)
s1=pd.Series(np.random.randint(size=5,low=1,high=100))
print(s1,'\n')
print(s1[s1>60],'\n')#取出大于60的值
print(s1[s1>=40][s1<=50])#取出40到50之间的值

#序列元素成员关系
arr1=np.array([1,2,3,4])
arr2=np.array([10,20,3,40])
print(np.in1d(arr1,arr2))#元素是否包含于另一个向量
s1=pd.Series(['A','B','C','D'])
s2=pd.Series(['X','A','Y','D'])
print(s1.isin(s2))
print(np.in1d(s1,s2))

#序列排重和水平统计
np.random.seed(3)
s=np.random.randint(size=1000,low=1,high=4)
print(pd.unique(s))#排除重复
print(pd.value_counts(s))#数量统计

#序列的排序
np.random.seed(4)
s=pd.Series(np.random.normal(size=4))
print(s.sort_index(ascending=False))#按索引降序排列
print(s.sort_values())#按数据的实际值升序排列

#抽样
s=pd.Series(range(1,101))
print(s.sample(n=3,frac=None,replace=False,weights=None,random_state=2,axis=None))
#n表示抽取样本的数量，frac指定抽取样本的比例，replace是否有放回默认无放回，weight指权重，random_state表示随机数种子
s=pd.Series(range(1,6))
print(s.sample(n=3,replace=True,random_state=2))

#序列汇总
np.random.seed(1234)
s=pd.Series(np.random.randint(size=100,low=10,high=30))
s.describe()
#其中count是序列中非缺失元素的个数

#判断数据缺失
s=pd.Series([1,2,np.nan,4,np.nan,6])
print(s)
print(s.isnull())
