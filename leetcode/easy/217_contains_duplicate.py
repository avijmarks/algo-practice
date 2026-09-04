def contains_duplicate(nums):
    seen = {}
    count = 0
    for num in nums:
        if num in seen:
            return True
        
        seen[num] = count

    return False


print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False