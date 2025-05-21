class Grafo:
    def __init__(self, grafo):
        self.grafo = grafo
        self.row = len(grafo)

    def BFS(self, s, t, parent):
        visited = [False] * (self.row)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.grafo[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False
    
    def fordFulkerson(self, s, t):
        parent = [-1] * (self.row)
        max_flow = 0

        while self.BFS(s, t, parent):
            path_flow = float("Inf")
            s = t
            while(s != 0):
                path_flow = min(path_flow, self.grafo[parent[s]][s])
                s = parent[s]

            v = t
            while(v != 0):
                u = parent[v]
                self.grafo[u][v] -= path_flow
                self.grafo[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow
    
grafo = [[0, 7, 3, 0, 0, 0],
         [0, 0, 1, 6, 0, 0,],
         [0, 0, 0, 0, 8, 0],
         [0, 0, 3, 0, 0, 2],
         [0, 0, 0, 2, 0, 8],
         [0, 0, 0, 0, 0, 0]]

g = Grafo(grafo)
s = 0
t = 5
print ("O fluxo máximo possível é %d " % g.fordFulkerson(s, t))