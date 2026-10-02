class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = defaultdict(int)
        adj = [[] for i in range(numCourses)]

        for prereq in prerequisites:
            indeg[prereq[0]] += 1
            adj[prereq[1]].append(prereq[0])

        q = deque()
        count = 0

        for i in range(numCourses):
            if not indeg[i]:
                q.append(i)
        
        while q:
            course = q.popleft()
            count += 1

            for c in adj[course]:
                indeg[c] -= 1
                if not indeg[c]:
                    q.append(c)
                

        return count==numCourses
