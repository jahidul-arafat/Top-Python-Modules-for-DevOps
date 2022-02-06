import numpy as np
import pandas as pd
# Creating array object
arr = np.array([ 1, 2, 3, 4, 5])

# create a pandas series s2. Make sure your array is 1-Dimensional
s2 = pd.Series(arr)

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

# Print S2- Pandas Series
print(s2)

# Print type of S2
print(type(s2))
