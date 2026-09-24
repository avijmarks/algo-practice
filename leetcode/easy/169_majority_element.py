# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than n // 2 times. 
# You may assume that a majority element always exists.

# Input:
# nums = [3, 2, 3]

# Output:
# 3
# Input:
# nums = [2, 2, 1, 1, 1, 2, 2]

# Output:
# 2

def majority_element_first(nums):
    counts = {}

    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1

    half = len(nums) // 2
    for num in counts:
        if counts[num] > half:
            return num


def majority_element(nums):
    # how do i instantaite this without accidentally affecting output though
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

        
nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))