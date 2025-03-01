class Solution(object):
    def moveZeroes(self, nums):
        l = 0
        temp = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l+=1
        return nums

# Test the function
nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums)) # [1, 3, 12, 0, 0]