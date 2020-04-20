#!/usr/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.kernel_ridge import KernelRidge as knlr

df = pd.read_csv('T01.csv')
va = df.values
print(va.shape)
x=va[:,0].reshape(-1,1)
y=va[:,1].reshape(-1,1)
kr=knlr(alpha=1, kernel='polynomial')
kr.fit(x,y)
tx = np.linspace(500,5000,100)
tx = tx.reshape(-1,1)
ty = kr.predict(tx)
plt.scatter(x,y,marker='x')
plt.plot(tx,ty,color='g')
plt.show()
