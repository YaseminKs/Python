from collections import deque

class Graph:
    def __init__( self, vertices ):
        self.vertices = vertices
        self.adj_list = { i: [] for i in range( vertices ) }

    def add_edge( self, src, dest ):
        self.adj_list[src].append( dest )
        self.adj_list[dest].append( src )  # For an undirected graph

    def bfs( self, start ):
        visited = [False] * self.vertices
        queue = deque( [start] )
        visited[start] = True

        while queue:
            node = queue.popleft()
            print(node, end=" " )

            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append( neighbor )

# Example usage
g = Graph( 6 )
g.add_edge( 0, 1 )
g.add_edge( 0, 2 )
g.add_edge( 1, 3 )
g.add_edge( 1, 4 )
g.add_edge( 2, 5 )

print( "BFS traversal starting from node 0:" )
g.bfs( 0 )
