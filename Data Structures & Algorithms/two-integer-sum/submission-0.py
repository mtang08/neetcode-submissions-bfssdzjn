class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in idx:
                return [idx[complement], i]
            idx[num] = i
        
        return []
            


# question: is a solution guaranteed to exist? YES
# can there be duplicate elements? YES

'''
nums = [4,5,6], target = 10
idx = {
  4 : 0,
  5 : 1,
}

return [0, 2]
'''