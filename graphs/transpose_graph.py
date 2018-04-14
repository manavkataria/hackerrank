
def transpose_graph(node):
    """
        Creates a new Node() for `node` and adds itself as a neighbour to its outnodes; recurses for its unvisited neighbours
    """
    if node.val in graph.keys():
        return graph.keys[node.val]

    root = Node()
    root.val = node.val
    root.neighbours = []
    graph[root.val] = root

    neighbour_node = None
    for v in node.neighbours:
        if v.val not in graph.keys():
            neighbour_node = transpose_graph(v)
        else:
            neighbour_node = graph[v.val]
        neighbour_node.neighbours.append(root)

    return root
