import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue


class GraphConstructor:
    def __init__(self):
        self.graph = nx.Graph()

    def construct_graph_with_max_triangles(self, graphic_sequence):

        vertices = [[i, degree] for i, degree in enumerate(graphic_sequence)]  # status:[vertex_id, free_edges]

        # Create a priority queue for vertices based on the number of "free" edges (degree)
        pq = PriorityQueue()
        for vertex in vertices:
            pq.put((-vertex[1], vertex[0]))  # The priority is by largest degree

        # creating edges until no vertex is left in the list
        while not pq.empty():
            current_vertex = pq.get()  # Get the vertex ID with largest degree
            current_ID, current_key = current_vertex[1], current_vertex[0]
            ids_to_update = []
            for _ in range(-current_key):
                if pq.empty():
                    print('Error: Invalid Graphic Sequence')
                    break  # If there are fewer than k vertices left, exit the loop

                next_vertex = pq.get()  # Get the next vertex ID
                next_vertex_id, next_vertex_key = next_vertex[1], next_vertex[0]
                next_vertex_free_edges = -next_vertex_key
                # Create an edge between the current vertex and the next vertex
                self.graph.add_edge(current_ID, next_vertex_id)
                print(f'Creating an edge from {current_ID} to {next_vertex_id}')

                # Update the number of free edges for the vertices
                next_vertex_free_edges -= 1
                vertices[next_vertex_id][1] = max(0, next_vertex_free_edges)

                # if the next vertex still has free edges, put it back in pq
                if next_vertex_free_edges > 0:
                    ids_to_update.append(next_vertex_id)

            for vertex_id in ids_to_update:
                pq.put((-vertices[vertex_id][1], vertex_id))

        return self.graph

    def print_graph(self):
        pos = nx.spring_layout(self.graph)
        degree_sequence = [self.graph.degree(node) for node in self.graph.nodes()]

        nx.draw(self.graph, pos, with_labels=False)

        # Draw vertex ID inside the circle
        labels = {node: str(node) for node in self.graph.nodes()}
        nx.draw_networkx_labels(self.graph, pos, labels=labels, font_color='w', font_size=10)

        # Draw degree around the vertices
        for node, (x, y) in pos.items():
            degree = self.graph.degree(node)
            plt.text(x, y+0.05, f"Degree: {degree}", ha='center', va='center',
                     bbox=dict(facecolor='gray', edgecolor='none', alpha=0.5))
        plt.title("Graph with Degrees")
        plt.show()