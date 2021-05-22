import numpy as np

# numpy的基础运算
a = np.array([10, 20, 30, 40])
b = np.arange(4)

print(a, b)
c = a * b
print(c)

# 求平方
c1 = a ** 2
print(c1)

c2 = 10 * np.sin(a)
print(c2)

print(b, b < 3)

a1 = np.array([[1, 1],
               [0, 1]])
b1 = np.arange(4).reshape((2, 2))
print(a1)
print(b1)
# 对应位置元素相乘
c3 = a * b
print('c3=', c3)

# 矩阵乘法
c4 = np.dot(a, b)
c5 = a.dot(b)
print('c4=', c4)
print('c5=', c5)

d = np.random.random((2, 4))
print(d)

# axis = 0 列数求和 axis=1 行数求和
print(np.sum(d, axis=1))
print(np.sum(d, axis=0))
print(np.max(d))
print(np.min(d))
