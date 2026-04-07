class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (2 * n)
        for i, num in enumerate(nums):
            res[i] = num

        for i, num in enumerate(nums):
            res[i + n] = num

        return res

'''
[1,4,1,2]
       0 1 2 3 4 5 6 7
res = [1,4,1,2,1,4,1,2]
'''