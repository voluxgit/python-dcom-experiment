d = int(input('Enter The decimal number:-'))
n = int(input('Enter The length of HRC character:-'))
D = bin(d)
x = D[2:]


def convert(x):
    values = []
    for i in range(len(x)):
        v = int(x[i])
        values.append(v)
    return values


def string(T):
    st =''
    for i in range(len(T)):
        v = str(T[i])
        st = st + v
    return st


def spilt_operation(x):
    x1 = list(x)
    emp =[]
    for i in range(0, len(x), n):
        x = i
        emp.append(x1[x:x + n])
    return emp


def spilt(x):
    if len(x)%n == 0:
        emp = spilt_operation(x)
        return emp
    else:
        if len(x) < n:
            a = 0 + len(x)
            while a < n:
                a +=1
        else:
            a1 = abs(len(x) - n)
            a = abs(n - a1)
            a = len(x) + a
        x2 = x.zfill(a)
        return spilt_operation(x2)


def operation(emp):
    emp_copy = emp.copy()
    list1 = [0]*n
    a1 = []
    for i in range(len(emp_copy)):
        list2 = emp_copy[i]
        a1 = a1 + list2
        list2 = convert(list2)
        parity = list(a^b for a,b in zip(list1, list2))
        list1 = parity
    emp1 = a1 + list1
    T = convert(emp1)
    return T


def check_parity(new):
    check = [0]*n
    for i in range(len(new)):
        a3 = new[i]
        check = list(a ^ b for a, b in zip(check, a3))
    return check, len(check)
#                                                       "TRANSMITTER SIDE"
emp = spilt(x)
T = operation(emp)
print('Transmitted code is', string(T))
print('--'*25)
#                                                           "RECIVER SIDE"
i1 = 0
while i1 < 6:
    r = list(input('Enter the Recieved Code :-'))
    r = convert(r)
    new = spilt_operation(r)
    a, b = check_parity(new)
    if [0]*b == a:
        print('No error')
        T1 = r[:-b]
        print('The data is', string(T1))
    else:
        p = [(i, j) for i, j in zip([0]*b, a) if i != j]
        print('error detected for',len(p),'-bit ')
    i1 += 1
    print('--'*25)
print('made by varad patil 120A2036')