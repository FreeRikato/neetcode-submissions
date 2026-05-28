class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        no_of_connected_components = 0

        visited = set()

        def dfs(node):
            visited.add(node)
            
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for i in range(n):
            if i not in visited:
                dfs(i)
                no_of_connected_components += 1
        
        return no_of_connected_components