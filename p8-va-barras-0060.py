import numpy as np
import matplotlib.pyplot as plt

diasX=["lun", "mar", "mie", "jue", "vie"]
califa_va_y=[5,6,3,8,10]
plt.bar(diasX,califa_va_y)
plt.title("califas en VA de Ambar Fierro NC = 0060")
plt.xlabel("dias semana habil")
plt.ylabel("califacaciones en VA")
plt.grid()
plt.show()

