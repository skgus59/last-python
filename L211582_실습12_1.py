import numpy as np
import matplotlib.pyplot as plt
a=np.array([[75,89,92,78],[90,76,88,83],[55,99,81,88],[80,67,75,91]])
b=np.array(['A','B','C','D'])
c=np.array(['Kor', 'Math', 'Eng', 'Com'])
A=np.sum(a, axis=1)
x=np.divide(A,4) #학생평균
B=np.sum(a, axis=0)
y=np.divide(B,4) #과목평균
plt.plot(b,x,'go--') #학생 그래프
plt.show()
plt.plot(c,y,'go--') #과목 그래프
plt.show()


