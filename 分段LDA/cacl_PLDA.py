# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:54:01 2017

@author: Administrator
"""

import os
import sys
from gensim import corpora,models,similarities
import matplotlib.pyplot as plt
import xlwt
from numpy import *
import numpy as np
np.set_printoptions(threshold=np.inf)
filelist = os.listdir('C:\\Users\\Administrator\\Desktop\\partlda\\rawdata')
num_section=[] #每个文件所含的段落数
rate_part=[]#每个段落所占的比例
for item in filelist:
    iitem = 'C:\\Users\\Administrator\\Desktop\\partlda\\rawdata\\' + item
    fp = open(iitem,'r')
    i=0;
    whole_num=0;#一篇文档总词数
    for linea in fp.readlines():
        llinea=linea.replace('nbsp/n','')
        if(llinea.strip()!=''):
            i = i+1;
            cour = llinea.strip().split(' ')
            num_part = len(cour) #每个段落的词数
            whole_num = whole_num+num_part
    num_section.append(i)
    iitem = 'C:\\Users\\Administrator\\Desktop\\partlda\\rawdata\\' + item
    fp = open(iitem,'r')
    for linea in fp.readlines():
        llinea=linea.replace('nbsp/n','')
        if(llinea.strip()!=''):
            cour = llinea.strip().split(' ')
            num_part = len(cour) #每个段落的词数   
            rate_part.append(num_part*1.0/whole_num)   
rate_part=np.matrix(rate_part)
numoftopic=[150,200,250];
for numoftopics in numoftopic:
    file=open('C:\\Users\\Administrator\\Desktop\\partlda\\ddata.txt','r')
    courses = [line.strip().split(' ') for line in file]
    dic = corpora.Dictionary(courses)
    corpus = [dic.doc2bow(text) for text in courses]#把文档doc变成一个稀疏矩阵
#corpus_tfidf=models.TfidfModel(corpus)[corpus]
    lda = models.LdaModel(corpus, id2word = dic,alpha=0.01, eta=0.05,iterations=2000, num_topics =numoftopics,minimum_probability=0.000000001)
#corpus_lda = lda[corpus]
#f=open('C:\\Users\\Administrator\\Desktop\\partlda\\ml_period5topic25a0.01j.txt','w')
#
#for topic_id in range(numoftopics):
#    f.write('*Topic:'+str(topic_id))
#    f.write(str(lda.show_topic(topic_id)))
#    f.write('\n')
#   
#fenbu=open('C:\\Users\\Administrator\\Desktop\\partlda\\ml_period4qtopic20a0.01f.txt','w')
##w=open('C:\\Users\\Administrator\\Desktop\\partlda\\ml_period4qtopic20a0.01s.txt','w')
#ff=open('C:\\Users\\Administrator\\Desktop\\partlda\\ml_period5topic25a0.01jj.txt','w')
    label = []
    i=1
    doc_topic = [lda[a] for a in corpus]
#for line in doc_topic:
#    fenbu.write(str(line))#将数字型变量或常量转化为字符型变量或常量
#    fenbu.write('\n')
#    ret_x=[y for [x,y] in line]
#    ff.write(str(ret_x)+'\n')    
#fenbu.close()
#f.close()
#ff.close()
    file.close()
    mtx_fenbu=zeros(numoftopics);
    for lline in doc_topic:
        ret_xx=[y for [x,y] in lline]
        mtx_fenbu=np.row_stack((mtx_fenbu,ret_xx))
#w.write(str(mtx_fenbu))
#w.close()
    workbook=xlwt.Workbook()
    ws=workbook.add_sheet('topic_doc')
    filelist = os.listdir('C:\\Users\\Administrator\\Desktop\\partlda\\rawdata')
    b=zeros(len(filelist)+1);
    b.astype(int)
    ggg=len(filelist)+1
    for i in range(1,ggg):
        a = num_section[i-1]
        b[i]=b[i-1]+a;
        cc=int(b[i-1])+1
        dd=int(b[i])+1
        ee=int(b[i-1])
        gg=int(b[i]-1)+1
        mtx1=mtx_fenbu[cc:dd,:]
        mtx2=rate_part[:,ee:gg]
        mtx=mtx2*mtx1
        filelistname=str(filelist[i-1])
        for j in range(numoftopics):
            vval=mtx[0,j]
            ws.write(i-1,j,vval)
        ws.write(i-1,numoftopics,filelistname)
    workbook.save('doc_topic'+str(numoftopics)+'.xls')

    


# 备注：
# 文件f 是文章对应主题分布
# 文件ss 是按最大分布概率判断文章属于哪个主题
# 文件j1 是提取的主题词
# a0.01 表示alpha=0.01 eta=0.05
# topicX 表示提取了x个主题