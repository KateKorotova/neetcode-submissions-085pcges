from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # state = [0]*n 

        # def has_cycle(node):
        #     if state[node] == 1:
        #         return True
        #     if state[node] == 2:
        #         return False
        #     state[node] = 1
        #     for nei in graph[node]:
        #         if nei == node:
        #             continue
        #         if has_cycle(nei):
        #             return True
        #     state[node] = 2
        #     return False


        # for i in range(n):
        #     cycle = has_cycle(i)
        #     if cycle:
        #         return False

        if len(edges) >= n:
            return False

        visited = set()
        queue = deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    queue.append(nei)

        return len(visited) == n


        




        