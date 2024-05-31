import heapq  # Import the heapq module for priority queue operations
import time  # Import the time module to measure execution time
from decimal import Decimal  # Import the Decimal class for high-precision arithmetic

def ucs_tsp(graph, start):
    start_time = time.time()  # Record the start time
    n = len(graph)  # Get the number of nodes in the graph
    pq = []  # Initialize an empty priority queue
    heapq.heappush(pq, (0, [start], set([start]), 0))  # Push the initial state to the priority queue
    best_route = None  # Initialize the best route
    min_distance = Decimal('Infinity')  # Initialize the minimum distance with infinity

    while pq:  # While the priority queue is not empty
        total_distance, route, visited, current = heapq.heappop(pq)  # Pop the state with the smallest total distance
        
        if len(route) == n:  # If all nodes have been visited
            total_distance += graph[current][start]  # Add the distance from the current node to the start node
            route.append(start)  # Append the start node to complete the cycle
            if total_distance < min_distance:  # If the total distance is less than the minimum distance
                min_distance = total_distance  # Update the minimum distance
                best_route = route  # Update the best route
            continue  # Continue to the next iteration

        for next_city in range(n):  # Iterate through all cities
            if next_city not in visited:  # If the city has not been visited
                next_total_distance = total_distance + graph[current][next_city]  # Calculate the total distance to the next city
                heapq.heappush(pq, (next_total_distance, route + [next_city], visited | {next_city}, next_city))  # Push the next state to the priority queue

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time

    return best_route, min_distance, elapsed_time  # Return the best route, minimum distance, and elapsed time