# Dijkstra's algorithm
# The algorithm finds the shortest path between two nodes in a graph.
# The graph is represented as a dictionary of nodes, where each node is a dictionary of its neighbors.
# The algorithm iterates over the nodes and finds the lowest cost node that has not been processed yet.
# It then updates the costs of the neighbors of this node.
#The O complexity of this algorithm is O(n^2) because it iterates over the nodes and the neighbors of each node.

def initialize_data():
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}
    processed = []
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = float("inf")
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None
    return graph, processed, costs, parents

def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def update_costs_and_parents(node, cost, neighbors, costs, parents, processed):
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)

def dijkstra(graph, costs, processed, parents):
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        update_costs_and_parents(node, cost, neighbors, costs, parents, processed)
        node = find_lowest_cost_node(costs, processed)
    return costs

def main():
    graph, processed, costs, parents = initialize_data()
    dijkstra_result = dijkstra(graph, costs, processed, parents)
    print(dijkstra_result["fin"])

if __name__ == "__main__":
    main()
