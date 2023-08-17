import numpy as np
from matplotlib import pyplot as plt

data = np.fromfile('13-1750MHz-dump-fftw.bin', dtype="float32", count=-1)
data = data[:136867500]
data = np.reshape(data, (90, 1520750))

print(data)

# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
plt.imshow(data)
plt.show()
# plt.imsave("data.png", data)
