#!/usr/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.kernel_ridge import KernelRidge as knlr

df = pd.read_csv('summary.csv')
va = df.values
skip=20
wid=7
yy = np.diff(va[skip:,3])
xx = np.diff(va[skip:,4])
n,=yy.shape
xt=np.array([])
yt=np.array([])
for i in range(wid,n):
    xt = np.append(xt,np.mean(xx[i-wid:i]))
    yt = np.append(yt,np.mean(yy[i-wid:i]))
x=xt.reshape(-1,1)
y=yt.reshape(-1,1)
kr=knlr(alpha=1, kernel='polynomial')
kr.fit(x,y)
tx = np.linspace(500,5000,100)
tx = tx.reshape(-1,1)
ty = kr.predict(tx)
plt.scatter(x,y,marker='x')
plt.plot(tx,ty,color='g')
plt.show()
