from random import randint, sample
import heapq

MAX_N = 1000


def printGraph(G, n):
    """ Prints an adjacency list graph. """
    for i in range(n):
        print(i, ": ", sep="", end="")
        for j in range(len(G[i])):
            print(G[i][j][0], "(", G[i][j][1], ") ", sep="", end="")
        print()

def createGraph(n):
    """ Creates a randomly-generated adjacency list graph. """
    G = [list() for i in range(n)]
    for i in range(n):
        vertices = sample(range(n), randint(1, n))
        for j in range(len(vertices)):
            if vertices[j] == i:
                continue
            # G consists of n adjacency lists with (vertex id, weight) as elements representing edges
            G[i].append((vertices[j], randint(1, n)))
    return G

def userInput():
    """ Receive input n from user then build a graph of size n. """
    n = int(input("Input n: "))
    return createGraph(n), n

def randomGen():
    """ Randomise n then build a graph of size n. """
    n = randint(1, MAX_N)
    return createGraph(n), n


def isEmpty(Q):
    """ Checks whether queue is empty. """
    return len(Q) == 0

def Dijkstra_b(G, n, source):
    """ Dijkstra implementation using an adjacency list and minimising heap. """
    d = [MAX_N for v in range(n)]   # estimates for len of shortest paths from source vertex to vertex v
    pi = [MAX_N for v in range(n)]  # predecessors for each vertex
    S = [0 for v in range(n)]       # set of explored vertices

    d[source] = 0
    hQ = [(d[v], v) for v in range(n) if not S[v]]
    heapq.heapify(hQ)

    while not isEmpty(hQ):
        _, u = heapq.heappop(hQ)
        S[u] = 1    # mark as visited

        # for each neighbour v of vertex u
        for i in range(len(G[u])):
            v = G[u][i][0]
            # if newly uncovered distance is shorter than current distance from source vertex
            if not S[v] and d[v] > d[u] + G[u][i][1]:
                # update distance and predecessor vertex
                d[v] = d[u] + G[u][i][1]
                pi[v] = u

        hQ = [(d[v], v) for v in range(n) if not S[v]]
        heapq.heapify(hQ)

    return pi

def shortestPath(pi, end):
    """ Traces pi to get shortest path. """
    pass

def findShortestPath(G, n, source):
    """ Runs. """
    pi, end = Dijkstra_b(G, n, source)
    sPath = shortestPath(pi, end)

    print(sPath)


if __name__ == '__main__':
    print("Dijkstra with an adjacency list and minimizing heap.")
    # G, n = userInput()
    G, n = randomGen()
    printGraph(G, n)

    print("\nShortest Path: ")
    findShortestPath(G, n, 0)
