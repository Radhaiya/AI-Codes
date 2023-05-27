def addEdge(graph, edge1, edge2):
    graph[edge1][edge2] = 1
    graph[edge2][edge1] = 1

def safeToAssign(i, j, graph, v, color):
    for k in range(v):
        if graph[i][k] == 1 and color[k] == j:
            return False
    return True

def graphColoring(graph, m, v, i, color):
    if i == v:
        return True
    for j in range(m):
        if safeToAssign(i, j, graph, v, color):
            color[i] = j
            if graphColoring(graph, m, v, i + 1, color):
                return True
            color[i] = -1
    return False

def main():
    m = 3  # no. of colors
    v = 5  # no. of vertices
    graph = [[0] * v for _ in range(v)]

    addEdge(graph, 0, 1)
    addEdge(graph, 0, 2)
    addEdge(graph, 0, 3)
    addEdge(graph, 2, 4)
    addEdge(graph, 2, 3)
    addEdge(graph, 3, 4)

    color = [-1] * v
    i = 0
    if graphColoring(graph, m, v, i, color):
        print("Graph can be colored using", m, "colors")
    else:
        print("Graph cannot be colored using", m, "colors")

if __name__ == '__main__':
    main()

