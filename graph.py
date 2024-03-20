import matplotlib.pyplot as plt
sub=['physics','chemistry','maths','english','ip']
t1=[6,10,3,8,9]
t2=[9,10,7,8,4]
plt.plot(sub,t1,label='wt-1',linewidth=3,linestyle='-.',marker='o',markersize=8,markeredgecolor='red')
plt.plot(sub,t2,label='wt-2',linewidth=3,linestyle='--',marker='o',markersize=8,markeredgecolor='yellow')
plt.title('student performance')
plt.xlabel('subject name')
plt.ylabel('marks obtained')
plt.legend(loc='lower left')
plt.ylim(1,10)
plt.yticks([3,4,6,7,8,9,10])
plt.show()
