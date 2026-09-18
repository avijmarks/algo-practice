# Go with LeetCode #88 — Merge Sorted Array.

# You’re given two integer arrays nums1 and nums2, both sorted in non-decreasing order.

# nums1 has enough extra space at the end to hold all elements from nums2.

# You also get:

# m = number of meaningful elements currently in nums1
# n = number of elements in nums2

# Merge nums2 into nums1 so that nums1 becomes one sorted array.

#The important part: modify nums1 in place.

# Example:

# Input:
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# Output:
# nums1 = [1,2,2,3,5,6]

# Another:

# Input:
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# Output:
# nums1 = [1]

def merge_sorted_array(nums1, m, nums2, n):
    # start at end and go backwards because we have buffer space to avoid overwriting that way?

    # start each at end of useful part of array
    next_nums1 = m - 1
    next_nums2 = n - 1


    for i in range(len(nums1) - 1, -1 , -1):
        if next_nums2 < 0:
            # dump rest of nums 1
            nums1[i] = nums1[next_nums1]
            next_nums1 -= 1
        elif next_nums1 < 0:
            # dump rest of nums 2
            nums1[i] = nums2[next_nums2]
            next_nums2 -= 1
        else:
            if nums1[next_nums1] >= nums2[next_nums2]:
                # nums1 at i is nums1[nextnums1]
                nums1[i] = nums1[next_nums1]
                next_nums1 -= 1
            elif nums1[next_nums1] < nums2[next_nums2]:
                #nums1 at i is nums2[next_nums2]
                nums1[i] = nums2[next_nums2]
                next_nums2 -= 1

    return nums1
        
nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

print(merge_sorted_array(nums1, m, nums2, n))
