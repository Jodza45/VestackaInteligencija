def find_paths_of_length(graph, start, end, target_length):    
    stack = [(start, [start])]
    
    found_paths = []

    while stack:
        current_node, current_path = stack.pop()

        current_len = len(current_path) - 1

        if current_len == target_length:
            if current_node == end:
                found_paths.append(current_path)
            continue

        if current_len < target_length:
            for neighbor in graph.get(current_node, []):
                if neighbor not in current_path:
                    new_path = list(current_path) 
                    new_path.append(neighbor)     
                    stack.append((neighbor, new_path)) 

    return found_paths


undirected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


start_node = 'A'
end_node = 'F'
length = 3  

rezultati = find_paths_of_length(undirected_graph, start_node, end_node, length)

print(f"Putevi dužine {length} od čvora {start_node} do čvora {end_node}:")
if not rezultati:
    print("Nema pronađenih puteva zadate dužine.")
else:
    for path in rezultati:
        print(path)