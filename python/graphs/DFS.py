# Author: Francesco Andrea Antoniazzi
#
# Problem: Depth First Search (DFS) is a basic graph algorithm that provides a criteria to inspect the whole graph. Every node is visited once.
#
# Theorical solution: 
# During the whole run of the algorithm, every node will have one of the following three colors: white (not discovered yet), gray (discovered not completed) and black (completed).
# DFS won't consider recursions calls when the current node's color is gray or black, as the node has been already discovered. The procedure will always visit all neighbors before visiting the node itself.
# 
# Steps: 
#   1. At initialization phase, all the nodes are set white
#   2. While there exist a white node in the order stack, pick the white node at starting point
#   3. Call an auxiliary recursion function that will traverse the tree from the starting point
#   4. The auxiliary function checks the color of the given node
#   5. If the node is white, make it gray and call the auxiliary function for all the neighbors
#   6. Visit the node and set it black
# 
# Usage: 
# DFS can be used to:
#   - search a value over the whole graph
#   - discover cycles in graphs
#   - find SCC (Strongly Connected Components)




def DFS(nodes, edges, order):
    colors = { node: 'W' for node in nodes}
    dfs_stack = []
    groups = []
    while order:
        start = order.pop()
        if colors[start] == 'W':
            visited_nodes = []
            DFS_aux(start, edges, colors, dfs_stack, visited_nodes)
            groups.append(visited_nodes)
            
    return dfs_stack, groups

def DFS_aux(node, edges, colors, dfs_stack, visited_nodes):
    if colors[node] == 'W':
        colors[node] = 'G'
        
        for out_nodes in edges[node]:
            DFS_aux(out_nodes, edges, colors, dfs_stack, visited_nodes)
        # VISIT NODE
        dfs_stack.append(node)
        visited_nodes.append(node)
        colors[node] = 'B'


# Example of usage
nodes = ["A", "B", "C", "D"]
adj = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["B"],
    "D": [],
}

dfs_stack, forest = DFS(nodes, adj, nodes[:])

print(dfs_stack)
print(forest)
