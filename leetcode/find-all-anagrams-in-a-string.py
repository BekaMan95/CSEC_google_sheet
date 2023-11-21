class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        out = []
        start = 0
        end = 0
        psw = sorted([x for x in p])
        while end < len(s):
            end = start + len(p)
            if psw == sorted([x for x in s[start:end]]):
                out.append(start)
            start += 1
        return out
