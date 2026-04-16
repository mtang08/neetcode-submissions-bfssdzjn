class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a, b):
            m, n = len(a), len(b)
            i, j = 0, 0
            res = []
            while i < m and j < n:
                if a[i] <= b[j]:
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

        
        def mergeSort(arr):
            n = len(arr)
            # base case: single element list
            if n < 2:
                return arr
            
            # creates copies of slices of lists -> could use idx to partition the lists

            a = mergeSort(arr[:n//2])
            b = mergeSort(arr[n//2:])
            return merge(a, b)

        return mergeSort(nums)
'''
merge sort
1. split into single element lists
[5,10,2,1,3]
[5,10] [2,1,3]
[5][10] [2][1,3]
[5][10] [2] [1][3]

2. merge in ascending order
[5,10] [2] [1,3]
[5,10] [1,2,3]
[1,2,3,5,10] -> DONE
'''

'''
dry run code
0     arr = [5,10,2,1,3]
1a    arr = [5,10]           1b    arr = [2,1,3]
2a    arr = [5]              2b    arr = [10] -> [5,10]
2ba   arr = [2]              2bb   arr = [1,3]
                             3ba, 3bb arrs = [1],[3] -> [1,3]
a = [2], b = [1,3] -> [1,2,3]
a = [5,10], b = [1,2,3] -> [1,2,3,5,10]
'''