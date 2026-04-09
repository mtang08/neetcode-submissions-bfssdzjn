class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # naive: if nums[i] == val: pop(i), else: i += 1
        # time = O(n^2)

        # key insight: order of elements not equal to val does not matter
        # can shuffle the elements ->
        # l starts at index 0, if we see val, swap to end and pop
        left, end = 0, len(nums)
        while left < end:
            end = len(nums)
            if left == end:
                break
            
            if nums[left] == val:
                nums[left], nums[end - 1] = nums[end - 1], nums[left]
                nums.pop()
            else:
                left += 1
        
        return len(nums)


'''
 0 1 2 3 4
[4,3,2], val = 1
left = 3
end = 3
nums[left] = 2

return len(nums) = 3

[3,2], val = 1
'''