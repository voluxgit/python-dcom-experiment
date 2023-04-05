from matplotlib import pyplot as mt
import numpy as np

def plot(n,t,k,c,b):
    mt.subplot(3, 2, n)
    mt.step(t,k,where=c)
    mt.grid(True, which='both')
    mt.vlines(x=b, ymin = 0.0, ymax = max(k))
    mt.axhline(y=0,color = 'black')
    mt.ylabel("Gain ")
    mt.xlabel("Time ")


a = input('Enter the voltage level of the pulse:-')
numList1 = a.split()
A2 = list(map(int, numList1))
w = int(input('enter the width of the pulse :- '))
T = np.arange(0,w+0.5,0.5)
t1 = list(T)
A1 = [0] + A2*(len(t1)-2) + A2
t = t1.copy()
k = A1.copy()
fig, ax = mt.subplots(3, 2)
fig.tight_layout(h_pad=2)

"""P(t)"""
plot(1,t,k,'pre',max(t))
mt.grid(True, which='both')
mt.title('P(t)')

"""p(-t)"""
for i in range(len(t)):
    t[i] = t[i] * -1
t.reverse()
k.reverse()
plot(2,t,k,'post',min(t))
mt.tick_params(labelright = True, labelleft = False)
mt.title('p(-t)')

"""P(T-t)"""
T = int(input('enter the T to shift :- '))
for i in range(len(t)):
    t[i] = t[i] + T

plot(3,t,k,'post',min(t))
mt.title('p(T-t)')

"""h(t)"""
j = int(input('Enter the gain (k):-'))
for i in range(len(k)):
    k[i] = k[i] * j


plot(4,t,k,'post',min(t))
mt.title('h(t)')

plot(5,t,k,'pre',min(t))
mt.xticks([])
mt.yticks([])
mt.ylabel('')
plot(6,t,k,'pre',min(t))
mt.xticks([])
mt.yticks([])

"""p(t) * h(t) convolution"""
output = np.convolve(A1,k)
output = list(output)
output.pop(0)
output.pop(-1)
t3 = list(range(0,len(output)))
print('The convolution is ',output)
fig.add_subplot(3, 1, 3)
mt.plot(t3,output)
mt.grid(True, which='both')
mt.ylabel("Gain ")
mt.xlabel("Time ")
mt.title('convolution')
print('Made by varad patil')
mt.show()

