import heapq

def dijkstra( graph, source ):
    """Computes shortest path from source to all vertices using Dijkstra's algorithm."""
    V = len( graph )
    distances = { i: float( 'inf' ) for i in range( V ) }
    distances[source] = 0
    pq = [( 0, source )]  # (distance, vertex)
    
    while pq:
        curr_distance, u = heapq.heappop(pq)
        
        if curr_distance > distances[u]:
            continue

        for v, weight in graph[u]:
            distance = curr_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush( pq, ( distance, v ) )

    return distances

# Example Usage
graph = {
    0: [( 1, 10 ), ( 2, 3 )],
    1: [( 2, 1 ), ( 3, 2 )],
    2: [( 1, 4 ), ( 3, 8 ), ( 4, 2 )],
    3: [( 4, 7 )],
    4: [( 3, 9 )]
}

source = 0
shortest_paths = dijkstra( graph, source )
print( "Shortest distances from source", source, ":", shortest_paths )
