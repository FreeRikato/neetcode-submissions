class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()
        no_of_components = 0

        def dfs(node):
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for i in range(n):
            if i not in visited:
                dfs(i)
                no_of_components += 1
        
        return no_of_components
