class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m, n = len(strs), len(strs[0]) # 4, 3
        res = []
        # iterate over vertical slices of strings, one index for each string at a time
        for i in range(n):
            cur = strs[0][i]
            for j in range(1, m):
                s = strs[j]
                # current string terminated, cannot match anymore
                # or char doesn't match
                if len(s) <= i or s[i] != cur:
                    return "".join(res)
            # build onto matched prefix
            res.append(cur)

        return "".join(res)

# should our solution be case-sensitive? THE INPUT IS ONLY LOWERCASE LETTERS IF NON-EMPTY


'''
0 1 2 3
b a t
b a g
b a n k
b a n d
'''