import numpy as np
import pandas as pd

x = [1,2,3,4,5]
y = range(1,6)


print(x)
print(y)

a = np.array(x)
b = np.array(y)

print(a)
print(b)

print(a,type(a))
print(b,type(b))


m = [[1,2,3,4,5],[6,7,8,9,0]]
ma = np.array(m)
print(ma,type(ma))