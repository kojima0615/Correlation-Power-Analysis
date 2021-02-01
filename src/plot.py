import numpy as np
import matplotlib.pyplot as plt

corr = np.load("./csv/corr_0123_mask.npy")
print(corr.shape)

corr = corr.T

plt.figure(figsize = (15,10))

for i in range(256):
    plt.plot(corr[i],color='grey')

plt.plot(corr[true_key],color='red')
plt.show()
plt.savefig("./image/corr_0123_mask.png")

