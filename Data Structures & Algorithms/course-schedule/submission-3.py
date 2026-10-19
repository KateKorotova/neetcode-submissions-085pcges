from collections import defaultdict
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        state = [0]*numCourses
        def has_cycle(course):
            if state[course] == 1:
                return True
            if state[course] == 2:
                return False
            state[course] = 1

            for child in graph[course]:
                if has_cycle(child):
                    return True 
            state[course] = 2
            return False
                
        for course in range(numCourses):
            check = has_cycle(course)
            if check:
                return False
        return True

        


