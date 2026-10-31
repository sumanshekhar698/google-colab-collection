fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# for fruit in fruits:
#     print(fruit)


# 0,1,2,3,4,5,6,7,8,9,10
num = 11
# for i in range(num):
#     print(i)


# 3,4,5,6,7,8,9,10
# for i in range(3,num):# start, stop | start is inclusive, stop is exclusive
#     print(i)

#  3 5 7 9
# for i in range(3,num,2):# start, stop, step | start is inclusive, stop is exclusive
#     print(i)


# 11,10,9,8,7,6,5,4,3,2
for i in range(num,1,-1):# negative steps goes from higher to lower
    print(i)


# 11,8,5,2
for i in range(num,1,-3):
    print(i)