import numpy as np 
import matplotlib.pyplot as plt

# Question 1
arr = np.random.random(100000)
arr = arr*(3.3+2) - (3.3+2)/2
print(arr.min(), arr.max())

# Question 2
a1 = np.random.randint(1,70, 100000)
a2 = np.random.normal(0,1, 100000)
a = a1+a1
print(a.mean())

# Question 3
b = a1 * a2
print(b.mean())

# Question 4
nor = np.random.normal(0.3, 1.2, 100000)
print(nor.mean(), nor.std())

# Question 5 
v1 = np.random.randint(1,20, 100000)
v2 = np.random.randint(1,20, 100000)
v1 = v1[:-2]
v2 = v2[1:]
v = v1 - v2
his, bins = np.histogram(v, range=(-20,21))
plt.plot(hist)

# Question 6 
que = np.random.normal(3, 1.2, 100000)
bin_width = 0.05
hist, bins1 = np.histogram(que, bins=bin_width, range=(-0.6, 0.6))
plt.plot(hist)

# Question 7 
ones = np.random(100000)
idx = (ones==1).nonzero()[0]
idx = np.array(idx) + 1
plt.hist(idx)
plt.show()
