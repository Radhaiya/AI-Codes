class Node:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt


dsuf = []
mst = []


def comparator(a, b):
    return a.wt < b.wt


def find(v):
    if dsuf[v].parent == -1:
        return v
    dsuf[v].parent = find(dsuf[v].parent)
    return dsuf[v].parent


def union_op(fromP, toP):
    if dsuf[fromP].rank > dsuf[toP].rank:
        dsuf[toP].parent = fromP
        dsuf[fromP].rank += 1
    elif dsuf[fromP].rank < dsuf[toP].rank:
        dsuf[fromP].parent = toP
        dsuf[toP].rank += 1
    else:
        dsuf[fromP].parent = toP
        dsuf[toP].rank += 1


def kruskals(edge_list, V, E):
    edge_list.sort(key=comparator)
    i = 0
    j = 0
    while i < (V - 1) and j < E:
        fromP = find(edge_list[j].src)
        toP = find(edge_list[j].dest)
        if fromP == toP:
            j += 1
            continue
        union_op(fromP, toP)
        mst.append(edge_list[j])
        i += 1


def print_mst(MST):
    for edge in MST:
        print(f"src: {edge.src}")
        print(f"dest: {edge.dest}")
        print(f"wt: {edge.wt}")
        print()


if __name__ == '__main__':
    E, V = map(int, input("Enter the number of edges and vertices: ").split())
    dsuf = [Node(-1, 0) for _ in range(V)]
    edge_list = []

    for _ in range(E):
        s, d, w = map(int, input().split())
        edge_list.append(Edge(s, d, w))

    kruskals(edge_list, V, E)
    print_mst(mst)
