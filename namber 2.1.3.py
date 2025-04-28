# наше множество чисел в массиве
nums = [1,2,3,4,5,1]
# а это тоже множество но с уникальными значениями)
newnums = set(nums)
# теперь сравниваем их длинну
if len(newnums) == len(nums):
    print(False)
else:
    print(True)
