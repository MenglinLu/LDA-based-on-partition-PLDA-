# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 20:02:10 2017

@author: Administrator
"""
from numpy import * 
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import gensim, logging
import os
import xlwt
logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s', level = logging.INFO)
sentences = gensim.models.doc2vec.TaggedLineDocument('ddata.txt')
numoftopic=100;
model = gensim.models.Doc2Vec(sentences, size = numoftopic, window = 5)
model.save('review_pure_text_model.txt')
resul=enumerate(model.docvecs);
value=[];
for docvec in resul:
    value.append(docvec[1]);
mat_val=zeros([len(value),numoftopic]);
for i in range(len(value)):
    j=0;
    for j in range(numoftopic):
        mat_val[i][j]=value[i][j];
train_result=[];
train_data=mat_val[0:3200,:];
test_data=mat_val[3200:4000,:];
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
#print len(model.docvecs)
#workbook=xlwt.Workbook()
#ws=workbook.add_sheet('doc2vec_representation');
#i=0; 
#for idx, docvec in enumerate(model.docvecs):
#    j=0;
#    for value in docvec:
#        ws.write(i,j,str(value));
#        j=j+1;
#    i+i+1;
#workbook.save('doc2vec_representation.xls')
#out = open('review_pure_text_vector.txt', 'w')
#for idx, docvec in enumerate(model.docvecs):
#    for value in docvec:
#      out.write(str(value) + ' ')
#    out.write('\n')
#    print idx
#    print docvec
#out.close()