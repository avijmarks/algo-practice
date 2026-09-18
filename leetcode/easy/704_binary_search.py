# Given a sorted array of integers nums and an integer target, return the index of target if it exists. Otherwise return -1.
# Constraint that matters: nums is sorted in ascending order.

def binary_search(nums: list[int], target: int):

    #lol this is definitely not the right way to iterate here hahahaha i might melt me pc
    flag = True

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            right = mid - 1

        if nums[mid] < target:
            left = mid + 1

    return -1

    
            
nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(binary_search(nums, target))

