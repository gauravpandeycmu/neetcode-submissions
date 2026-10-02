class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = defaultdict(int)
        adj = [[] for i in range(numCourses)]

        for u, v in prerequisites:
            indeg[v] += 1
            adj[u].append(v)

        q = deque()

        for course in range(numCourses):
            if not indeg[course]:
                q.append(course)

        res = list()
        
        while (q):
            course = q.popleft()
            res.append(course)
            
            for course in adj[course]:
                indeg[course] -= 1
                if not indeg[course]:
                    q.append(course)

        return res[::-1] if len(res)==numCourses else []