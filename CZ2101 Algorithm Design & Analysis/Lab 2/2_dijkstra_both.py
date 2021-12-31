import csv
import timeit
from random import random, randint, choice
import heapq


MAX_N = 1000


def printMatrixGraph(G, V):
    """ Prints an adjacency matrix graph. """
    for i in range(V):
        for j in range(V):
            print(G[i][j], " ", sep="", end="")
        print()

def createGraph(V, E):
    """ Creates a randomly-generated adjacency matrix graph. """

    # very bad but workable code on graph creation --> my 2am brain just trying to get the job done

    # get no. of neighbours for each vertex, no. of neighbours cannot exceed V-1
    neighbours = [random() for i in range(V)]
    s = sum(neighbours)
    neighbours = [round(i*E/s) for i in neighbours]
    not_cool = True
    while not_cool:
        not_cool = False
        for i in range(V):
            if neighbours[i] > V-1:
                not_cool = True
                extra = neighbours[i] - (V - 1)
                neighbours[i] -= extra
                for j in range(extra):
                    neighbours[(i+j+1) % V] += 1
                break

    G = [[0 for i in range(V)] for j in range(V)]
    for i in range(V):
        vertices = list()
        nei_available = set(range(V)) - set([i])
        for j in range(neighbours[i]):
            nei = choice(list(nei_available))
            vertices.append(nei)
            nei_available.remove(nei)
        for j in range(len(vertices)):
            G[i][vertices[j]] = randint(1, V)
    return G

def convert_adjM_to_adjL(matrixG, V):
    """ Converts an adjacency matrix graph G to an adjacency list. """

    listG = [list() for i in range(V)]
    for i in range(V):
        for j in range(V):
            if matrixG[i][j] != 0:
                listG[i].append((j, matrixG[i][j]))
    return listG

def genGraphs(V, E):
    """ Builds a random graph of V vertices and E edges. Returns in both adj matrix and adj list form. """
    matrixG = createGraph(V, E)
    listG = convert_adjM_to_adjL(matrixG, V)
    return matrixG, listG


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


def Dijkstra_a(G, V, source):
    """ Dijkstra implementation using an adjacency matrix and priority array. """
    d = [V for v in range(V)]   # estimates for len of shortest paths from source vertex to vertex v
    pi = [V for v in range(V)]  # predecessors for each vertex
    S = [0 for v in range(V)]       # set of explored vertices

    d[source] = 0
    pQ = [v for v in range(V)]

    while not isEmpty(pQ):
        u = getPriority(d, pQ)
        S[u] = 1    # mark as visited

        # for each neighbour v of vertex u
        for v in range(V):
            if G[u][v]:
                # if newly uncovered distance is shorter than current distance from source vertex
                if not S[v] and d[v] > d[u] + G[u][v]:
                    # update distance and predecessor vertex
                    d[v] = d[u] + G[u][v]
                    pi[v] = u

    return pi


def Dijkstra_b(G, V, source):
    """ Dijkstra implementation using an adjacency list and minimising heap. """
    d = [MAX_N for v in range(V)]   # estimates for len of shortest paths from source vertex to vertex v
    pi = [MAX_N for v in range(V)]  # predecessors for each vertex
    S = [0 for v in range(V)]       # set of explored vertices

    d[source] = 0
    hQ = [(d[v], v) for v in range(V) if not S[v]]
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

        hQ = [(d[v], v) for v in range(V) if not S[v]]
        heapq.heapify(hQ)

    return pi


def shortestPath(pi):
    """ Traces pi to get shortest path. """
    pass


def run(V, E, source, ave_over):
    """ Runs both algorithms on ave_over different graphs with V vertices and E edges. """

    a_runtime, b_runtime = 0, 0
    
    for i in range(ave_over):
        mG, lG = genGraphs(V, E)
        
        start = timeit.default_timer()
        pi = Dijkstra_a(mG, V, source)
        stop = timeit.default_timer()
        a_runtime += stop - start

        start = timeit.default_timer()
        pi = Dijkstra_b(lG, V, source)
        stop = timeit.default_timer()
        b_runtime += stop - start

    a_runtime /= ave_over
    b_runtime /= ave_over

    return a_runtime, b_runtime

def record(ave_over):
    """ Runs. """

    V = 10000
    Earr = [10000, 100000, 1000000, 10000000, 90000000]
    source = 0

    for i in range(len(Earr)):
        E = Earr[i]

        a_runtime, b_runtime = run(V, E, source, ave_over)

        with open('runtimes_2.csv', 'a+') as f:
            writer = csv.writer(f)
            writer.writerow(['a', V, E, a_runtime])
            writer.writerow(['b', V, E, b_runtime])


if __name__ == '__main__':
    print("Dijkstra.")
    # G, n = userInput()
    # printGraph(G, n)

    # with open('runtimes_2.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['algorithm', 'V', 'E', 'ave_runtime'])

    ave_over = 10

    record(ave_over)

    

    