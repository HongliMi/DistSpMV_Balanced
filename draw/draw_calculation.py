# importing pandas package
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('../csv/DistSpMV_Balanced_calculation.csv')
data.sort_values(' process', axis=0, ascending=True, inplace=True)
matrix=['../matrix/road_central.mtx','../matrix/inline_1.mtx']
title=['road_central','inline_1']
#balanced information
message = [[0 for i in range(8)] for i in range(2)] 
local = [[0 for i in range(8)] for i in range(2)]
remote = [[0 for i in range(8)] for i in range(2)]
#reordered information
message1 = [[0 for i in range(8)] for i in range(2)] 
local1 = [[0 for i in range(8)] for i in range(2)]
remote1 = [[0 for i in range(8)] for i in range(2)]
idx=0
for index, row in data.iterrows():
    idx=idx+1
    for i in range(2):
        if row[0]==matrix[i]:
            m=int(row[2])
            l=int(row[3])
            r=int(row[4])
            message[i][int((idx-1)/2)]=m;
            local[i][int((idx-1)/2)]=l;
            remote[i][int((idx-1)/2)]=r;

data2 = pd.read_csv('../csv/DistSpMV_Reordered_calculation.csv')
data2.sort_values(' process', axis=0, ascending=True, inplace=True)

idx=0
for index, row in data2.iterrows():
    idx=idx+1
    for i in range(2):
        if row[0]==matrix[i]:
            m=int(row[2])
            l=int(row[3])
            r=int(row[4])
            message1[i][int((idx-1)/2)]=m;
            local1[i][int((idx-1)/2)]=l;
            remote1[i][int((idx-1)/2)]=r;



plt.figure(dpi=128, figsize=(5, 5))
c=0
plt.suptitle('communication volume per-process',fontsize=15)  
x=[0,10,20,30,40,50,60,70]
xlabel = ["np0","np1","np2","np3","np4","np5","np6","np7"]
for i in range(2):
    c=c+1
    plt.subplot(2, 1, c)
    plt.plot(x, message[i], linewidth =1.0,c='yellow',label='DistSpMV_Balanced',marker='.') 
    plt.plot(x, message1[i],linewidth =1.0, c='black',label='DistSpMV_reordered',marker='.') 
    plt.title(matrix[i], fontsize=6)
    plt.xticks([0,10,20,30,40,50,60,70],
               xlabel,
              fontsize=4);
    plt.yticks(fontsize=4)
    plt.subplots_adjust(wspace =0.3, hspace =0.5)
    plt.legend(fontsize=4)
    plt.title(title[i])
plt.savefig("../figure/figure5_cummunication.png")
plt.show()

plt.figure(dpi=128, figsize=(5, 5))
plt.suptitle('local matrix calculation per-process',fontsize=15)  
c=0
x=[0,10,20,30,40,50,60,70]
xlabel = ["np0","np1","np2","np3","np4","np5","np6","np7"]
for i in range(2):
    c=c+1
    plt.subplot(2, 1, c)
    plt.plot(x, local[i], linewidth =1.0,c='red',label='DistSpMV_Balanced',marker='.') 
    plt.plot(x, local1[i],linewidth =1.0, c='blue',label='DistSpMV_reordered',marker='.') 
    plt.title(matrix[i], fontsize=6)
    plt.xticks([0,10,20,30,40,50,60,70],
               xlabel,
              fontsize=4);
    plt.yticks(fontsize=4)
    plt.subplots_adjust(wspace =0.3, hspace =0.5)
    plt.legend(fontsize=4)
    plt.title(title[i])
plt.savefig("../figure/figure5_local_calculation.png")
plt.show()

plt.figure(dpi=128, figsize=(5, 5))
plt.suptitle('remote matrix calculation per-process',fontsize=15)  
c=0
x=[0,10,20,30,40,50,60,70]
xlabel = ["np0","np1","np2","np3","np4","np5","np6","np7"]
for i in range(2):
    c=c+1
    plt.subplot(2, 1, c)
    plt.plot(x, remote[i], linewidth =1.0,c='brown',label='DistSpMV_Balanced',marker='.') 
    plt.plot(x, remote1[i],linewidth =1.0, c='purple',label='DistSpMV_reordered',marker='.') 
    plt.title(matrix[i], fontsize=6)
    plt.xticks([0,10,20,30,40,50,60,70],
               xlabel,
              fontsize=4);
    plt.yticks(fontsize=4)
    plt.subplots_adjust(wspace =0.3, hspace =0.5)
    plt.legend(fontsize=4)
    plt.title(title[i])
plt.savefig("../figure/figure5_remote_calculation.png")
plt.show()