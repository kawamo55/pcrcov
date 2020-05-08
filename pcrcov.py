#!/usr/bin/python3
# programed by M.kawase 組込AI研究所(Embed AI Labo.)
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.kernel_ridge import KernelRidge as knlr

df = pd.read_csv('summary.csv')
va = df.values
# データSkip数
skip=30
# 平均幅
wid=14
# 重傷者倍率
zb = 1
# 感染者数(日別)
yy = np.diff(va[skip:,3])
# 重傷者数(日別)
y2 = np.diff(va[skip:,12])
# PCR検査数(日別)
xx = np.diff(va[skip:,4])
# MAXPCR
maxpcr = 5000
# alpha Param
al = 1

# データの個数
n,=yy.shape

xt=np.array([])
yt=np.array([])
yz=np.array([])

# 平均加工
for i in range(wid,n):
#for i in range(wid,n,wid):
    xt = np.append(xt,np.mean(xx[i-wid:i]))
    yt = np.append(yt,np.mean(yy[i-wid:i]))
    yz = np.append(yz,zb*np.mean(y2[i-wid:i]))
x=xt.reshape(-1,1)
y=yt.reshape(-1,1)
z=yz.reshape(-1,1)
kr=knlr(alpha=al, kernel='polynomial')
kr.fit(x,y)
kz=knlr(alpha=al, kernel='polynomial')
kz.fit(x,z)
tx = np.linspace(500,maxpcr,100)
tx = tx.reshape(-1,1)
ty = kr.predict(tx)
tz = kz.predict(tx)
plt.scatter(x,y,marker='x',color='g')
plt.scatter(x,z,marker='.',color='r')
plt.plot(tx,ty,color='g')
plt.plot(tx,tz,color='r')
plt.show()
