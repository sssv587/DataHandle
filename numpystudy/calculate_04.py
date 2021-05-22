import numpy as np

A = np.arange(2, 14).reshape((3, 4))

# 最小值的索引
print(np.argmin(A))
print(np.argmax(A))
print(A)

# 求平均值
print(np.mean(A))
print(A.mean())
print(np.average(A))

# 求中位数
print(np.median(A))

# 逐个累加生成的列表
print(np.cumsum(A))

# 每行的连续两个数的差值
print(np.diff(A))

# 非0的数，行，列
print(np.nonzero(A))

# 排序
print(np.sort(A))

# 行列互换
print(np.transpose(A))
print(A.T)
print((A.T).dot(A))

# 小于5变成5，大于9变成9
print(np.clip(A, 5, 9))
