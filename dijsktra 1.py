import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start):
    # Initialize distances with infinity and set the distance to the start node to zero
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Priority queue to store nodes and their distances from the start node
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# Define the graph as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Run Dijkstra's algorithm
start_node = 'A'
distances = dijkstra(graph, start_node)
print("Distances from node", start_node, ":", distances)

# Visualization
G = nx.Graph()

# Add edges to the graph
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# Define positions of the nodes for visualization
pos = nx.spring_layout(G)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Highlight the shortest paths
shortest_paths = nx.single_source_dijkstra_path(G, start_node)
for target_node, path in shortest_paths.items():
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

plt.title("Shortest Paths from Node " + start_node)
plt.show()