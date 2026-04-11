class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # take in two sorted lists, return merged sorted list
        def merge(a, b):
            m, n = len(a), len(b)
            if m == 0:
                return b
            if n == 0:
                return a
            
            # two pointer approach
            res = []
            i, j = 0, 0
            while i < m and j < n:
                if a[i] < b[j]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            while i < m:
                res.append(a[i])
                i += 1
            while j < n:
                res.append(b[j])
                j += 1
            return res

        # recursively call itself to break into smaller sublists
        def mergeSort(unsorted):
            n = len(unsorted)
            # base case: cannot split any smaller
            if n < 2:
                return unsorted
            a, b = unsorted[:n // 2], unsorted[n // 2:]
            a = mergeSort(a)
            b = mergeSort(b)
            return merge(a, b)

        return mergeSort(nums)