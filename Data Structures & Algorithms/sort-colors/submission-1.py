class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # naive: count frequency of each number and overwrite in nums array
        # time: O(n)
        # space: O(n)

        # optimized three pointer: track first non-zero index and last non-two index as bounds
        # then iterate with third pointer to swap into place
        # if encounter a 0, swap into 0 pointer and inc both idx and left
        # if encounter a 2, swap into 2 pointer and dec
        n = len(nums)
        left, right = 0, n - 1

        # initialize pointers
        while left < right and (nums[left] == 0 or nums[right] == 2):
            if nums[left] == 0:
                left += 1
            if nums[right] == 2:
                right -= 1
        idx = left # iterate through elements to swap into place     
        while idx <= right and left < right:
            if nums[idx] == 1:
                idx += 1
            elif nums[idx] == 0:
                # swap into left index
                nums[idx], nums[left] = nums[left], nums[idx]
                left += 1
                # can inc because value swapped in is guaranteed to not be a 2
                # due to earlier iterations sorting this already
                # -> nums[left] does not need to be considered again
                idx += 1
            elif nums[idx] == 2:
                # swap into right index
                nums[idx], nums[right] = nums[right], nums[idx]
                right -= 1
                # cannot inc idx because unknown what was swapped from right 
'''
nums = [1,0,1,2]

left  = 0
right = 2
idx   = 1

nums = [1,0,2]
left  = 0
right = 1
idx   = 1
'''