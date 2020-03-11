# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:26:00 2020

@author: Administrator
"""

import pandas as pd
data=pd.read_excel("D:Desktopdatasdata.xlsx")
#数据规模
data.shape
#数据类型
data.dtypes
#数值型转字符型
data['id']=data['id'].astype(str)
#字符型转数值型
data['custom_amt']=data['custom_amt'].str[1:].astype(float)#用切片去掉人民币符号“￥”
#字符转日期
data['order_date']=pd.to_datetime(data['order_date'],format='%Y年%m月%d日')
# 判断数据中是否存在重复数据
data.duplicated().any()#出现重复用drop_duplicates删除
# 构造数据
df=pd.DataFrame(dict(name=['张三','李四','王二','张三','赵五','丁一','王二'],gender = ['男','男','女','男','女','女','男'],age = [29,25,27,29,21,22,27],income = [15600,14000,18500,15600,10500,18000,13000],edu = ['本科','本科','硕士','本科','大专','本科','硕士']))
df.drop_duplicates()
df.drop_duplicates(subset=['name','age'])#基于特征删除重复

