class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # three pointer approach: swap zeros to the left, twos to the right, do nothing with ones
        # keep pointer to swap destinations for zeros and twos, third pointer to iterate through list
        l, r, cur = 0, len(nums) - 1, 0
        # nums[l] = 0s
        # nums[l:cur] = 1s
        # nums[cur:r+1] = unknown
        # nums[r+1:] = 2s        
        while cur <= r:
            if nums[cur] == 0:
                # swap into zero ptr idx
                nums[cur], nums[l] = nums[l], nums[cur]
                l += 1
                # can increment cur because the swapped element is guaranteed 0 or 1
                # a 2 would've been swapped into position on earlier iteration
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                # swap into two ptr idx
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
                # cannot increment cur because we do not know whether the value swapped
                # into cur idx is a 0 (requires another swap) or 1 (can increment)
                # need to consider cur idx again




'''
# case 1: encounter zero, swap to start
[1,0,1,2]
[0,1,1,2]

[0,1,1,2]
l = 1
c = 3
r = 2

[0,1,2]
l = 1
r = 1
c = 2


# case 2: encounter 2, swap to end
[2,1,0]
[0,1,2]

# case 3: encounter 1, do nothing unless need swap
[2,0,1]
[1,0,2] -> need to reconsider idx 0 after swap -> do nothing
[1,0,2] -> 1 = cur == r, swap 0 into leftmost position
[0,1,2] 



'''