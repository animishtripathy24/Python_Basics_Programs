import matplotlib.pyplot as plt
import numpy as np
sub=['physics','chemistry','maths','english','i.p']
l=np.arange(len(sub))
wt1=[6,8,4,9,10]
wt2=[9,6,10,5,8]
plt.title('Student Performance')
plt.grid(True)
plt.legend(loc='upper left')
plt.bar(sub,wt1,width=0.25)
plt.bar(l+0.25,wt2,width=0.25)
plt.show()
