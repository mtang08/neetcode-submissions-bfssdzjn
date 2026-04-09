class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       # naive: count frequency of all elements in array, return element when count > floor(n / 2)
       # time = O(n)
       # space = O(n)

       # sort -> count streaks, return when streak > floor(n / 2) -> O(nlogn) time, O(logn) space
        candidate, count = nums[0], 1
        n = len(nums)
        for i in range(1, n):
            if candidate == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = nums[i]
                count = 1
        return candidate


# key insight: arbitrarily pick a candidate. if it is the majority, then it will outnumber any other number by at least one
# keep track of count, increment if match, decrement if new val. if count = 0, switch candidate to current element 
# time = O(n)
# space = O(1)