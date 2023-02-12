import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


data = pd.read_csv('../csv/DistSpMV_Reordered_preprocess.csv')
matrix=['../matrix/audikw_1.mtx','../matrix/bone010.mtx','../matrix/dielFilterV2real.mtx','../matrix/asia_osm.mtx','../matrix/ldoor.mtx','../matrix/nlpkkt80.mtx','../matrix/rajat31.mtx','../matrix/rgg_n_2_21_s0.mtx','../matrix/road_central.mtx','../matrix/inline_1.mtx','../matrix/hugebubbles-00000.mtx','../matrix/germany_osm.mtx','../matrix/italy_osm.mtx','../matrix/adaptive.mtx','../matrix/ecology1.mtx','../matrix/vas_stokes_1M.mtx','../matrix/AS365.mtx','../matrix/M6.mtx','../matrix/NLR.mtx','../matrix/cant.mtx']
xlabel=['audikw_1','bone010','dielFilterV2real','asia_osm','ldoor','nlpkkt80','rajat31','rgg_n_2_21_s0','road_central','inline_1','hugebubbles-00000','germany_osm','italy_osm','adaptive','ecology1','vas_stokes_1M','AS365','M6','NLR','cant']

reordertime = [0 for i in range(20)]
balancetime = [0 for i in range(20)]
for index, row in data.iterrows():
    for i in range(20):
        if row[0]==matrix[i]:
            temp =float(row[4])
            reordertime[i]=temp

data2 = pd.read_csv('../csv/DistSpMV_Balanced_preprocess.csv')
for index, row in data2.iterrows():
    for i in range(20):
        if row[0]==matrix[i]:
            temp =float(row[4])
            balancetime[i]=temp

size =20
#x=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0]

x_len = np.arange(20)
total_width, n = 0.8, 2
width = total_width/n
# x 就是三个柱子的开始位置
x = x_len - (total_width - width) / 2
# 画柱状图
plt.figure(figsize=(12,5))
plt.bar(x, reordertime, width=width, color='blue',label="DistSpMV_Reordered")
plt.bar(x + width, balancetime, width=width,color='red',label="DistSpMV_Balanced(our work)")
# 显示图例
plt.title('preprocess time combination figure')
plt.xticks(x,xlabel,fontsize=6)
pl.xticks(rotation=60)
plt.legend()
plt.savefig("../figure/fig7_preprocess_time.png")
# 显示柱状图
plt.show()
