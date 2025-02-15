# Python implementation of Topological Sort

from collections import defaultdict

def topological_sort( vertices, edges ):
    graph = defaultdict( list )
    for u, v in edges:
        graph[u].append( v )

    visited = set()
    stack = []

    def dfs( v ):
        visited.add( v )
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs( neighbor )
        stack.append( v )

    for v in range( vertices ):
        if v not in visited:
            dfs( v )

    return stack[::-1]

vertices = 6
edges = [( 5, 2 ), ( 5, 0 ), ( 4, 0 ), ( 4, 1 ), ( 2, 3 ), ( 3, 1 )]
print( "Topological Sort:", topological_sort( vertices, edges ) )
