class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count the char frequencies of string s
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        
        # iterate over chars in t, decrement on match
        for c in t:
            if c not in count:
                return False
            count[c] -= 1
        
        for c, freq in count.items():
            if freq != 0:
                return False

        return True