class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0]*numCourses
        for course, pre in  prerequisites:
            graph[pre].append(course)
            in_degrees[course] += 1
        
        queue = deque(i for i in range(numCourses) if in_degrees[i] == 0)
        
        topological_sort = []
        while queue:
            node = queue.popleft()
            topological_sort.append(node)
            for course in graph[node]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    queue.append(course)

        return len(topological_sort) == numCourses


