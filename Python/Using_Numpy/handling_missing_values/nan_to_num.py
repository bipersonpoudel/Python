import numpy as np
arr=np.array([1,2,3,4,np.nan])
print(np.isnan(arr))
print(np.nan_to_num(arr, nan=1))