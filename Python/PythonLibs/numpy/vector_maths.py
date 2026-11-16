import numpy as np

nums_py_list = [30,25,26,35] # 120
mul3_nums = nums_py_list * 3
print(mul3_nums)


print(nums_py_list)
marks = np.array(nums_py_list) # 120
print(marks)
marks_plus_5 = marks+5 
print(marks_plus_5)
print(marks)


marks_percent = ((marks/120)*100).round(2)
print(marks_percent)

print(marks.mean())
print(marks.max())
print(marks.min())
print(marks.std())

mask_gt_30 = marks >= 30
print(type(mask_gt_30))
print(mask_gt_30)# boolean mask
print(marks[mask_gt_30])