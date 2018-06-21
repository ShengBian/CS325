# Author: Sheng Bian
# Date: May 13, 2017
# Description: This program read input from a file contains the number
# of wrestlers, n, followed by their names, the number of rivalries r
# and rivalries listed in pairs. It will output whether it is possible
# to designate some of the wrestlers as Babyfaces and the remainder as
# Heels such that each rivalry is between a Babyface and a Heel.

# The following code reference from https://www.youtube.com/watch?v=-uR7BSfNJko

# class Vertex represents wrestler
class Vertex:
    # constructor assign initial values
    def __init__(self, wrestler):
        # assign wrestler to the name of Vertex
        self.name = wrestler
        # empty list of neighbours
        self.neighbors = list()
        # initial distance is very large
        self.distance = 88888
        # unvisited color is gray
        self.color = 'gray'
        # types of wrestlers
        self.type = ''

    # add other Vertex to neighbor
    def add_neighbor(self, v):
        # confirms the vertex is not already a neighbor
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

# Graph class is used to build graph using wrestlers and pairs of rivalries
# if it successfully build the graph, it is possible to designate, vice versa.
class Graph:
    # contains all the wrestlers
    vertices = {}

    # add vertex (wrestler) to graph
    def add_vertex(self, vertex):
        # check if vertex already in vertices dictionary
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

    # add edges (rivalries) to graph
    def add_edge(self, u, v):
        # u and v are vertex, check if they are in vertices dictionary
        if u in self.vertices and v in self.vertices:
            # add neighbours for u and v
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)

    # Breadth first search to check if it is possible to designate
    def bfs(self, vertex):
        # initialize the empty queue
        q = list()
        vertex.distance = 0
        # color blue represent visited node
        vertex.color = 'blue'
        # initialize the start vertex type is Babyfaces
        vertex.type = 'Babyface'

        for v in vertex.neighbors:
            self.vertices[v].distance = vertex.distance + 1
            # the neighbor of 'Babyface' is 'Heel'
            self.vertices[v].type = 'Heel'
            q.append(v)

        # loop through neighbors to BFS
        while len(q) > 0:
            # Dequeue a vertex from queue
            u = q.pop(0)
            node_u = self.vertices[u]
            # mark visited node is blue
            node_u.color = 'blue'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                # if the node is unvisited, enqueue the v to the queue
                if node_v.color == 'gray':
                    q.append(v)
                    # if the distance is bigger than previous node, increase distance by 1
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1
                    # sine the start node is Babyfaces, if the distance is even, the type of
                    # that vertex should be Babyfaces
                    if node_v.distance % 2 == 0:
                        node_v.type = 'Babyface'
                    else:
                        node_v.type = 'Heel'
                    # when u and v have the same type, it's impossible to designate, just exit the program
                    if node_v.type == node_u.type:
                        print("Impossible")
                        quit()

        # loop through unvisited vertices to build the graph
        for v in self.vertices:
            if self.vertices[v].color == 'gray':
                self.bfs(self.vertices[v])

    # this function is used to print the result
    def printResult(self):
        print("Yes Possible")
        result1 = 'Babyfaces: '
        result2 = 'Heels: '
        list1 = []
        list2 = []
        # print the result based on two different types
        for v in self.vertices:
            if self.vertices[v].type == "Babyface":
                list1.append(self.vertices[v].name)
        list1.sort()
        for item in list1:
            result1 = result1 + item + ' '

        for v in self.vertices:
            if self.vertices[v].type == "Heel":
                list2.append(self.vertices[v].name)
        list2.sort()
        for item in list2:
            result2 = result2 + item + ' '

        print(result1)
        print(result2)


# Input is read in from a file specified in the command line at run time
filename = raw_input('Enter a filename: ')
with open(filename) as file_stream:
    # split the input line by line
    lines = file_stream.read().splitlines()
    # first line of data is number of wrestlers
    num_w = int(lines[0])
    # the number of rivalries is number of wrestlers plus 1
    num_r = int(lines[num_w + 1])
    g = Graph()
    # add wrestlers to vertices of graph
    for i in range(1, num_w + 1):
        g.add_vertex(Vertex(lines[i]))

    # add neighbours of vertices
    for j in range(num_w + 2, num_w + num_r + 2):
        # split one line data to two wrestlers
        wrestlers = lines[j].split()
        g.add_edge(wrestlers[0], wrestlers[1])

    # call the bfs to build the graph
    g.bfs(g.vertices[lines[1]])
    # if it successfully build the graph, we can print the result
    g.printResult()
