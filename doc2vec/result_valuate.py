# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 11:25:00 2017

@author: Administrator
"""
from __future__ import division
import pandas as pd
import xlrd
import xlwt
import numpy as np
data = xlrd.open_workbook('doc_topic.xls')
table1 = data.sheets()[3];
y_true=table1.col_values(0);
y_pre=table1.col_values(1);
tp1=0;
tp2=0;
tp3=0;
tp4=0;
fp1=0;
fp2=0;
fp3=0;
fp4=0;
tn1=0;
tn2=0;
tn3=0;
tn4=0;
fn1=0;
fn2=0;
fn3=0;
fn4=0;
for i in range(len(y_true)):
    tp1 = tp1+(y_true[i]=='C1')*(y_pre[i]=='C1');
    fp1 = fp1+(y_pre[i]=='C1')*(y_true[i]!='C1');
    tn1 = tn1+ (y_pre[i]!='C1')*(y_true[i]!='C1');
    fn1 = fn1+ (y_pre[i]!='C1')*(y_true[i]=='C1');
    tp2 = tp2+(y_true[i]=='C2')*(y_pre[i]=='C2');
    fp2 = fp2+(y_pre[i]=='C2')*(y_true[i]!='C2');
    tn2 = tn2+ (y_pre[i]!='C2')*(y_true[i]!='C2');
    fn2 = fn2+ (y_pre[i]!='C2')*(y_true[i]=='C2');
    tp3 = tp3+(y_true[i]=='C3')*(y_pre[i]=='C3');
    fp3 = fp3+(y_pre[i]=='C3')*(y_true[i]!='C3');
    tn3 = tn3+ (y_pre[i]!='C3')*(y_true[i]!='C3');
    fn3 = fn3+ (y_pre[i]!='C3')*(y_true[i]=='C3');
    tp4 = tp4+(y_true[i]=='C4')*(y_pre[i]=='C4');
    fp4 = fp4+(y_pre[i]=='C4')*(y_true[i]!='C4');
    tn4 = tn4+ (y_pre[i]!='C4')*(y_true[i]!='C4');
    fn4 = fn4+ (y_pre[i]!='C4')*(y_true[i]=='C4');
pre1=tp1/(tp1+fp1);
rcc1=tp1/(tp1+fn1);
f11=2*pre1*rcc1/(pre1+rcc1);
pre2=tp2/(tp2+fp2);
rcc2=tp2/(tp2+fn2);
f12=2*pre2*rcc2/(pre2+rcc2);
pre3=tp3/(tp3+fp3);
rcc3=tp3/(tp3+fn3);
f13=2*pre3*rcc3/(pre3+rcc3);
pre4=tp4/(tp4+fp4);
rcc4=tp4/(tp4+fn4);
f14=2*pre4*rcc4/(pre4+rcc4);
P1=(pre1+pre2+pre3+pre4)/4;
R1=(rcc1+rcc2+rcc3+rcc4)/4;
F1=(f11+f12+f13+f14)/4;

workbook=xlwt.Workbook()
ws=workbook.add_sheet('test_result')
ws.write(0,0,'Precision:');
ws.write(0,1,str(P1));
ws.write(0,2,'Recall:');
ws.write(0,3,str(R1));
ws.write(0,4,'F1:');
ws.write(0,5,str(F1));
workbook.save('result_valuate.xls')

