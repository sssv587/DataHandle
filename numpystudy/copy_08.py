import numpy as np

a = np.arange(4)
print(a)

b = a
c = a
d = b

a[0] = 11
print(a)
print(b)
print(c)
print(d)

print(b is a)
print(d is a)

d[1:3] = [22, 33]

print(a)

b = a.copy()  # deep copy 只拷贝数值
a[3] = 44
print(b)
