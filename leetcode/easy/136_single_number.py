# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find and return the element that appears only once.

# Input:
# nums = [4, 1, 2, 1, 2]

# Output:
# 4

def single_number(nums):
    appearances = set()

    # it has to iterate the whole array because otherwise it cant know it appears once. 
    # could we go from both ends to reduce time? nah then were just doing same operation twice per loop lol
    #sets kinda suck  because we could have one value left (the single) and wed have to do a tiny iteration to grab it?

    for num in nums:
        if num in appearances:
            appearances.remove(num)
        else:
            appearances.add(num)

    for single in appearances:
        return single


nums = [4, 1, 2, 1, 2]
print(single_number(nums))