class Graph:
    ''' A class that include the methods for Graphs'''

    def __init__(self):
    ''' A fuction to iniciate the graph'''
        self.graph = {}
        self.edges = {}
        self.vertex_count = 0

    def get_vertices(self):
    ''' A fuction to return the vertices of Graph'''
        return self.graph.keys()

    def get_neighbours(self, u):
    ''' A fuction to verify all the neighbours of a vertex'''
        return self.graph[u]

    def add_vertex(self, u):
    ''' A fuction to add a element us vertex to Graph'''
        if u not in self.graph:
            self.graph[u] = []
            self.edges[u] = []

    def add_edge(self, u, v, weight):
    ''' A fuction to add a edge between u and v. Add
    the weight of this edge. After include the edge,
    increase the numbers of vertices '''
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        self.edges[u].append(weight)
        self.vertex_count += 1

    def get_edge_weight(self, u, v):
    ''' Localize the distance between a source and a target in 
    the list of all of weight from the source'''
        edges = self.edges[u]
        for i in range(len(edges)):
            if self.graph[u][i] == v:
                return edges[i]
        return 0

    def min_distance_between(self, u, v):
    ''' Aplly the dijkstra fuction to a element from Graph.
    Return the minime distance between two vertices'''
        res = dijkstra(self, u)
        return res[v].distance

    # Prints all paths from 's' to 'd'
    def find_all_paths(self, s, d, max_steps):
        '''A recursive function to print all paths from 'u' to 'd'.
            visited[] keeps track of vertices in current path.
            path[] stores actual vertices and path_index is current
            index in path[]'''
        print(self.graph)
        def find_all_paths_util(u, d, visited, path, max_steps, step=0):

            # Mark the current node as visited and store in path
            visited[u] = True
            path.append(u)
            step = step + 1

            # If current vertex is same as destination, then print
            # current path[]
            if u == d and step - 1 <= max_steps:
                print(path, step)
                paths.append(list(path))
            else:
                # If current vertex is not destination
                # Recur for all the vertices adjacent to this vertex
                for i in self.graph[u]:
                    if visited[i] == False:
                        find_all_paths_util(
                            i, d, visited, path, max_steps, step)

            # Remove current vertex from path[] and mark it as unvisited
            path.pop()
            visited[u] = False
            return paths

        # Mark all the vertices as not visited
        visited = {}
        for v in self.get_vertices():
            visited[v] = False

        # Create an array to store paths
        path = []
        paths = []

        # Call the recursive helper function to print all paths
        return find_all_paths_util(s, d, visited, path, max_steps)


class DijkstraVertex():
    ''' This fuction gets the vertices that was traveled in all paths'''
    def __init__(self, vertex):
        self.vertex = vertex
        self.distance = 1e17
        self.parent = None

    def __repr__(self):
        return "to {} - {} (from {})".format(self.vertex, self.distance, self.parent.vertex if self.parent else "None")

    def build_path(self):
    ''' A fuction to create a path using the vertices that was traveled until the last vertex.
    The path is created starting from the last vertex to the initial'''
        current = self
        path = [current.vertex]
        while current.parent is not None:
            current = current.parent
            path.insert(0, current.vertex)
        return path


def dijkstra(graph: Graph, source):
    def relax(u, v):
        weight = graph.get_edge_weight(u.vertex, v.vertex)
        if v.distance > u.distance + weight:
            v.distance = u.distance + weight
            v.parent = u

    def extract_min(vertices: set):
        min_item = list(vertices)[0]
        for v in vertices:
            if v.distance < min_item.distance:
                min_item = v
        vertices.remove(min_item)
        return min_item

    d_vertices = {}
    for v in graph.get_vertices():
        d_vertices[v] = DijkstraVertex(v)
    d_vertices[source].distance = 0

    non_visited_vertices = set(d_vertices.values())

    while len(non_visited_vertices) > 0:
        u = extract_min(non_visited_vertices)
        for v in graph.get_neighbours(u.vertex):
            relax(u, d_vertices[v])

    return d_vertices

