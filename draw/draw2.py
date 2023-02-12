
import seaborn
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
import seaborn as sns
sns.set()


data = pd.read_csv('../csv/DistSpMV_Reordered_com.csv')
matrix=['../matrix/road_central.mtx','../matrix/inline_1.mtx']
uniform_data=[[[]for i in range(8)] for i in range(8)]
for index, row in data.iterrows():
    if row[0]==matrix[0]:
        x =int(row[1])
        y=int(row[2])
        #print(x,y)
        num=int(row[3])
        uniform_data[x][y]=num
x = ["np0","np1","np2","np3","np4","np5","np6","np7"]
seaborn.set(font_scale=0.8)
# heatmap = sns.heatmap(uniform_data,vmin=0,vmax=500,annot=True,fmt="d",cmap="YlGnBu",cbar=False,xticklabels=x,yticklabels=x) # 生成热力图
heatmap = sns.heatmap(uniform_data,vmin=0,vmax=500,annot=True,fmt="d",cmap="YlGnBu",xticklabels=x,yticklabels=x) # 生成热力图
heatmap.set_title("DistSpMV_Reordered_road_central",fontsize=15)
figure = heatmap.get_figure()
figure.savefig('../figure/DistSpMV_Reordered_road_central_heatmap.jpg')  # 保存图片
plt.show()

uniform_data=[[[]for i in range(8)] for i in range(8)]
for index, row in data.iterrows():
    if row[0]==matrix[1]:
        x =int(row[1])
        y=int(row[2])
        #print(x,y)
        num=int(row[3])
        uniform_data[x][y]=num
x = ["np0","np1","np2","np3","np4","np5","np6","np7"]
seaborn.set(font_scale=0.8)
# heatmap = sns.heatmap(uniform_data,vmin=0,vmax=500,annot=True,fmt="d",cmap="YlGnBu",cbar=False,xticklabels=x,yticklabels=x) # 生成热力图
heatmap = sns.heatmap(uniform_data,vmin=0,vmax=500,annot=True,fmt="d",cmap="YlGnBu",xticklabels=x,yticklabels=x) # 生成热力图
heatmap.set_title("DistSpMV_Balanced_inline_1",fontsize=15)
figure = heatmap.get_figure()
figure.savefig('../figure/DistSpMV_Reordered_inline_1_heatmap.jpg')  # 保存图片
plt.show()