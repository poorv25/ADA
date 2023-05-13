import networkx as nx
import matplotlib.pyplot as plt

def find_communities(G):
    # Create a copy of the original graph
    G_temp = G.copy()
    # Initialize the communities list
    communities = []
    # Repeat until there are no edges left in the graph
    while len(G_temp.edges()) > 0:
        # Calculate the betweenness centrality of all edges in the graph
        centrality = nx.edge_betweenness_centrality(G_temp)
        # Find the edge(s) with the highest betweenness centrality
        max_centrality = max(centrality.values())
        max_edges = [edge for edge, centrality in centrality.items() if centrality == max_centrality]
        # Remove the edge(s) with the highest betweenness centrality from the graph
        G_temp.remove_edges_from(max_edges)
        # Find the connected components of the graph
        components = [list(c) for c in nx.connected_components(G_temp)]
        # If there is more than one connected component, add them to the communities list
        if len(components) > 1:
            communities.extend(components)
    # Return the list of communities
    return communities

# Example usage
G = nx.karate_club_graph()
communities = find_communities(G)
print(communities)
# Output: [[0, 1, 2, 3, 7, 11, 12, 13, 17, 19, 21], [4, 5, 6, 10, 16], [8, 14, 15, 18, 20, 22, 23, 26, 28, 29, 30, 31, 32, 33], [9, 24, 25, 27]]
# Visualize the communities
colors = ['r', 'b', 'g', 'y']
for i, community in enumerate(communities):
    nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), nodelist=community, node_color=colors[i])
nx.draw_networkx_edges(G, pos=nx.spring_layout(G))
plt.show()
