# Given an integer array nums, move all 0s to the end of the array while maintaining the 
# relative order of the non-zero elements.

# You must modify nums in place.

# Input:
# nums = [0, 1, 0, 3, 12]

# Output:
# [1, 3, 12, 0, 0]
# Input:
# nums = [0]

# Output:
# [0]

def move_zeroes(nums):
    # dont want to make a new array. inefficient.
    zero_count = 0

    i = 0
    looking = 0
    while i < len(nums):
        # if were into the zero zone
        if i >= (len(nums) - zero_count):
            return fill_zeroes(nums, i, zero_count)
            
        else:
            if nums[looking] == 0:
                # look to next
                # find next nonzero item
                while nums[looking] == 0:
                    zero_count += 1
                    looking += 1

                    #exit loops if outside of array indices
                    if looking not in range(len(nums)):
                        return fill_zeroes(nums, i, zero_count)

                # once we have found next non zero
                nums[i] = nums[looking]

                looking += 1
            else:
                # if the one were alreadying looking at isnt zero thats the next value in array (no need to look furhter)
                nums[i] = nums[looking]
                looking += 1
            
        i += 1
    
    return nums

def fill_zeroes(nums, start, zero_count):
    for i in range(start, len(nums), 1):
        nums[i] = 0

    return nums
            
nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))