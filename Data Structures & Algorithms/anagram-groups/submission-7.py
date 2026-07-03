class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            map[str(sorted(s))].append(s)
        res = []
        for i,j in map.items():
            res.append(j)
        return res
