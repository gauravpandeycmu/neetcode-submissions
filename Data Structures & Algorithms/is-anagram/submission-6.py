class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            map1[s[i]] += 1
            map2[t[i]] += 1
        return map1==map2
