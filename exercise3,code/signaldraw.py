import numpy as np
import matplotlib.pyplot as plt
n = range(300)
x1 = np.cos((6/9)*(np.pi)*np.asarray(n)+1)
x2= (np.cos(((np.pi)*np.asarray(n))/6))**2
x3 = np.cos(((np.pi)*np.asarray(n))/2)*np.cos(((np.pi)*np.asarray(n))/4)
plt.subplot(3,1,1)
plt.plot(n,x1,"-o")
plt.xlabel("x1 samples, number")
plt.ylabel("Amplitude, units")

plt.subplot(3,1,2)
plt.plot(n,x2,"-o")
plt.xlabel("x2 samples, number")
plt.ylabel("Amplitude, units")

plt.subplot(3,1,3)
plt.plot(n,x3,"-o")
plt.xlabel("x3 samples, number")
plt.ylabel("Amplitude, units")
plt.show()
