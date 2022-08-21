
from operator import ixor
import functools as f


def sum(values):
    parity = f.reduce(ixor,values)
    return parity


def convert(x):
    values = []
    for i in range(len(x)):
        v = int(x[i])
        values.append(v)
    return values


def string(c):
    st = ''
    for i in range(len(c)):
        v = str(c[i])
        st = st + v
    return st


d = int(input('Enter The decimal number:-'))
D = bin(d)
x = D[2:]
print('binary of ', d, 'is', x)
a = len(x)
x = list(x)
values = convert(x)
parity = sum(values)
values.append(parity)
C = values
print('Transmitted Code', string(C))

print('--'*25)
R = list(input('Enter the Recieved Code :-'))
Exor = convert(R)
print('Recieved Code', Exor)
s = sum(Exor)

print('--'*25)
if s == 0:
    print('No error')
    T = Exor[:a]
    print('The data is', string(T))
elif s == 1:
    print('1 bit error detected')


print('made by Varad Patil 120A2036')
