# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]


def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set.intersection(set1, set2))


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

print(intersection(nums1, nums2))
