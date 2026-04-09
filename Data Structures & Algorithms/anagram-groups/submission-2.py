class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # option 1: use map of sorted string -> list of anagrams
        # time = O(n*mlog(m))

        # option 2: count frequency of characters in each string -> encode as string
        # map of encoded frequency -> list of anagrams
        # time = O(n*m)
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagrams[key].append(s)

        return list(anagrams.values())

# key insight: tuples are hashable in Python