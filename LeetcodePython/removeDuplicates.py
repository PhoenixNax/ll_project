class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        l = 1
        for r in range(1,n):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

# Test the solution
nums = [1,1,2]
print(Solution().removeDuplicates(nums)) # 2