import numpy as np

A = np.array([1, 1, 1])[np.newaxis, :]
B = np.array([2, 2, 2])[np.newaxis, :]
print('A=', A)
print('B=', B)

# 上下合并
C = np.vstack((A, B))
print(C)  # vertical stack

# 左右合并
D = np.hstack((A, B))  # horizontal stack
print(D)

print(A.shape, C.shape)

# 矩阵变换
# print(A[np.newaxis, :].shape)
# print(A[:, np.newaxis].shape)

E = np.concatenate((A, B, B, A), axis=1)
print(E)

F = np.array([1, 1, 1])[np.newaxis, :]
G = np.array([1, 1, 1])[:, np.newaxis]
print(F)
print(G)

