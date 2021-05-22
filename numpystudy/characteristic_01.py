# numpy属性

import numpy as np

# list -> array
array = np.array([[1, 2, 3], [2, 3, 4]])

print(array)

# 维度
print('number of dim:', array.ndim)
# 行数，列数
print('shape:', array.shape)
# 元素个数
print('size:', array.size)
