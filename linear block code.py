"""linear code error detection and correction experiment"""

import numpy as np
from tabulate import tabulate
import pandas as pd

def convert(x):
    values = []
    for i in range(len(x)):
        v = int(x[i])
        values.append(v)
    return values

def generate_data_matrix(k, intial):
    """Generation of data matrix"""
    arr = 2 ** k
    a = []
    for i in range(intial, arr):
        b = bin(i)
        b = b[2:]
        b = b.zfill(k)
        a.append(list(b))
    data = np.array(a, dtype=int)
    return data

def generator_parity(parity):
    """Generation of parity matrix"""
    p = generate_data_matrix(parity, 0)
    p = list(map(list, p))
    p_matrix = p.copy()
    for i in range(len(p)):
        ones = list(p[i]).count(1)
        if ones < parity - 1:
            p_matrix.remove(p[i])
    return p_matrix

def generator_matrix(n, k):
    """Generation of generator matrix"""
    I = np.identity(k, dtype=int)
    parity = n - k
    p_matrix = generator_parity(parity)
    I = list(map(list, I))
    I_copy = I.copy()
    p = p_matrix.copy()
    emp = []
    empI = []
    for j in range(len(p)):
        if p[j].count(1) >= 2:
            emp.append(p[j])

    form = input('Enter the generator matrix format:-')
    if 'PI' == form.upper():
        print('The generator matrix is in PI')
        print()

        for i in range(k):
            num_of_ones = list(I_copy[i]).count(1)
            if num_of_ones == 1:
                a = emp[i] + I_copy[i]
                empI.append(a)
                p_matrix.remove(p[i])

    elif 'IP' == form.upper():
        print('The generator matrix is in IP')
        print()

        for i in range(k):
            num_of_ones = list(I_copy[i]).count(1)
            if num_of_ones == 1:
                a = I_copy[i] + emp[i]
                empI.append(a)
                p_matrix.remove(p[i])
    I1 = np.array(empI)
    return I1, emp, form

def generator2(h,k):
    f = check_form(h, parity)
    s = Extract(h, k, f)
    I = np.identity(k, dtype=int)
    I = list(map(list, I))
    I_copy = I.copy()
    empI = []
    if 'PI' == f.upper():
        for i in range(k):
            a = s[i] + I_copy[i]
            empI.append(a)
        return empI
    elif 'IP' == form.upper():
        for i in range(k):

            a = I_copy[i] + s[i]
            empI.append(a)
        return  empI,f

def H_matrix(p,form):
    pt = np.transpose(p)
    I = np.identity(n - k, dtype=int)
    I = list(map(list, I))
    pt= list(map(list, pt))
    P = pt.copy()
    I_copy = I.copy()
    empI = []
    if 'PI' == form.upper():
        for i in range(n-k):
            a =  I_copy[i] + P[i]
            empI.append(a)
        print()
    elif 'IP' == form.upper():
        for i in range(n-k):
            a = P[i] + I_copy[i]
            empI.append(a)
        print()
    return empI

def code_generation(data,g):
    """code matrix generation"""
    drow = data.shape[0]
    gcol = g.shape[1]

    global C

    if data.shape[1] == g.shape[0]:
        C = np.zeros((data.shape[0], g.shape[1]), dtype=int)
        for row in range(drow):
            for col in range(gcol):
                for elt in range(len(g)):
                    C[row, col] ^= data[row, elt] * g[elt, col]
        return C
    else:
        return "Sorry, cannot multiply A and B."

def words(data,form,a):
    """genearte words"""
    emp = []
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    for i in range(1, data + 1):
        if k == data and a.upper() =='D':
            emp.append('D' + str(i).translate(SUB))
        elif n - k == data and a.upper() =='S':
            emp.append('S' + str(i).translate(SUB))
        elif n - k == data and a.upper() == 'P':
            emp.append('P' + str(i).translate(SUB))
        elif n == data and a.upper() =='C':
            emp.append('C' + str(i).translate(SUB))
        elif n == data and a.upper() == 'e':
            emp.append('e' + str(i).translate(SUB))
    if 'IP' == form.upper():
        emp = sorted(emp, reverse=True)
    return emp

