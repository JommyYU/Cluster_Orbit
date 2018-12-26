#coding=utf-8
#读取数据
import matplotlib.pyplot as plt
import numpy as np
import 

dataset = np.load("dataset.npy")

plt.plot(dataset[:,0],dataset[:,1])
plt.show()



