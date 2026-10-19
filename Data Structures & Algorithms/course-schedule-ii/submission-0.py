class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0]*numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degrees[course] += 1
        
        queue = deque(i for i in range(numCourses) if in_degrees[i] == 0)

        topological_sort = []
        while queue:
            node = queue.popleft()
            topological_sort.append(node)
            for nxt in graph[node]:
                in_degrees[nxt] -= 1
                if in_degrees[nxt] == 0:
                    queue.append(nxt)

        ans = topological_sort if len(topological_sort) == numCourses else []
        return ans
