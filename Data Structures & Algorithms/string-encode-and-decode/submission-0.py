class Solution:

    def encode(self, strs: List[str]) -> str:
        # define a delimiter that tells decode how many chars to read before creating new string
        # delimiter = <num_chars>#
        res = []
        for s in strs:
            n = len(s)
            res.append(str(n))
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
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
            cur = []
            for i in range(idx, idx + delim):
                cur.append(s[i])
            res.append("".join(cur))
            idx += delim

        return res