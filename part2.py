# 2. Imagine that you are playing with a random number generator that produces
# values between 0 and 1, perfectly spread (uniformly distributed). Now, what if you could
# generate n of these numbers, calculate their mean and variance, and then watch how these
# statistics change as n grows larger and larger? Does randomness settle into predictable
# patterns as you generate more numbers? Try experimenting with different values of n.
# What do you observe and why do you think it happens?

import random
import numpy as np
import matplotlib.pyplot as plt
meanArray=[]
varArray=[]
def function(n):
    # creating array of size n(uniform distribution)
    arr=np.random.rand(n) 
    # print(arr)
    mean=arr.mean()
    var=arr.var()
    meanArray.append(mean)
    varArray.append(var)
    # print(meanArray)

n=[10,100,200,500,1000,2000,4000,6000,8000,10000,12000,14000,16000,18000,20000]
for i in n:
  function(i)

    
# Plotting results
plt.figure(figsize=(12, 6))

# Mean plot
plt.subplot(1, 2, 1)
plt.plot(n, meanArray, marker='o', label='Mean')
plt.axhline(0.5, color='r', linestyle='--', label='Expected Mean (0.5)')
plt.xscale('log')
plt.xlabel('n (log scale)')
plt.ylabel('Mean')
plt.title('Mean vs n')
plt.legend()
plt.grid(True)

# Variance plot
plt.subplot(1, 2, 2)
plt.plot(n, varArray, marker='o', label='Variance')
plt.axhline(1/12, color='r', linestyle='--', label='Expected Variance (1/12)')
plt.xscale('log')
plt.xlabel('n (log scale)')
plt.ylabel('Variance')
plt.title('Variance vs n')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
