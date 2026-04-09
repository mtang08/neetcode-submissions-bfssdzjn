class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # option 1: use map of sorted string -> list of anagrams
        # time = n*mlog(m)

        # option 2: count frequency of characters in each string -> encode as string
        # map of encoded frequency -> list of anagrams
        # time = n*m
        anagrams = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            encoded = []
            for freq in count:
                encoded.append(str(freq))
            key = "#".join(encoded)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)

        return [sublist for sublist in anagrams.values()]
