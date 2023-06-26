from GraphConstructor import GraphConstructor


# Example
graphic_sequence = [4, 4, 3, 2, 2, 1]
graph_constructor = GraphConstructor()
graph = graph_constructor.construct_graph_with_max_triangles(graphic_sequence)

# Print the graph with degrees
graph_constructor.print_graph()
