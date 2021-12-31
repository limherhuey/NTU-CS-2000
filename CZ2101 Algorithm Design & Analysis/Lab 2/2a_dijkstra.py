from random import randint, sample

MAX_N = 1000


def printGraph(G, n):
    """ Prints an adjacency matrix graph. """
    for i in range(n):
        for j in range(n):
            print(G[i][j], " ", sep="", end="")
        print()

def createGraph(n):
    """ Creates a randomly-generated adjacency matrix graph. """
    G = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        vertices = sample(range(n), randint(1, n))
        for j in range(len(vertices)):
            if vertices[j] == i:
                continue
            G[i][vertices[j]] = randint(1, n)
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

def getPriority(d, pQ):
    """ Returns index of shortest distance vertex. """
    min = 0
    for i in range(len(pQ)):
        if d[pQ[i]] < d[pQ[min]]:
            min = i
    idx = pQ[min]
    del pQ[min]
    return idx

def Dijkstra_a(G, n, source):
    """ Dijkstra implementation using an adjacency matrix and priority array. """
    d = [MAX_N for v in range(n)]   # estimates for len of shortest paths from source vertex to vertex v
    pi = [MAX_N for v in range(n)]  # predecessors for each vertex
    S = [0 for v in range(n)]       # set of explored vertices

    d[source] = 0
    pQ = [v for v in range(n)]

    while not isEmpty(pQ):
        u = getPriority(d, pQ)
        S[u] = 1    # mark as visited

        # for each neighbour v of vertex u
        for v in range(n):
            if G[u][v]:
                # if newly uncovered distance is shorter than current distance from source vertex
                if not S[v] and d[v] > d[u] + G[u][v]:
                    # update distance and predecessor vertex
                    d[v] = d[u] + G[u][v]
                    pi[v] = u

    return pi


def shortestPath(pi):
    """ Traces pi to get shortest path. """
    pass

def run(G, n, source):
    """ Runs. """
    pi = Dijkstra_a(G, n, source)
    sPath = shortestPath(pi)

    print(sPath)


if __name__ == '__main__':
    print("Dijkstra with an adjacency matrix and array.")
    # G, n = userInput()
    G, n = randomGen()
    printGraph(G, n)

    print("\nShortest Path: ")
    run(G, n, 0)
    