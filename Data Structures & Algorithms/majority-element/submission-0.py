class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       # naive: count frequency of all elements in array, return element when count > floor(n / 2)
       # time = O(n)
       # space = O(n)

       # sort -> count streaks, return when streak > floor(n / 2) -> O(nlogn) time, O(logn) space
       count = defaultdict(int)
       for num in nums:
         count[num] += 1
         if count[num] > len(nums) / 2:
            return num
       return -1