#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 13:43:40 2017

@author: ZHANG Shuang
"""    
    
from gensim import corpora, models, similarities
import matplotlib.pyplot as plt 
import numpy as np 
import os
import xlwt
file=open('C:\\Users\\Administrator\\Desktop\\original_lda\\ddata.txt','r')
#courses =[];
#for line in file:
#    courses.append(line.strip().split(' '))#将文本中的字符依据空格一字字分开，变成list
courses = [line.strip().split() for line in file];
dic = corpora.Dictionary(courses) #为每个单词分配一个id
corpus = [dic.doc2bow(text) for text in courses]#把文档doc变成一个稀疏矩阵
#corpus_tfidf=models.TfidfModel(corpus)[corpus]
numoftopics=50;
lda = models.LdaModel(corpus, id2word = dic,alpha=0.01, eta=0.05,iterations=2000, num_topics =numoftopics,minimum_probability=0.00000001)
#文件j表示主题-词分布
f=open('C:\\Users\\Administrator\\Desktop\\original_lda\\ml_period5topic25a0.01j.txt','w') 
for topic_id in range(numoftopics):
    f.write('*Topic:'+str(topic_id))
    f.write(str(lda.show_topic(topic_id)))
    f.write('\n')
#文件f用来表示每个文档和各个主题的分布
fenbu=open('C:\\Users\\Administrator\\Desktop\\original_lda\\ml_period4qtopic20a0.01f.txt','w')
ff=open('C:\\Users\\Administrator\\Desktop\\original_lda\\ml_period5topic25a0.01jj.txt','w')
label = []
i=1
doc_topic = [lda[a] for a in corpus]
for line in doc_topic:
    fenbu.write(str(line))#将数字型变量或常量转化为字符型变量或常量
    fenbu.write('\n')
    ret_x=[y for [x,y] in line]
    ff.write(str(ret_x)+'\n')    
fenbu.close()
doc_topic = [lda[a] for a in corpus]
workbook=xlwt.Workbook()
ws=workbook.add_sheet('topic_doc')
filelist = os.listdir('C:\\Users\\Administrator\\Desktop\\original_lda\\rawdata')
i=0;
for line in doc_topic:
    ret_x=[y for [x,y] in line]
    filelistname=str(filelist[i]);
    for j in range(numoftopics):
        vval=ret_x[j];
        ws.write(i,j,vval);
    ws.write(i,numoftopics,filelistname)
    i=i+1;
workbook.save('doc_topic.xls')
f.close()
ff.close()
file.close()
