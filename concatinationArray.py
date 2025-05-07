

def getConcatenation(nums):
    n = len(nums)
    ans = [0] * 2 * n

    for i in range(n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]

    return ans

# Example 1
nums1 = [1, 2, 1]
print(getConcatenation(nums1)) # Output: [1, 2, 1, 1, 2, 1]

# Example 2
nums2 = [1, 3, 2, 1]
print(getConcatenation(nums2)) # Output: [1, 3, 2, 1, 1, 3, 2, 1]
