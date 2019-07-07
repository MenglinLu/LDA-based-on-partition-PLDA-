# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 09:52:23 2017

@author: Administrator
"""
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import xlrd
import xlwt
import numpy as np
data = xlrd.open_workbook('doc_topic.xls')
table1 = data.sheets()[0]
table2=data.sheets()[1]
table3=data.sheets()[2]
train_data=[]
for i in range(table1.nrows):
    a=table1.row_values(i)
    train_data.append(a)
train_data=np.array(train_data)
train_result=table2.col_values(0)
ddata={'llabel':train_result}
frame=pd.DataFrame(ddata)
frame=frame.drop_duplicates(['llabel'])
train_result=np.array(train_result)
clf=RandomForestClassifier(n_estimators=100);
y,_=pd.factorize(train_result);
clf.fit(train_data,y);
test_data=[]
ad=np.array(frame);
targett=ad.tolist()
for i in range(table3.nrows):
    a=table3.row_values(i)
    test_data.append(a)
test_data=np.array(test_data)
preds=clf.predict(test_data)
workbook=xlwt.Workbook()
ws=workbook.add_sheet('test_result')
pre_len=len(preds)
for i in range(pre_len):
    a=preds[i];
    ws.write(i,0,str(targett[a]));
workbook.save('test_result.xls')


