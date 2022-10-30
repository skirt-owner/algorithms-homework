"""
Корнем ациклического орграфа называется вершина r такая, что
существуют пути, исходящие из этой вершины и достигающие всех
остальных вершин орграфа. Напишите программу, определяющую,
имеет ли данный ациклический орграф корень и вывести его на
экран.

Матрица смежности.

1. FIRST(v) - возвращает индекс первой вершины, смежной с вершиной v. Если вершина v не
имеет смежных вершин, то возвращается "нулевая" вершина .
2. NEXT(v, i)- возвращает индекс вершины, смежной с вершиной v, следующий за индексом i.
Если i — это индекс последней вершины, смежной с вершиной v, то возвращается .
3. VERTEX(v, i) - возвращает вершину с индексом i из множества вершин, смежных с v.
4. ADD_V(<имя>,<метка, mark>) - добавить УЗЕЛ
5. ADD_Е(v, w, c) - добавить ДУГУ (здесь c — вес, цена дуги (v,w))
6. DEL_V(<имя>) - удалить УЗЕЛ
7. DEL_Е(v, w) – удалить ДУГУ
8. EDIT_V(<имя>, <новое значение метки или маркировки>) - изменить метку (маркировку)
УЗЛА
EDIT_Е(v, w, <новый вес дуги>) - изменить вес ДУГИ
"""

class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
    def __str__(self):
        return str(self.weight)

class Vertex:
    def __init__(self, id, label):
        self.id = id
        self.label = label
        self.edges = list()
    def append(self, edge):
        self.edges.append(edge)
    def pop(self, index):
        self.edges.pop(index)
    def __getitem__(self, index):
        return self.edges[index]
    def __len__(self):
        return len(self.edges)
    def __str__(self):
        return " ".join(map(str, self))

class Graph:
    def __init__(self):
        self.vertices = list()

    def addVertex(self, id, label):
        if id not in self:
            new_vertex = Vertex(id, label)
            for i in range(len(self)):
                self[i].append(Edge(self[i], new_vertex, 0))
            self.append(new_vertex)
            for i in range(len(self)):
                self[-1].append(Edge(new_vertex, self[i], 0))
        else:
            raise Exception(f"Vertex with id:{id} already exists.")

    def editVertex(self, id, new_label):
        if id in self:
            for vertex in self:
                if vertex.id == id:
                    break
            vertex.label = new_label
        else:
            raise Exception(f"There is no vertex with id:{id}.")

    def deleteVertex(self, id):
        if id in self:
            for i in range(len(self)):
                if self[i].id == id:
                    break
            self.pop(i)
            for i in range(len(self)):
                self[i].pop(-1)
        else:
            raise Exception(f"There is no vertex with id:{id}.")

    def addEdge(self, id1, id2, weight):
        for i in range(len(self)):
            if self[i].id == id1:
                break
        for j in range(len(self)):
            if self[j].id == id2:
                break

        if self[i][j].weight == 0:
            self[i][j].weight = weight
        else:
            raise Exception(f"Edge between {id1}-{id2} already exists.")

    def editEdge(self, id1, id2, new_weight):
        for i in range(len(self)):
            if self[i].id == id1:
                break
        for j in range(len(self)):
            if self[j].id == id2:
                break

        if self[i][j].weight != 0:
            self[i][j].weight = new_weight
        else:
            raise Exception(f"There is no edge between {id1}-{id2}.")

    def deleteEdge(self, id1, id2):
        for i in range(len(self)):
            if self[i].id == id1:
                break
        for j in range(len(self)):
            if self[j].id == id2:
                break

        if self[i][j].weight!= 0:
            self[i][j].weight = 0
        else:
            raise Exception(f"There is no edge between {id1}-{id2}.")

    def getVertex(self, id, index):
        for i in range(len(self)):
            if self[i].id == id:
                break
        conns = []
        for j in range(len(self[i])):
            if self[i][j].weight != 0:
                conns.append(self[i][j].v2)
        return conns[index]

    def firstVertex(self, id):
        for i in range(len(self)):
            if self[i].id == id:
                break
        for j in range(len(self[i])):
            if self[i][j].weight != 0:
                return j
        return Vertex(None, None)

    def nextVertex(self, id, index):
        for i in range(len(self)):
            if self[i].id == id:
                break
        for j in range(len(self[i])):
            if self[i][j].weight != 0 and j > index:
                    return j
        return Vertex(None, None)

    def getRoots(self, vertex):
        self.editVertex(vertex.id, True)

        for j in range(len(vertex)):
            next_vertex = vertex[j].v2
            if not next_vertex.label and vertex[j].weight > 0:
                self.getRoots(next_vertex)

    def dfs(self, id):
        for i in range(len(self)):
            if self[i].id == id:
                break
        vertex = self[i]

        self.getRoots(vertex)

        isRoot = True
        for i in range(len(self)):
            if self[i].label != True:
                isRoot = False

        for i in range(len(self)):
            self[i].label = False

        if isRoot:
            return True, id
        return False, id

    def append(self, vertex):
        self.vertices.append(vertex)
    def pop(self, index):
        self.vertices.pop(index)

    def __getitem__(self, index):
        return self.vertices[index]
    def __len__(self):
        return len(self.vertices)
    def __contains__(self, id):
        return id in map(lambda obj: obj.id, self)
    def __str__(self):
        template = ""
        for i in range(len(self)+1):
            template += "{"+str(i)+":3}"
        first_row = [" "]
        for i in range(len(self)):
            first_row.append(str(self[i].id))
        string = template.format(*first_row)+"\n"
        for i in range(len(self)):
            next_row = [str(i)]
            for j in range(len(self[i])):
                next_row.append(str(self[i][j]))
            string += template.format(*next_row)+"\n"
        return string

