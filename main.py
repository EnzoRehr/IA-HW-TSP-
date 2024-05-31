import sys  # Import the sys module to access system-specific parameters and functions

# Import functions for solving TSP from different modules
from DFS import dfs_tsp
from Least_Cost import ucs_tsp
from AStar import a_star_tsp

# Import utility functions for generating and reading graphs
from Graph_Utils import generate_adjacency_matrix_from_tsp
from Graph_Utils import read_graph_from_file

def menu():
    # Display menu options for selecting the file to read from
    print("Traveling Salesman Problem Solver")
    print("The file to read from:")
    print("1. Graph")
    print("2. gr137 (first 10 nodes)")
    print("3. att532 (first 10 nodes)")
    print("4. ulysses22 (first 10 nodes)")
    choice = input("Enter your choice (1/2/3/4): ")  # Prompt user for input
    return int(choice)  # Return the integer choice entered by the user

def show(graph, start_city):
    # Display results of TSP algorithms for the given graph and starting city
    
    # Run DFS algorithm and display results
    route, cost, time = dfs_tsp(graph, start_city)
    print("==DFS Result==")
    print(f"Route: {route}")
    print(f"Cost: {cost}")
    print(f"RunTime: {time}")
    
    # Run UCS algorithm and display results
    route, cost, time = ucs_tsp(graph, start_city)
    print("==UCS Result==")
    print(f"Route: {route}")
    print(f"Cost: {cost}")
    print(f"RunTime: {time}")
    
    # Run A* algorithm and display results
    route, cost, time = a_star_tsp(graph, start_city)
    print("==A* Result==")
    print(f"Route: {route}")
    print(f"Cost: {cost}")
    print(f"RunTime: {time}")

def main():
    # Main function to control the flow of the program
    
    while True:
        choice = menu()  # Prompt user for menu choice
        
        if choice == 1:
            generate_adjacency_matrix_from_tsp("Graph.txt", "AdjMat.txt")  # Generate adjacency matrix from Graph.txt
            
        elif choice == 2:
            generate_adjacency_matrix_from_tsp("gr137.txt", "AdjMat.txt")  # Generate adjacency matrix from gr137.txt

        elif choice == 3:
            generate_adjacency_matrix_from_tsp("att532.txt", "AdjMat.txt")  # Generate adjacency matrix from att532.txt
            
        elif choice == 4:
            generate_adjacency_matrix_from_tsp("ulysses22.txt", "AdjMat.txt")  # Generate adjacency matrix from ulysses22.txt
           
        else:
            print("==Exiting==")  # Print message indicating program is exiting
            break  # Exit the loop
        
        start_city = 0  # Define the starting city index as 0
        graph = read_graph_from_file("AdjMat.txt")  # Read the generated adjacency matrix from file
        show(graph, start_city)  # Show TSP results for the graph and starting city

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly