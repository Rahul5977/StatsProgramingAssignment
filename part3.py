# Repeat the same experiment as in Question 2 but for a Gaussian distribution
# having 4 and standard deviation as 4 and 3 respectively.

import numpy as np
import matplotlib.pyplot as plt
n=[100,500,1000,15000,20000,25000,30000]
for i in n:
    arr=np.random.normal(4,3,i)

    plt.hist(arr, bins=30, density=True, alpha=0.6, color='blue')

    # Overlay the theoretical Gaussian curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 10000)
    p = (1 / (np.sqrt(2 * np.pi * 3**2))) * np.exp(-0.5 * ((x - 4) / 3)**2)
    plt.plot(x, p, 'k', linewidth=2)

    plt.title("Gaussian Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()