class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False


'''
possible questions:
 - is nums sorted?
'''

'''
nums = [1,2,3,3]
seen = {1,2,3}

return True
'''