def check_form(g1,a):
    global form
    s1 = [item[-a:] for item in g1]
    s2 = [item[:a] for item in g1]
    s1 = list(map(list, s1))
    s2 = list(map(list, s2))
    I = np.identity(a, dtype=int)
    I = list(map(list, I))

    if a == k:
        for i in range(len(I)):
            for j in range(len(g1)):
                if s1[j] == I[i]:
                    form = 'pi'
                elif s2[j] == I[i]:
                    form = 'ip'
    else:
        for i in range(len(I)):
            for j in range(len(g1)):
                if s1[j] == I[i]:
                    form = 'ip'
                elif s2[j] == I[i]:
                    form = 'pi'
    return form

def Extract(lst, parity, form):
    """extract the parity matrix"""

    if parity == n-k:
        if 'IP' == form.upper():
            print('The generator matrix is in IP')
            s = [item[-parity:] for item in lst]
            return s

        elif 'PI' == form.upper():
            print('The generator matrix is in PI')
            s = [item[0:parity] for item in lst]
            return s
    else:
        if 'IP' == form.upper():
            print('The generator matrix is in IP')
            s = [item[0:parity] for item in lst]
            s = np.transpose(s)
            s = list(map(list,s))
            return s
        elif 'PI' == form.upper():
            print('The generator matrix is in PI')

            s = [item[-parity:] for item in lst]
            s = np.transpose(s)
            s = list(map(list, s))
            return s

def display(data,a):
    """displaying the data"""
    if dict != type(data):
        data = np.array(data)
        data = np.transpose(data)
        D = words(len(data), form,a)
        data = list(map(list,data))
        data = dict(zip(D, data))
    df = pd.DataFrame(data)
    df = tabulate(df, headers='keys', tablefmt='fancy_grid')
    return df, data

def decoding(n,h):
    emp = []
    s = [1] + [0]*(n-1)
    for i in range(n):
        a = np.roll(s,i)
        a = list(a)
        emp.append(a)
    emp.append([0]*n)
    ht = np.transpose(h)
    ht = list(map(list,ht))
    a = [0]*parity
    ht.append(a)
    return emp, ht

def syndrome(h,e,c1):

    global s
    c1 = list(map(list,c1))
    r = list(input('Enter the recieved code:-'))
    r = convert(r)
    ht = np.transpose(h)
    ht = list(map(list,ht))
    s= []
    emp =[]
    for i in range(len(r)):
        if r[i] == 1:
           s.append(ht[i])
    list1 = [0]*len(ht[0])

    for i in range(len(s)):
        list2 = s[i]
        emp= [a^b for a,b in zip(list1,list2)]
        list1 = emp
    if emp == [0]*parity:
        print('No error')
        return r

    elif emp != [0]*parity:
        err = []
        for i in range(len(ht)):
            if emp == ht[i]:
                err = e[i]
        print('for Syndrome =',string(emp),'the error code is',string(err))

        print('The error is in ',err.index(1)+1,'-bit')
        C = [a^b for a,b in zip(err,r)]
        return C

def string(T):
    st =''
    for i in range(len(T)):
        v = str(T[i])
        st = st + v
    return st

def minimum_weight(c):
    """calculate min hamming weight"""
    num_of_ones = []
    c = list(map(list, c))
    for i in range(len(c)):
        a = list(c[i]).count(1)
        num_of_ones.append(a)
    num_of_ones.remove(0)
    return num_of_ones

def error(ones):
    """Error correction and detectiion capabality"""
    global t

    dmin = min(ones)
    err_detect = dmin - 1
    if dmin%2 == 0:
        print('dmin is an even number')
        t = (dmin - 2)/2
    elif dmin%2 ==1:
        print('dmin is an odd number')
        t = (dmin - 1) / 2
    return err_detect, t

