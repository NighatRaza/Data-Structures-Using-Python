# SELECTION SORT
def sort(nums):
    for i in range(len(nums)-1):
        minpos=i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
    return nums

nums = [int(x) for x in input('enter numbers\n').split()]
print('sorted list',sort(nums))