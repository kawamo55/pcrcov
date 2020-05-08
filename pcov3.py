#!/usr/bin/python3
# programed by M.kawase 組込AI研究所(Embed AI Labo.)
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('summary.csv')
va = df.values
# データSkip数
skip=20
# 平均幅
wid=7
# 倍率
by1 = 5 
# 倍率
by2 = 100
# ratio倍率
by3 = 10000
# 感染者数(日別)
yy1 = np.diff(va[skip:,3])
# 重傷者数(日別)
yy2 = np.diff(va[skip:,12])
# PCR検査数(日別)
yy3 = np.diff(va[skip:,4])
# 日数
xx = 0

# データの個数
n,=yy1.shape

xt=np.array([])
y1=np.array([])
y2=np.array([])
y3=np.array([])

# 平均加工
for i in range(wid,n):
    xt = np.append(xt,i-wid)
    y1 = np.append(y1,np.mean(yy1[i-wid:i]))
    y2 = np.append(y2,np.mean(yy2[i-wid:i]))
    y3 = np.append(y3,np.mean(yy3[i-wid:i]))
y4=by3*y1/y3
plt.plot(xt,by1*y1,color='g',label=str(by1)+' x infected')
plt.plot(xt,by2*y2,color='r',label=str(by2)+' x serious')
plt.plot(xt,y3,color='b',label='PCR')
plt.plot(xt,y4,color='y',label=str(by3)+' x ratio')
plt.legend(loc='upper left', borderaxespad=1, fontsize=12)
plt.show()
