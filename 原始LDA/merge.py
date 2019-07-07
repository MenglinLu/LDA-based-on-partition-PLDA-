#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:55:53 2017

@author: Administrator
"""
from gensim import corpora, models, similarities
import matplotlib.pyplot as plt 
import numpy as np 
import os
filelist=os.listdir('C:\\Users\\Administrator\\Desktop\\original_lda\\rawdata');
for item in filelist:
    iitem='C:\\Users\\Administrator\\Desktop\\original_lda\\rawdata\\'+item;
    newfile=open('C:\\Users\\Administrator\\Desktop\\original_lda\\rawdata1\\'+item,'a');
    src=open(iitem,'r');
    string5='';
    for line in src:
        if(line.strip()!=''):
            line=line.strip('\n');
            data=line.strip();
            string=str(data);
            string0=string.replace('\n',' ');
            string1=string0.replace('[','');
            string2=string1.replace(']','');
            string3=string2.replace(',',' ');
            string4=string3.replace('nbsp/n','');
            string5=string5+' '+string4;
#    string5=string5.decode('gbk');
#    string5=string5.encode('utf-8');
    newfile.write(string5);
    newfile.write('\n');
    newfile.close();
filelist = os.listdir('C:\\Users\\Administrator\\Desktop\\original_lda\\rawdata1')
newfile = open('C:\\Users\\Administrator\\Desktop\\original_lda\\ddata.txt','a')
for item in filelist:
    iitem = 'C:\\Users\\Administrator\\Desktop\\original_lda\\rawdata1\\' + item
    for txt in open(iitem,'r'):
        newfile.write(txt)   
newfile.close()
    