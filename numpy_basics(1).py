import numpy as np

print(np.zeros(13))

jedynka = np.ones(22,dtype=int)

print(jedynka)
print(type(jedynka))

j  = [1,1,1,1,1,1]
print(type(j))

u = np.arange(1,2.7E7,3)
print(u)

k = np.linspace(0,10,num=5)
print(k)

l1 = [5,7,8,9]
l2 = [11,34,5,67]
l3 = [12,22,56,89]

l1 = l1+l2+l3
print(l1)

a = np.array(l1)
b = np.array(l2)
c = np.array(l3)

# a = a+b+c
# print(a)

a = np.concatenate((a,b,c))
print(a)

listaz1 = [[65,4],[34,56]]

macierzm1 = np.array([[2,99],[78,24]])

print(listaz1)
print(macierzm1)

print(listaz1[0])
print(listaz1[0][1])
# print(listaz1[0,1])

print(macierzm1[0])
print(macierzm1[0])
print(macierzm1[0][1])
print(macierzm1[0,1])

#funkcja reshape

pr = np.arange(12)
print(pr)

fp = pr.reshape(3,4)
print(fp)
