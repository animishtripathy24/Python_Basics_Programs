import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0.,10.,0.1)
a=np.cos(x)
b=np.sin(x)
plt.plot(x,a,'r',label='cosx',linestyle='-.')
plt.plot(x,b,'g',label='sinx',linestyle='--')
plt.legend(loc='lower left')
plt.show()
