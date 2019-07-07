# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 14:57:11 2017

@author: Administrator
"""

import os  
import sys  
import xlwt
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
file=open('C:\\Users\\Administrator\\Desktop\\original_lda\\ddata.txt','r')
filelist = os.listdir('C:\\Users\\Administrator\\Desktop\\original_lda\\rawdata')
courses = [line for line in file];
vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频  
transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值  
tfidf=transformer.fit_transform(vectorizer.fit_transform(courses))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵  
word=vectorizer.get_feature_names()#获取词袋模型中的所有词语  
weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重 
train_result=[];
train_data=weight[0:3200,:];
test_data=weight[3200:4000,:];
for i in range(3200):
    if i>=0 and i<=799:
        train_result.append('C1');
    if i>=800 and i<=1599:
        train_result.append('C2');
    if i>=1600 and i<=2399:
        train_result.append('C3');
    if i>=2400 and i<=3200:
        train_result.append('C4');
clf=RandomForestClassifier(n_estimators=100);
y,_=pd.factorize(train_result);
clf.fit(train_data,y);
preds=clf.predict(test_data)
targett=['C1','C2','C3','C4']
workbook=xlwt.Workbook()
ws=workbook.add_sheet('test_result')
pre_len=len(preds)
for i in range(pre_len):
    a=preds[i];
    ws.write(i,0,str(targett[a]));
workbook.save('test_result.xls')   
#workbook=xlwt.Workbook()
#ws=workbook.add_sheet('vsm_representation'); 
#for i in range(len(weight)):
#    for j in range(len(word)): 
#        vvalue=weight[i][j];
#        ws.write(i,j,vvalue);
#file.close;
#workbook.save('vsm_representation.xls')
