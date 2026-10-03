class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        res = 0

        start = 0
        end = 0

        while end<len(s):
            while end<len(s) and s[end] not in temp:
                temp.add(s[end])
                end += 1

            res = max(res, end-start)

            while end<len(s) and s[end] in temp:
                temp.remove(s[start])
                start+=1
                
        return res