g = Graph()
g.addVertex(0, False)

g.addVertex(1, False)

g.addVertex(2, False)

g.addVertex(3, False)

g.addVertex(4, False)

g.addVertex(5, False)

g.addVertex(6, False)

g.addVertex(7, False)

g.addVertex(8, False)

g.addVertex(9, False)

g.addVertex(10, False)

g.addVertex(11, False)

g.addVertex(12, False)

g.addEdge(7, 8, 1)
g.addEdge(6, 7, 1)

g.addEdge(6, 4, 1)
g.addEdge(6, 9, 1)
g.addEdge(4, 9, 1)
g.addEdge(3, 4, 1)
g.addEdge(3, 5, 1)
g.addEdge(2, 3, 1)
g.addEdge(0, 6, 1)
g.addEdge(0, 2, 1)
g.addEdge(0, 1, 1)
g.addEdge(0, 3, 1)
g.addEdge(0, 5, 1)
g.addEdge(9, 10, 1)
g.addEdge(9, 11, 1)
g.addEdge(9, 12, 1)
g.addEdge(11, 12, 1)

for i in range(9):
    print(g.dfs(i))

print(g)

# class Edge:
#     def __init__(self, id1, id2, weight):
#         self.id1 = id1
#         self.id2 = id2
#         self.weight = weight

# class Vertex:
#     def __init__(self, id, label):
#         self.id = id
#         self.label = label
#         self.edges = list()

#     def remove(self, id2):
#         self.edges.remove(self[id2])
#     def __len__(self):
#         return len(self.edges)
#     def __iter__(self):
#         for edge in self.edges:
#             yield edge
#     def __contains__(self, id2):
#         for edge in self:
#             if edge.id2 == id2:
#                 return True
#         return False
#     def __call__ (self, edge):
#         self.edges.append(edge)
#     def __setitem__(self, id2, weight):
#         self[id2].weight = weight
#     def __getitem__(self, id2):
#         if type(id2) == int:
#             return self.edges[id2]
#         for edge in self:
#             if edge.id2 == id2:
#                 return edge
#         return None

# class Graph:
#     def __init__(self):
#         self.vertices = list()

#     def first(self, id):
#         array = [edge for edge in self[id]]
#         if len(array) == 0:
#             return Vertex(None, None)
#         array.sort(key=lambda i: i.weight)
#         vertex = self[array[0].id2]
#         return self.vertices.index(vertex)

#     def next(self, id, i):
#         return self.vertices.index(self.getVertex(id, i))

#     def getVertex(self, id1, i):
#         return self[self[id1][i].id2]

#     def addVertex(self, id, label):
#         if id not in self:
#             new_vertex = Vertex(id, label)
#             self(new_vertex)
#         else:
#             raise Exception(f"Vertex with id:{id} is already existed!")

#     def addEdge(self, id1, id2, weight):
#         if id2 not in self[id1]:
#             new_edge = Edge(id1, id2, weight)
#             self[id1](new_edge)
#         else:
#             raise Exception(f"Edge between {id1}-{id2} is already existed!")

#     def editVertex(self, id, new_label):
#         self[id] = new_label

#     def editEdge(self, id1, id2, weight):
#         self[id1][id2] = weight

#     def deleteVertex(self, id):
#         if id in self:
#             for edge in self[id]:
#                 self.deleteEdge(edge.id1, edge.id2)
#             for vertex in self:
#                 for edge in vertex:
#                     if edge.id2 == id:
#                         self.deleteEdge(edge.id1, edge.id2)
#             self.remove(id)
#         else:
#             raise Exception(f"There is no vertex with id:{id}!")

#     def deleteEdge(self, id1, id2):
#         if id2 in self[id1]:
#             self[id1].remove(id2)
#         else:
#             raise Exception(f"There is no edge between {edge.id1}-{edge.id2}!")

#     def remove(self, id):
#         self.vertices.remove(self[id])
#     def __len__(self):
#         return len(self.vertices)
#     def __iter__(self):
#         for vertex in self.vertices:
#             yield vertex
#     def __contains__(self, id):
#         for vertex in self:
#             if vertex.id == id:
#                 return True
#         return False
#     def __call__(self, vertex):
#         self.vertices.append(vertex)
#     def __setitem__(self, id, label):
#         self[id].label = label
#     def __getitem__(self, id):
#         if type(id) == int:
#             return self.vertices[id]
#         for vertex in self:
#             if vertex.id == id:
#                 return vertex
#         return None

# g = Graph()
# g.addVertex("A", "a")
# g.addVertex("B", "b")
# g.addVertex("C", "c")
# g.addEdge("A", "B", 2)
# g.addEdge("A", "C", 4)
# print(g.next("A", 0))

