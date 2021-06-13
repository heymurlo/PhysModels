import matplotlib.pyplot as plt
import numpy as np

y = [0.02, 0.12, 0.229, 0.392, 0.509, 0.630, 0.809]

x = [12.097, 12.346, 12.5, 12.987, 13.273, 13.575, 14.019]


b, a = np.polyfit(x, y, 1)
abline_values = [b * i + a for i in x]

# Plot the best fit line over the actual values
plt.plot(x, y, '--')
plt.plot(x, abline_values, 'b')
plt.title('График зависимости запирающего напряжения от частоты')
plt.xlabel('частота')
plt.ylabel('зап. напряжение')
a_ = round(a, 3)
slo = round(b, 18)
plt.show()
print("b =", b, "a =", a)
