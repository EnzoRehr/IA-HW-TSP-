import math

def generate_adjacency_matrix_from_tsp(filename, output_filename):
    def read_tsp_file(filename):
        with open(filename, 'r') as file:  # Open the TSP file for reading
            lines = file.readlines()  # Read all lines from the file
        
        graph = []  # Initialize an empty list to store graph nodes
        in_node_section = False  # Flag to indicate when in the node section

        for line in lines:
            if line.strip() == "NODE_COORD_SECTION":  # Check for start of node section
                in_node_section = True  # Set the flag to true
                continue  # Skip to the next line
            if in_node_section:  # Process lines within the node section
                if line.strip() == "EOF":  # Check for end of file section
                    break  # Exit the loop if EOF is reached
                parts = line.split()  # Split the line into parts
                if len(parts) >= 3:  # Check if there are at least 3 parts
                    node_id = int(parts[0])  # Extract node ID
                    x = float(parts[1])  # Extract x-coordinate
                    y = float(parts[2])  # Extract y-coordinate
                    graph.append((node_id, x, y))  # Append the node to the graph
        
        return graph  # Return the graph as a list of nodes

    def euclidean_distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Calculate and return the Euclidean distance

    def create_adjacency_matrix(graph):
        dimension = len(graph)  # Get the number of nodes in the graph
        adjacency_matrix = [[0.0] * dimension for _ in range(dimension)]  # Initialize the adjacency matrix with zeros
        
        for i in range(dimension):
            for j in range(dimension):
                if i != j:  # Only calculate distances for different nodes
                    x1, y1 = graph[i][1], graph[i][2]  # Get coordinates of node i
                    x2, y2 = graph[j][1], graph[j][2]  # Get coordinates of node j
                    adjacency_matrix[i][j] = euclidean_distance(x1, y1, x2, y2)  # Compute and set the distance
        
        return adjacency_matrix  # Return the adjacency matrix

    def write_adjacency_matrix_to_file(adjacency_matrix, output_filename):
        with open(output_filename, 'w') as file:  # Open the output file for writing
            for row in adjacency_matrix:  # Iterate over each row of the adjacency matrix
                line = " ".join(f"{distance:.2f}" for distance in row)  # Format the row as a string
                file.write(line + "\n")  # Write the row to the file

    graph = read_tsp_file(filename)  # Read the TSP file and get the graph
    adjacency_matrix = create_adjacency_matrix(graph)  # Create the adjacency matrix from the graph
    write_adjacency_matrix_to_file(adjacency_matrix, output_filename)  # Write the adjacency matrix to the output file


def read_graph_from_file(filename):
    with open(filename, 'r') as file:  # Open the adjacency matrix file for reading
        lines = file.readlines()  # Read all lines from the file
    
    graph = []  # Initialize an empty list to store the graph

    for line in lines:
        graph.append(list(map(float, line.split())))  # Convert each line to a list of floats and append to the graph
    
    return graph  # Return the graph as an adjacency matrix