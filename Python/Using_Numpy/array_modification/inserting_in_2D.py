import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
new_arr= np.insert(arr,2,[7,8], axis= 1)
print(new_arr)