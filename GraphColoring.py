def add_edge(adj_matrix, vertex1, vertex2):
    adj_matrix[vertex1][vertex2] = 1
    adj_matrix[vertex2][vertex1] = 1

def is_safe_to_assign(vertex_index, color_index, adj_matrix, num_vertices, colors):
    for k in range(num_vertices):
        if adj_matrix[vertex_index][k] == 1 and colors[k] == color_index:
            return False
    return True

def graph_coloring(adj_matrix, num_colors, num_vertices, current_vertex, colors):
    if current_vertex == num_vertices:
        return True

    for color_index in range(num_colors):
        if is_safe_to_assign(current_vertex, color_index, adj_matrix, num_vertices, colors):
            colors[current_vertex] = color_index
            if graph_coloring(adj_matrix, num_colors, num_vertices, current_vertex + 1, colors):
                return True
            colors[current_vertex] = -1

    return False

def main():
    num_colors = 3  # Number of available colors
    num_vertices = 5  # Number of vertices
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    add_edge(adj_matrix, 0, 1)
    add_edge(adj_matrix, 0, 2)
    add_edge(adj_matrix, 0, 3)
    add_edge(adj_matrix, 2, 3)
    add_edge(adj_matrix, 2, 4)
    add_edge(adj_matrix, 3, 4)

    colors = [-1] * num_vertices
    current_vertex = 0

    if graph_coloring(adj_matrix, num_colors, num_vertices, current_vertex, colors):
        print("Graph can be colored using", num_colors, "colors")
    else:
        print("Graph cannot be colored using", num_colors, "colors")

if __name__ == '__main__':
    main()