def parity_eqn(p,form):
    """generate parity eqn"""

    result = []
    last = []
    emp = words(k,form,'d')
    parity = words(n-k,form,'p')
    p = np.array(p)
    p = np.transpose(p)
    emp1 = list(map(list, p))

    for j in range(p.shape[0]):
        b = emp1[j]
        a = [item1 * item2 for item1, item2 in zip(emp, b)]
        a1 = a.copy()
        for i in range(len(a)):
            if '' == a[i]:
                a1.pop(i)
        result.append(a1)
    for j in range(len(result)):
        a = result[j]
        res = '+'.join(str(a[i]) for i in range(len(result[j])))
        last.append(res)
    parity1 = dict(zip(parity, last))
    return parity1, emp

print('''plz select what you want to do:-
         1 = to use the genearator and data matrix which is there
         2 = to create a new generator and data matrix 
         3 = to enter the values of generator and data matrix from the user
         4 = to enter the values of H matrix and data matrix ''')
print('\n')
q = int(input('Enter the option number you want: -'))
print()
global n, k, initial, data, g, p,form,h,decode,d,ones,err_detect,rate,final,c,t,eqn,c1
if 1 == q:
    print('''which linear code you want of (6,3) or (7,4)
             Enter a for (6,3)
             Enter b for another(6,3)
             Enter c for (7,4)''')

    a = input('Enter linear code : -')

    if a.lower() == 'a':
        g = [[1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1]]
        k = 3
        intial = 0
        n = 6
        data = generate_data_matrix(k, intial)
        parity = n - k
        p = Extract(g, parity, 'ip')
        g = np.array(g)
        form = 'ip'
        h = H_matrix(p, form)
        rate = round(k / n, 2)
        c = code_generation(data, g)
        c1 = c.copy()
        ones = minimum_weight(c)
        err_detect, t = error(ones)
        eqn, D = parity_eqn(p, form)
        data, dict1 = display(data,'d')
        c, dict2 = display(c,'c')
        merge = dict1 | dict2
        final, _ = display(merge,'q')
        decode, ht = decoding(n, h)
        a, b = display(decode,'e')
        a1, b1 = display(ht,'s')
        di = b | b1
        d, _ = display(di,'_')
    elif a.lower() == 'b':
        n = 6
        k = 3
        parity = n - k
        d = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
        g = [[1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1]]
        g1 = g.copy()
        form = check_form(g1, k)
        print('The generator matrix is in', form.upper(), 'form\n')
        p = Extract(g, parity, form)
        data = np.array(d)
        g = np.array(g)
        h = H_matrix(p, form)
        rate = round(k / n, 2)
        c = code_generation(data, g)
        ones = minimum_weight(c)
        err_detect, t = error(ones)
        eqn, D = parity_eqn(p, form)
        data, dict1 = display(data,'d')

        c, dict2 = display(c, 'c')
        merge = dict1 | dict2
        final, _ = display(merge, 'q')
        decode, ht = decoding(n, h)
        a, b = display(decode, 'e')
        a1, b1 = display(ht, 's')
        di = b | b1
        d, _ = display(di, '_')

    elif a.lower() == 'c':
        k = 4
        intial = 0
        n = 7
        data = generate_data_matrix(k, intial)
        g = [[1, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 0]]
        parity = n - k
        p = Extract(g, parity, 'ip')
        g = np.array(g)
        form = 'ip'
        h = H_matrix(p, form)
        rate = round(k / n, 2)
        c = code_generation(data, g)
        ones = minimum_weight(c)
        err_detect, t = error(ones)
        eqn, D = parity_eqn(p, form)
        data, dict1 = display(data, 'd')
        c, dict2 = display(c, 'c')
        merge = dict1 | dict2
        final, _ = display(merge, 'q')
        decode, ht = decoding(n, h)
        a, b = display(decode, 'e')
        a1, b1 = display(ht, 's')
        di = b | b1
        d, _ = display(di, '_')

