import sys
import copy

a = [1, 2, [3, 4]]
b = copy.copy(a)
c = copy.deepcopy(a)
d = a
 
print('address of a:', id(a))
print('address of b:', id(b))
print('address of c:', id(c))
print ('address of d:', id(d))
print ('address of 1:', id(1))
print ('address of element 0 in a:', id(a[0]))
print ('address of element 0 in b:', id(b[0]))
print ('address of element 0 in c:', id(c[0]))
print ('a=', a)
print ('b=', b)
print ('c=', c)
print ('d=', d)
 
a[0] = 99
print ('a=', a)
print ('b=', b)
print ('c=', c)
print ('d=', d)
 
print('address of element 0 in a:', id(a[0]))
print('address of element 0 in b:', id(b[0]))
print('address of element 0 in c:', id(c[0]))
 
print('address of element 2 in a:', id(a[2]))
print('address of element 2 in b:', id(b[2]))
print('address of element 2 in c:', id(c[2]))
 
a[2].append(5)
print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)


def run(param=[]):
    print('address of param:', id(param))
    param.append(1)
    print('reference count of 1:', sys.getrefcount(1))
    return param


print (run(a))
print (run())
print (run())
print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)
 
print('reference count of 1:', sys.getrefcount(1))
n = 1
print('reference count of 1:', sys.getrefcount(1))
del n
print('reference count of 1:', sys.getrefcount(1))