class DepthFirstTraversal:
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.adjacencyList = [[] for _ in range(numVertices)]

    def addEdge(self, vertex1, vertex2):
        self.adjacencyList[vertex1].append(vertex2)

    def depthFirstSearchUtil(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for adjacentVertex in self.adjacencyList[vertex]:
            if not visited[adjacentVertex]:
                self.depthFirstSearchUtil(adjacentVertex, visited)

    def performDepthFirstSearch(self, startVertex):
        visited = [False] * self.numVertices
        self.depthFirstSearchUtil(startVertex, visited)


if __name__ == '__main__':
    numVertices = int(input("Enter the number of vertices: "))
    graph = DepthFirstTraversal(numVertices)

    numEdges = int(input("Enter the number of edges: "))
    print("Enter the edges (start & destination):")
    for _ in range(numEdges):
        vertex1, vertex2 = map(int, input().split())
        graph.addEdge(vertex1, vertex2)

    startVertex = int(input("Enter the starting vertex: "))

    print("Following is the Depth First Traversal:")
    graph.performDepthFirstSearch(startVertex)
