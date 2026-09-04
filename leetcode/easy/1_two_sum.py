# Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.

# Assume exactly one valid answer exists, and you can’t use the same element twice.

def two_sum(nums, target):
    #store num as key index as value
    seen_compliments = {}
    index = 0

    for num in nums:
        compliment = target - num

        if num in seen_compliments:
            return [seen_compliments[num], index]

        seen_compliments[compliment] = index
        
        index += 1


nums = [3, 4, 2, 7]
target = 6

print(two_sum(nums, target))
