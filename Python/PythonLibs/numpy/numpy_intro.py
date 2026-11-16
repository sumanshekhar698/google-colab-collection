import numpy as np

marks = np.array([12,32,54,88,32,80,30,66])
print(type(marks))
print(marks.shape)
print(marks.dtype)
print(marks.ndim)


marks_range = np.array([[23,56],
                        [32, 64],
                        [67,98]])
print(type(marks_range))
print(marks_range.shape)
print(marks_range.dtype)
print(marks_range.ndim)

matrix_3d = np.array([[[22,44,56],[22,44,56],[21,34,4]] , [[22,44,56],[22,44,56],[21,34,4]], [[22,44,56],[22,44,56],[21,34,4]]])
print(matrix_3d)
print(type(matrix_3d))
print(matrix_3d.shape)
print(matrix_3d.dtype)
print(matrix_3d.ndim)

print(np.zeros(10))
print(np.arange(0,30,5))
print(np.linspace(0,1,5))

# mix_array = np.array([23,565,90.5,67])
mix_array = np.array([23,565,90.5,67, "dsds"])
print(mix_array)
print(mix_array.shape)
print(mix_array.dtype)
print(mix_array.ndim)