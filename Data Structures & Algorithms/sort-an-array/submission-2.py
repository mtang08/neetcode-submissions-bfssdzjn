class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, mid, r):
            i, j = l, mid
            res = []
            while i < mid and j < r:
                if arr[i] <= arr[j]:
                    res.append(arr[i])
                    i += 1
                else:
                    res.append(arr[j])
                    j += 1
            while i < mid:
                res.append(arr[i])
                i += 1
            while j < r:
                res.append(arr[j])
                j += 1
            
            arr[l:r] = res

        
        def mergeSort(arr, l, r):
            # base case: single element list
            if r - l < 2:
                return arr
            
            # creates copies of slices of lists -> could use idx to partition the lists
            # calculate new idx instead of creating slice copies
            mid = (r + l) // 2
            mergeSort(arr, l, mid) # left half
            mergeSort(arr, mid, r) # right half
            merge(arr, l, mid, r) # overwrite the values in place in the reference list being passed around

        mergeSort(nums, 0, len(nums))
        return nums
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