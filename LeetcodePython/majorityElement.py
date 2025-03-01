class Solution(object):
    def majorityElement(self, nums):
        count = 0
        ans = -1
        for num in nums:
            if count == 0:
                ans = num
            if ans == num:
                count += 1
            else:
                count -= 1

        return ans

# Test the function
nums = [3,2,3]
print(Solution().majorityElement(nums)) # 3