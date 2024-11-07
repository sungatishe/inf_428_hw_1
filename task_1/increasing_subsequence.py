# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
# 4.

def findLengthOfLCIS(nums):
    res = 1
    max_res = 1
    for i in range(0, len(nums) - 1):
        if nums[i] < nums[i + 1]:
            print("Pre: ", nums[i], "Next: ", nums[i + 1], nums[i] < nums[i + 1])
            res += 1
        else:
            max_res = max(max_res, res)
            res = 1

    return max(max_res, res)


nums = [1, 3, 5, 4, 2, 3, 4, 5]

print(findLengthOfLCIS(nums))
