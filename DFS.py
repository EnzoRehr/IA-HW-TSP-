import time  # Import the time module to measure execution time
from decimal import Decimal  # Import the Decimal class for high-precision arithmetic

def dfs_tsp(graph, start):
    start_time = time.time()  # Record the start time
    n = len(graph)  # Get the number of nodes in the graph
    best_route = None  # Initialize the best route
    min_distance = Decimal('Infinity')  # Initialize the minimum distance with infinity

    def dfs(route, visited, current_distance):
        nonlocal best_route, min_distance  # Access the variables from the outer function
        if len(route) == n:  # If all nodes have been visited
            route.append(start)  # Append the starting node to complete the cycle
            current_distance += graph[route[-2]][route[-1]]  # Update the current distance
            if current_distance < min_distance:  # If the current distance is less than the minimum distance
                min_distance = current_distance  # Update the minimum distance
                best_route = route.copy()  # Update the best route
            route.pop()  # Remove the starting node
            return  # Exit the function

        for i in range(n):  # Iterate through all nodes
            if not visited[i]:  # If the node has not been visited
                route.append(i)  # Add the node to the route
                visited[i] = True  # Mark the node as visited
                next_distance = current_distance + graph[route[-2]][i]  # Calculate the distance to the next node
                if next_distance < min_distance:  # If the next distance is less than the minimum distance
                    dfs(route, visited, next_distance)  # Recursively call dfs
                visited[i] = False  # Unmark the node as visited
                route.pop()  # Remove the node from the route

    visited = [False] * n  # Initialize a list to keep track of visited nodes
    visited[start] = True  # Mark the starting node as visited
    dfs([start], visited, 0)  # Start depth-first search from the starting node with initial distance 0

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    return best_route, min_distance, elapsed_time  # Return the best route, minimum distance, and elapsed time