# BUBBLE SORT
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    return nums


nums = [int(x) for x in input('enter list of numbers\n').split()]
print('sorted list',sort(nums))
