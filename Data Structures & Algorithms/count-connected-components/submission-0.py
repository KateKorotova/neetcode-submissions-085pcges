class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit_global = set()
        
        def dfs(node):
            visit_global.add(node)
            for nei in graph[node]:
                if nei in visit_global:
                    continue
                dfs(nei)
        
        components = 0
        for i in range(n):
            if i in visit_global:
                continue
            dfs(i)
            components += 1
        return components

