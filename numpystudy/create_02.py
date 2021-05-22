import numpy as np

# array的创建
a = np.array([2, 23, 4], dtype=np.int64)
print(a)
# array的类型
print(a.dtype)

anp = np.array([[2, 23, 4],
                [2, 32, 4]])
print(anp)

a1 = np.zeros((3, 4), dtype=np.int16)
a2 = np.ones((3, 4), dtype=np.int16)
a3 = np.empty((3, 4), dtype=np.int16)
print(a1)
print(a2)
print(a3)

# 生成线段矩阵
a4 = np.arange(10, 20, 2)
print(a4)

# 范围内生成矩阵
a5 = np.arange(12).reshape((3, 4))
print(a5)

# 生成线段
a6 = np.linspace(1, 10, 6)
print(a6)

# 重新生成矩阵
a7 = a6.reshape((2, 3))
print(a7)
