# importing pandas package
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

def getidx(a):
    if(a==1): return 0;
    if(a==2): return 1;
    if(a==4): return 2;
    if(a==8): return 3;
    if(a==16): return 4;
    if(a==32): return 5;
    if(a==64): return 6;
    



data = pd.read_csv('../csv/DistSpMV_Balanced.csv')
data.sort_values(' process', axis=0, ascending=True, inplace=True)
matrix=['../matrix/audikw_1.mtx','../matrix/bone010.mtx','../matrix/dielFilterV2real.mtx','../matrix/asia_osm.mtx','../matrix/ldoor.mtx','../matrix/nlpkkt80.mtx','../matrix/rajat31.mtx','../matrix/rgg_n_2_21_s0.mtx','../matrix/road_central.mtx','../matrix/inline_1.mtx','../matrix/hugebubbles-00000.mtx','../matrix/germany_osm.mtx','../matrix/italy_osm.mtx','../matrix/adaptive.mtx','../matrix/ecology1.mtx','../matrix/vas_stokes_1M.mtx','../matrix/AS365.mtx','../matrix/M6.mtx','../matrix/NLR.mtx','../matrix/cant.mtx']
GFlops = [[0 for i in range(7)] for i in range(20)]
GFlops2 = [[0 for i in range(7)] for i in range(20)]
GFlops3 = [[0 for i in range(7)] for i in range(20)]
num = [[] for i in range(20)]
for index, row in data.iterrows():
    for i in range(20):
        if row[0]==matrix[i]:
            g =float(row[7])
            temp=float(row[8])
            idx=getidx(temp)
            GFlops[i][idx]=g


data2 = pd.read_csv('../csv/DistSpMV_Reordered.csv')
data2.sort_values(' process', axis=0, ascending=True, inplace=True)
for index, row in data2.iterrows():
    for i in range(20):
        if row[0]==matrix[i]:
            g =float(row[7])
            temp=float(row[8])
            idx=getidx(temp)
            GFlops2[i][idx]=g



data3 = pd.read_csv('../csv/DistSpMV.csv')
data3.sort_values(' process', axis=0, ascending=True, inplace=True)
matrix=['../matrix/audikw_1.mtx','../matrix/bone010.mtx','../matrix/dielFilterV2real.mtx','../matrix/asia_osm.mtx','../matrix/ldoor.mtx','../matrix/nlpkkt80.mtx','../matrix/rajat31.mtx','../matrix/rgg_n_2_21_s0.mtx','../matrix/road_central.mtx','../matrix/inline_1.mtx','../matrix/hugebubbles-00000.mtx','../matrix/germany_osm.mtx','../matrix/italy_osm.mtx','../matrix/adaptive.mtx','../matrix/ecology1.mtx','../matrix/vas_stokes_1M.mtx','../matrix/AS365.mtx','../matrix/M6.mtx','../matrix/NLR.mtx','../matrix/cant.mtx']
for index, row in data3.iterrows():
    for i in range(20):
        if row[0]==matrix[i]:
            g =float(row[7])
            temp=float(row[8])
            idx=getidx(temp)
            GFlops3[i][idx]=g



plt.figure(dpi=128, figsize=(20, 20))
c=0
x=[1,10,20,30,40,50,60]
for i in range(20):
    c=c+1
    plt.subplot(4, 5, c)
    plt.plot(x, GFlops[i], linewidth =1.0,c='red',label='DistSpMV_Balanced') 
    plt.plot(x, GFlops2[i],linewidth =1.0, c='green',label='DistSpMV_reordered') 
    plt.plot(x, GFlops3[i],linewidth =1.0, c='blue',label='DistSpMV') 
    plt.ylabel("GFlops", fontsize=6)
    plt.xlabel('', fontsize=3)
    plt.title(matrix[i], fontsize=6)
    plt.xticks([0,10,20,30,40,50,60],
               [1,2,4,8,16,32,64],
              fontsize=4);
    plt.yticks(fontsize=4)
    plt.subplots_adjust(wspace =0.3, hspace =0.5)
    plt.legend(fontsize=4)

    
plt.savefig("../figure/fig4_performance.png")
plt.show()
