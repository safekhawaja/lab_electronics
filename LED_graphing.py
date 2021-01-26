import numpy as np

import matplotlib.pyplot as plt

i = np.array([])

v = np.array([])

plt.plot(i, v, '*-')
[<matplotlib.lines.Line2D at 0x7f9bbad5e0f0>]

plt.ylabel("LED Voltage [V]"); plt.xlabel("LED Current [mA]");

plt.axis([0, None, 1.5, 1.9])
[0, None, 1.5, 1.9]
