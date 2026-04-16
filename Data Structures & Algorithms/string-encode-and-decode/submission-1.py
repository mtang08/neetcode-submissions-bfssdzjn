class Solution:

    def encode(self, strs: List[str]) -> str:
        # define a delimiter that tells decode how many chars to read before creating new string
        # delimiter = <num_chars>#
        # time: O(n) where n is number of chars in strs
        # space: O(n)
        res = []
        for s in strs:
            n = len(s)
            res.append(str(n))
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # time: O(n) where n is len(s)
        # space: O(m) auxiliary where m is length of longest string, O(n) for output
        res = []
        # first part of string will be delimiter with number to read
        idx, n = 0, len(s)
        while idx < n:
            # decode the delimiter
            delim = 0
            while s[idx] != '#':
                delim = delim * 10 + int(s[idx])
                idx += 1
            # skip the #
            idx += 1

            # decode the string and append
            res.append(s[idx:idx + delim])
            idx += delim

        return res