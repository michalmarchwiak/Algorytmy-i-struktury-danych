import sys

from graphviz import Digraph
from queue import Queue

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = 'white'
        self.distance = sys.maxsize
        self.predecessor = None
        self.disc = 0
        self.fin = 0

    def add_neighbour(self, neighbour, weight=0):
        self.connected_to[neighbour] = weight

    def set_color(self,color):
        self.color = color

    def set_distance(self,d):
        self.distance = d

    def set_predecessor(self,p):
        self.predecessor = p

    def set_disc(self,d):
        self.disc = d

    def set_fin(self,f):
        self.fin = f

    def get_fin(self):
        return self.fin

    def get_disc(self):
        return self.disc

    def get_predecessor(self):
        return self.predecessor

    def get_distance(self):
        return self.distance

    def get_color(self):
        return self.color

    def __str__(self):
        return (str(self.id))

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbour):
        return self.connected_to[neighbour]

class Graph:
    def __init__(self):
        self.vert_list = {}
        self.vert_nbr = 0

    def add_vertex(self, key):
        self.vert_nbr = self.vert_nbr + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def add_vertices_from_list(self, vertices):
        for vertex in vertices:
            self.add_vertex(vertex)

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def __contains__(self, item):
        return item in self.vert_list

    def add_edge(self, f, t, weight=0):
        """
        f = edge origin
        t = edge destination
        weight = weight of the edge (default 0)
        """
        if isinstance(f, Vertex):
            f = f.get_id()
        if isinstance(t, Vertex):
            t = t.get_id()
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbour(self.vert_list[t], weight)

    def add_edges_from_list(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1], edge[2])

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def __str__(self):
        return str(self.vert_list.keys())

    def __getitem__(self, item):
        return self.vert_list[item]

    def get_neighbours(self, vertex):
        if vertex in self.vert_list:
            return list(self.vert_list[vertex].get_connections())
        else:
            return []

    def to_dot(self):
        dot = "digraph G {\n"
        for vertex in self.vert_list.values():
            for neighbour in vertex.get_connections():
                dot += f'    {vertex.get_id()} -> {neighbour.get_id()} [label="{vertex.get_weight(neighbour)}"];\n'
        dot += "}"
        return dot

    def draw(self, output_file="graph"):
        dot = Digraph()

        for vertex in self.vert_list.values():
            dot.node(str(vertex.get_id()))  # Dodaj wierzchołek
            for neighbour in vertex.get_connections():
                dot.edge(
                    str(vertex.get_id()),
                    str(neighbour.get_id()),
                    label=str(vertex.get_weight(neighbour))
                )

        dot.render(output_file, format="png", cleanup=True)
        print(f"Graf został zapisany jako {output_file}.png")

    def bfs(self, start):
        visited = []
        start.set_distance(0)
        start.set_predecessor(None)
        vert_queue = Queue()
        vert_queue.enqueue(start)
        while vert_queue._size > 0:
            current_vert = vert_queue.dequeue()
            for nbr in current_vert.get_connections():
                if nbr.get_color() == 'white':
                    nbr.set_color('gray')
                    visited.append(nbr.__str__())
                    nbr.set_predecessor(current_vert)
                    vert_queue.enqueue(nbr)
            current_vert.set_color('black')
        return visited

    def dfs(self, start):
        visited = []
        stack = []

        start.set_distance(0)
        start.set_predecessor(None)
        stack.append(start)

        while stack:
            current_vert = stack.pop()
            if current_vert.get_color() == 'white':
                current_vert.set_color('gray')
                visited.append(current_vert.__str__())

                for nbr in current_vert.get_connections():
                    if nbr.get_color() == 'white':
                        nbr.set_predecessor(current_vert)
                        stack.append(nbr)
                current_vert.set_color('black')

        return visited

    def is_acyclic(self):
        visited = set()
        recursion_stack = set()

        def dfs(vertex):
            if vertex in recursion_stack:
                return False
            if vertex in visited:
                return True

            visited.add(vertex)
            recursion_stack.add(vertex)

            for neighbour in self.get_neighbours(vertex):
                if not dfs(neighbour.get_id()):
                    return False

            recursion_stack.remove(vertex)
            return True

        for vertex in self.get_vertices():
            if vertex not in visited:
                if not dfs(vertex):
                    return False

        return True

    def topological_sort(self):
        """
        Działa pod warunkiem, że graf jest skierowany i nie ma cykli
        """
        visited = set()
        stack = []

        def dfs_recursive(vertex):
            if vertex not in visited:
                visited.add(vertex)
                for neighbour in self.get_neighbours(vertex):
                    dfs_recursive(neighbour.get_id())
                stack.append(vertex)
        if self.is_acyclic():
            for vertex in self.get_vertices():
                if vertex not in visited:
                    dfs_recursive(vertex)
            return stack[::-1]
        else:
            print("Graf niesortowalny topologicznie")




g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_edge(1, 2)
print(g.get_neighbours(1))