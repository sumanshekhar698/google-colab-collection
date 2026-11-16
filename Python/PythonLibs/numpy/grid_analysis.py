import numpy as np



scores = np.array([
    [80, 75, 90, 85],   # Student A
    [60, 70, 65, 72],   # Student B
    [95, 88, 92, 98],   # Student C
])

print(scores.ndim)
print(scores)
print(scores.mean())
print(scores.mean(axis=0).round(2)) # column wise mean
print(scores.mean(axis=1).round(2)) # row wise mean

print(scores[2,1])