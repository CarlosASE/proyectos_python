import heapq
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.animation as animation
from matplotlib.widgets import Button

# Define the graph as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Visualization
G = nx.Graph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)
pos = nx.spring_layout(G)

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.2)  # Adjust the bottom to fit the button
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', ax=ax)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
plt.title("Graph Visualization")

# Add a button
ax_button = plt.axes([0.45, 0.05, 0.1, 0.075])
button = Button(ax_button, 'Continue')

# Initialize the priority queue and distances for Dijkstra
distances = {node: float('infinity') for node in graph}
previous_nodes = {node: None for node in graph}
start_node = 'A'
distances[start_node] = 0
priority_queue = [(0, start_node)]
visited = set()

# Global variable to hold the animation
ani = None

def dijkstra_animated(event):
    global ani  # Use the global variable to store the animation

    def update(num):
        if priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                return
            visited.add(current_node)
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
            ax.clear()
            nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', ax=ax)
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
            
            # Highlight the shortest path edges
            path_edges = []
            for node in visited:
                if previous_nodes[node] is not None:
                    path_edges.append((previous_nodes[node], node))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2, ax=ax)
            nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color='green', node_size=500, ax=ax)

    ani = animation.FuncAnimation(fig, update, frames=len(graph) * 2, repeat=False)
    plt.title("Dijkstra's Algorithm Animation")
    plt.draw()

# Connect the button to the function
button.on_clicked(dijkstra_animated)

plt.show()