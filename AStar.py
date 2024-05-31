import heapq  # Import the heapq module for priority queue operations
import time  # Import the time module to measure execution time
from decimal import Decimal  # Import the Decimal class for high-precision arithmetic

def prim_mst_cost(graph, vertices):
    if not vertices:  # If there are no vertices, return a cost of 0
        return 0
    
    visited = set()  # Initialize an empty set to keep track of visited vertices
    mst_cost = 0  # Initialize the cost of the minimum spanning tree (MST)
    edges = [(0, list(vertices)[0])]  # Start with an arbitrary vertex with cost 0

    while edges and len(visited) < len(vertices):  # While there are edges to process and not all vertices are visited
        cost, u = heapq.heappop(edges)  # Pop the edge with the smallest cost
        if u not in visited:  # If the vertex has not been visited
            visited.add(u)  # Mark the vertex as visited
            mst_cost += cost  # Add the cost to the MST cost
            for v in vertices:  # Iterate through all vertices
                if v not in visited:  # If the vertex has not been visited
                    heapq.heappush(edges, (graph[u][v], v))  # Push the edge to the priority queue
    
    return mst_cost  # Return the total cost of the MST

def a_star_tsp(graph, start):
    start_time = time.time()  # Record the start time
    n = len(graph)  # Get the number of nodes in the graph
    pq = []  # Initialize an empty priority queue
    initial_state = (0, [start], set([start]), 0)  # Define the initial state with cost 0, starting node, and empty visited set
    heapq.heappush(pq, initial_state)  # Push the initial state to the priority queue
    best_route = None  # Initialize the best route
    min_distance = Decimal('Infinity')  # Initialize the minimum distance with infinity

    while pq:  # While the priority queue is not empty
        estimated_cost, route, visited, current = heapq.heappop(pq)  # Pop the state with the smallest estimated cost
        actual_cost = estimated_cost - prim_mst_cost(graph, set(range(n)) - visited)  # Calculate the actual cost

        if len(route) == n:  # If all nodes have been visited
            total_cost = actual_cost + graph[current][start]  # Calculate the total cost of the route
            route.append(start)  # Append the starting node to complete the cycle
            if total_cost < min_distance:  # If the total cost is less than the minimum distance
                min_distance = total_cost  # Update the minimum distance
                best_route = route  # Update the best route
            continue  # Continue to the next iteration

        remaining_cities = set(range(n)) - visited  # Get the set of remaining cities to visit
        mst_cost = prim_mst_cost(graph, remaining_cities)  # Calculate the MST cost for the remaining cities
        
        for next_city in remaining_cities:  # Iterate through the remaining cities
            next_total_distance = actual_cost + graph[current][next_city]  # Calculate the next total distance
            estimated_cost = next_total_distance + mst_cost  # Estimate the cost with MST heuristic
            next_state = (estimated_cost, route + [next_city], visited | {next_city}, next_city)  # Define the next state
            heapq.heappush(pq, next_state)  # Push the next state to the priority queue

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    return best_route, min_distance, elapsed_time  # Return the best route, minimum distance, and elapsed time