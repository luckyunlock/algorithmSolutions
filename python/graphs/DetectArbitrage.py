

import math
def detectArbitrage(exchangeRates):
    log_matrix = []
    for node in exchangeRates:
        new_row = []
        for out_edge in node:
            new_row.append((-1) * math.log(out_edge,10) )
        log_matrix.append(new_row)

    return bellman_ford(log_matrix)

def bellman_ford(log_matrix):
    num_nodes = len(log_matrix)
    
    # Initialize vectors of distances from start
    dist = [float('inf')] * num_nodes
    dist[0] = 0
    
    for _ in range(num_nodes-1):
        # Relax all edges
        for u in range(len(log_matrix)):
            for v in range(len(log_matrix[u])):
                edge_weight = log_matrix[u][v]
                if dist[v] > dist[u] + edge_weight:
                    dist[v] = dist[u] + edge_weight

    for u in range(len(log_matrix)):
        for v in range(len(log_matrix[u])):
            edge_weight = log_matrix[u][v]
            if dist[v] > dist[u] + edge_weight:
                return True

    return False
                