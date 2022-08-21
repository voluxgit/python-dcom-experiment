import math
def huffman(eg):
    assert(sum(eg.values())) == 1.0 #check wheather the sum of probabilties is 1
    if (len(eg)==2): #now check if there are only two probabilties
        return dict(zip(eg.keys(), ['0', '1'])) #zip will insert 0 and 1 in keys and it is return in the form of dict
    p_prime = eg.copy() #copying the original prob
    a1, a2 = lowest_prob_pair(eg) #get the 2 lowest prob
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = round(p1 + p2,3)
    #print('p_prime',p_prime)
    #print('p_prime[a1 + a2]',p_prime[a1 + a2])

    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2) # then follow the tree in reverse order
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'
    #print(c[a1], c[a2])
    #print('values of c', c)
    return c

def lowest_prob_pair(eg):
    '''Return pair of symbols from distribution  eg with lowest probabilities.'''
    assert(len(eg) >= 2) # Ensure there are at least 2 symbols in the dist.

    sorted_p = sorted(eg.items(), key=lambda x:x[1],reverse=True)
    #eg.items gets the symbols with thier prob(s1:0.01)
    #lambda is a function used with keys to get the sorting of probabilities on position[1](s1,0.01) where 0.01 is on position 1
    #print('sorted',sorted_p)
    #print(sorted_p[-2][0], sorted_p[-1][0])
    return sorted_p[-2][0], sorted_p[-1][0]#return the lowest prob

def descendingorder(eg):
    sorted_p = sorted(eg.items(), key=lambda x: x[1], reverse=True)
    return sorted_p


def entropy(eg):
    x = []
    for k, v in eg.items():
        eg[k] = float(v)
        x.append(eg[k] * math.log2(1 / eg[k]))
    #print(x)
    entropy = sum(x)
    return round(entropy,3)

def codelength(code,prob):
    x=[]
    y=[]
    z=[]
    for k, v in code.items():
        code[k] = len(v)
        x.append(code[k])
    #print('length of the code',x)
    for k, v in prob.items():
        prob[k] = float(v)
        y.append(prob[k])
    #print('prob of the code',y)
    for i in range(0,len(code)):
        z.append(x[i]*y[i])
    length = sum(z)
    return float(round(length,3))

def code_rate(u,v):
    eff = u/v
    return round(eff,3)
#a  = {'a':0.25,'b':0.25,'c':0.25,'d':0.25}
n =int(input('Enter the numbers of the symbols:-'))
a = dict(input("Enter symbols and Probabilities: ").split() for _ in range(n))
for k, v in a.items():
    a[k] = float(v)
print('our Input sequence is',a)
s = dict(descendingorder(a))
final = huffman(a)
print('The descending order of sequence = ',descendingorder(a))
print('The huffman code of the sequence is:-',huffman(a))
x = entropy(a)
print('The entropy = ',x)
y = codelength(final,s)
print('The Average code length =',y)
rate = code_rate(x,y)
print('The code rate is',rate)
print('The efficiency is', rate*100,'%')
print('The code redundancy is',round((1-rate)*100,3),'%')
print('Made by Varad Patil 120A2036')















