# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the 
# elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using division.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 100000
# -30 <= nums[i] <= 30



def product_of_array_except_self_lol(nums):
    #the pproblem here is a.) easiest way is division, calculate total product divide by current i, 
        #in terms of loops atleast that gives O(n)
    #otherwise you want to just brute force by nesting a loop

    #its just O(n) time not space so finding a way of generating another constant that enables a single 
    #   non-nestedloop is what i see immediately
    #unless theres another way to loop through differently related data. O(n) doesnt preclude looping through twice
        #we just cant nest.

    #XOR? could XOR each thing but you still have to recalculate and multiply every number by either a 0 or 1 determined each loop

    #I have a hilarious solution

    reciprocals = {
        -30: -0.03333333333333333,
        -29: -0.034482758620689655,
        -28: -0.03571428571428571,
        -27: -0.037037037037037035,
        -26: -0.038461538461538464,
        -25: -0.04,
        -24: -0.041666666666666664,
        -23: -0.043478260869565216,
        -22: -0.045454545454545456,
        -21: -0.047619047619047616,
        -20: -0.05,
        -19: -0.05263157894736842,
        -18: -0.05555555555555555,
        -17: -0.058823529411764705,
        -16: -0.0625,
        -15: -0.06666666666666667,
        -14: -0.07142857142857142,
        -13: -0.07692307692307693,
        -12: -0.08333333333333333,
        -11: -0.09090909090909091,
        -10: -0.1,
        -9: -0.1111111111111111,
        -8: -0.125,
        -7: -0.14285714285714285,
        -6: -0.16666666666666666,
        -5: -0.2,
        -4: -0.25,
        -3: -0.3333333333333333,
        -2: -0.5,
        -1: -1.0,
        0: None,
        1: 1.0,
        2: 0.5,
        3: 0.3333333333333333,
        4: 0.25,
        5: 0.2,
        6: 0.16666666666666666,
        7: 0.14285714285714285,
        8: 0.125,
        9: 0.1111111111111111,
        10: 0.1,
        11: 0.09090909090909091,
        12: 0.08333333333333333,
        13: 0.07692307692307693,
        14: 0.07142857142857142,
        15: 0.06666666666666667,
        16: 0.0625,
        17: 0.058823529411764705,
        18: 0.05555555555555555,
        19: 0.05263157894736842,
        20: 0.05,
        21: 0.047619047619047616,
        22: 0.045454545454545456,
        23: 0.043478260869565216,
        24: 0.041666666666666664,
        25: 0.04,
        26: 0.038461538461538464,
        27: 0.037037037037037035,
        28: 0.03571428571428571,
        29: 0.034482758620689655,
        30: 0.03333333333333333
    }

    product_total = 1
    zero = None
    multiple_zeroes = False

    for i in range(len(nums)):
        if nums[i] == 0:
            if zero != None:
                #we have multiple zeroes oh no!
                multiple_zeroes = True

            zero = i
        else:
            product_total *= nums[i]

    products = []
    for i in range(len(nums)):
        if multiple_zeroes:
            products.append(0)
        else:
            if zero != 69420:
                if i != zero:
                    products.append(0)
                else:
                    products.append(product_total)
            else:
                products.append(round(product_total * reciprocals[nums[i]]))

    return products

def product_of_array_except_self(nums):
    product_before = nums.copy()
    product_after = nums.copy()

    before_total = 1
    for i in range(len(nums)):
        product_before[i] = before_total
        before_total *= nums[i]

    after_total = 1
    for i in range(len(nums) - 1, -1, -1):
        product_after[i] = after_total
        after_total *= nums[i]

    products = []
    for i in range(len(nums)):
        products.append(product_before[i] * product_after[i])

    return products



nums = [0,2,0,4]
print(product_of_array_except_self(nums))