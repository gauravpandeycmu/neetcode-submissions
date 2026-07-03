class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapA, mapB = defaultdict(int), defaultdict(int)

        for i in s:
            mapA[i] += 1
        for i in t:
            mapB[i] += 1
        return mapA == mapB
        