elif 2 == q:

    n, k = map(int, input('Enter the number of  code bit and data bit:-').split())
    print('The linear code is of ','(',n,',', k,')')
    intial = int(input('enter The starting  decimal number:-'))
    data = generate_data_matrix(k, intial)
    g, p, form = generator_matrix(n, k)
    rate = round(k / n, 2)
    c = code_generation(data, g)
    ones = minimum_weight(c)
    err_detect, t = error(ones)
    eqn, D = parity_eqn(p, form)
    data, dict1 = display(data, 'd')
    c, dict2 = display(c, 'c')
    merge = dict1 | dict2
    final, _ = display(merge, 'q')
    decode, ht = decoding(n, h)
    a, b = display(decode, 'e')
    a1, b1 = display(ht, 's')
    di = b | b1
    d, _ = display(di, '_')

elif 3 == q:

    n, k = map(int, input('Enter the number of  code bit and data bit:-').split())
    print('The linear code is of ', '(', n, ',', k, ')')
    print("\n")
    d = [input('Enter the data matrix with space :-').split() for _ in range(2**k)]
    g_matrix = [input('Enter the generator matrix with space :-').split() for _ in range(k)]

    data = []
    g = []
    parity = n - k
    for i in range(len(d)):
        a = convert(d[i])
        data.append(a)

    for i in range(len(g_matrix)):
        a = convert(g_matrix[i])
        g.append(a)

    g1 = g.copy()
    form = check_form(g1,k)
    print('The generator matrix is in', form.upper(), 'form\n')
    p = Extract(g, parity, form)
    data = np.array(data)
    g = np.array(g)
    rate = round(k / n, 2)
    c = code_generation(data, g)
    ones = minimum_weight(c)
    err_detect, t = error(ones)
    eqn, D = parity_eqn(p, form)
    data, dict1 = display(data, 'd')
    c, dict2 = display(c, 'c')
    merge = dict1 | dict2
    final, _ = display(merge, 'q')
    decode, ht = decoding(n, h)
    a, b = display(decode, 'e')
    a1, b1 = display(ht, 's')
    di = b | b1
    d, _ = display(di, '_')

elif 4 == q:

    n, k = map(int, input('Enter the number of  code bit and data bit:-').split())
    print('The linear code is of ', '(', n, ',', k, ')')
    parity = n - k
    d = [input('Enter the data matrix with space :-').split() for _ in range(2 ** k)]
    h_matrix = [input('Enter the H matrix with space :-').split() for _ in range(parity)]
    h = []
    for i in range(len(h_matrix)):
        a = convert(h_matrix[i])
        h.append(a)
    g2, form = generator2(h, k)
    print('The Generator matrix is in', form.upper(), 'form\n')
    g = np.array(g2)
    print()
    data = []
    for i in range(len(d)):
        a = convert(d[i])
        data.append(a)
    data = np.array(data)
    rate = round(k / n, 2)
    c = code_generation(data, g)
    ones = minimum_weight(c)
    err_detect, t = error(ones)
    eqn, D = parity_eqn(p, form)
    data, dict1 = display(data, 'd')
    c, dict2 = display(c, 'c')
    merge = dict1 | dict2
    final, _ = display(merge, 'q')
    decode, ht = decoding(n, h)
    a, b = display(decode, 'e')
    a1, b1 = display(ht, 's')
    di = b | b1
    d, _ = display(di, '_')
g = tabulate(g, tablefmt='fancy_grid')
p = tabulate(eqn.items(), headers=['PARITY', 'DATA'], tablefmt='fancy_grid')

print('--'*100, end='\n')
print('The DATA MATRIX IS :-')
print(data)
print('--'*100, end='\n')
print('The GENERATOR MATRIX IS ')
print(g)
print('--'*100, end='\n')
print('The CODE is :-')
print(c)
print('The minimum Hamming weight is = ', min(ones))
print('The error detection capability :- ', err_detect)
print('The error correction capability :- ', t)
print('The Code rate is', rate)
print('The Code efficiency is ', round(rate*100, 2))
print('The Parity eqn are')
print(p)
print('The final table is :- ')
print(final)
h1 = tabulate(h, tablefmt='fancy_grid')
print('--' * 50, end='\n')
print('The H MATRIX IS :-')
print(h1)
print('The Decoding Table is')
print(d)
i = 0
while i < 3:
    r = syndrome(h, decode,c1)
    print('The recieved Code is', string(r))
    i = i + 1
    print('--' * 50, end='\n')
print('Made by varad patil')