def airportConnections(airports, routes, startingAirport):
    # Create the adjacency matrix
    adj, adj_transp = create_adjacency_matrix(airports, routes)
    # Find strongly connected components
    components, adj_components = SCC(airports, adj, adj_transp)
    # Count number of strongly connected components that has #in-edges == 0 and not contains starting point
    adj_transposed = transpose_adj(components, adj_components)

    print(components, adj_components, )
    print(adj_transposed)
    node_to_add = 0
    for comp, neigh_comp in adj_transposed.items():
        if not neigh_comp and startingAirport not in components[comp]:
            node_to_add += 1

    return node_to_add

def transpose_adj(nodes, adj):
    adj_transp = { idx: [] for idx, node in enumerate(nodes) }
    for origin, destinations in adj.items():
        for destination in destinations:
            adj_transp[destination].append(origin)
    return adj_transp
    
def create_adjacency_matrix(airports, routes):
    adj = { airport: [] for airport in airports }
    adj_transp = { airport: [] for airport in airports }
    for origin, destination in routes:
        adj[origin].append(destination)
        adj_transp[destination].append(origin)
    return adj, adj_transp

def SCC(nodes, edges, edges_transp):
    dfs_stack, _ = DFS(nodes, edges, nodes[:])
    _, components = DFS(nodes, edges_transp, dfs_stack[:])

    map_nodes_components = {}
    for idx, comp_nodes_list in enumerate(components):
        for node in comp_nodes_list:
            map_nodes_components[node] = idx

    adj_components = {}
    for idx, comp_nodes_list in enumerate(components):
        adj_components[idx] = set()
        for node in comp_nodes_list:
            components_pointed = [map_nodes_components[x] for x in edges[node]]
            adj_components[idx].update(components_pointed)
            if idx in adj_components[idx]:
                adj_components[idx].remove(idx)
    
    return components, adj_components

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
        dfs_stack.append(node)
        visited_nodes.append(node)
        colors[node] = 'B'