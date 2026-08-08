"""
Problem 9: Node Path Existence (Graph Traversal)

Language Choice: Python
Reason: An adjacency list dictionary coupled with BFS allows straightforward graph representation 
and guarantees finding the shortest path in unweighted directed graphs with cycles.

Approach:
1. Represent the directed graph using an adjacency list.
2. Perform Breadth-First Search (BFS) starting from `start_node`.
   - Maintain a queue storing tuples of (current_node, path_taken_so_far).
   - Maintain a `visited` set to prevent infinite loops caused by cycles.
3. Formats output string strictly as required:
   - Path exists:  "True (START --> ... --> END)"
   - No path:      "False"

Space-Time Complexity Analysis:
- Time Complexity: O(V + E) where V = vertices and E = edges.
- Space Complexity: O(V) for visited set and BFS queue.
"""

def find_node_path(graph: dict[str, list[str]], start_node: str, end_node: str) -> str:
    """
    Checks if a connected path exists between start_node and end_node.
    Returns string formatted to match assignment requirements:
    - True (A --> B --> C)
    - False
    """
    if start_node not in graph or end_node not in graph:
        return "False"

    if start_node == end_node:
        return f"True ({start_node})"

    queue = [(start_node, [start_node])]
    visited = {start_node}

    while queue:
        current, path = queue.pop(0)

        for neighbor in graph.get(current, []):
            if neighbor == end_node:
                full_path = path + [neighbor]
                path_str = " --> ".join(full_path)
                return f"True ({path_str})"

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return "False"


# --- Graph matching assignment image & all 4 examples perfectly ---
SAMPLE_GRAPH = {
    'A': ['B'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['F'],
    'D': ['G'],         # D only points to G
    'E': ['F'],         # E only points to F
    'F': ['B', 'G'],    # F points back to B and G
    'G': [],
    'H': []             # Isolated node
}


# --- Interactive CLI Execution ---
if __name__ == "__main__":
    print("=== Problem 9: Node Path Existence ===")
    
    start_in = input("Enter Start Node (default 'E'): ").strip().upper()
    end_in = input("Enter End Node (default 'D'): ").strip().upper()

    start_node = start_in if start_in else "E"
    end_node = end_in if end_in else "D"

    output = find_node_path(SAMPLE_GRAPH, start_node, end_node)

    print(f"\nInput: Start = {start_node}, End = {end_node}")
    print(f"Expected output: {output}\n")