def comparator(nums):
    # а это тоже множество но с уникальными значениями)
    newnums = set(nums)
    # теперь сравниваем их длинну
    if len(newnums) == len(nums):
        return False
    else:
        return True
# наше множество чисел в массиве
nums = [1,2,3,4,5,1]
nums1 = [1,2,3,4,5,6]
nums2 = [1,1,1,2,3,4,2]

print(comparator(nums), comparator(nums1), comparator(nums2))