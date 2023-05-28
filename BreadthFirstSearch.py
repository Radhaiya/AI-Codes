from collections import deque

class BreadthFirstTraversal:
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.adjacencyList = [[] for _ in range(numVertices)]

    def addEdge(self, vertex1, vertex2):
        self.adjacencyList[vertex1].append(vertex2)

    def breadthFirstSearch(self, startVertex):
        visited = [False] * self.numVertices
        queue = deque()

        visited[startVertex] = True
        queue.append(startVertex)

        while queue:
            currentVertex = queue.popleft()
            print(currentVertex, end=" ")

            for adjacentVertex in self.adjacencyList[currentVertex]:
                if not visited[adjacentVertex]:
                    visited[adjacentVertex] = True
                    queue.append(adjacentVertex)


if __name__ == '__main__':
    numVertices = int(input("Enter the number of vertices: "))
    graph = BreadthFirstTraversal(numVertices)

    numEdges = int(input("Enter the number of edges: "))
    print("Enter the edges (start & destination):")
    for _ in range(numEdges):
        vertex1, vertex2 = map(int, input().split())
        graph.addEdge(vertex1, vertex2)

    startVertex = int(input("Enter the starting vertex: "))

    print("Following is the Breadth-First Traversal:")
    graph.breadthFirstSearch(startVertex)
