class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        max_len = 0
        for i in s:
            if not sub.__contains__(i):
                sub += i
                if max_len < len(sub):
                    max_len = len(sub)
            else:
                sub = sub[sub.index(i)+1:] + i
                if max_len < len(sub):
                    max_len = len(sub)
        return max_len
