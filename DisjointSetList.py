class DisjointSet:
    def __init__(self):
        self.parent = list()
        self.rank = list()

    def make_set(self, x):
        self.parent.append(x)
        self.rank.append(0)

    def find_set(self, x):  # use path compression
        if x != self.parent[x]:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    # def find_set(self, x):  # use path compression
    #     xlist = []
    #     while x != self.parent[x]:
    #         xlist.append(x)
    #         x = self.parent[x]
    #     for i in xlist:
    #         self.parent[i] = self.parent[x]
    #     # while xlist:
    #     #     self.parent[xlist.pop()] = self.parent[x]
    #     return self.parent[x]

    def link(self, x, y):  # union by rank
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def get(self):
        return self.parent


if __name__ == '__main__':
    # g = Graph()
    # g.add_edge('a', 'b')
    # g.add_edge('a', 'c')
    # g.add_edge('b', 'c')
    # g.add_edge('b', 'd')
    # g.add_edge('e', 'f')
    # g.add_edge('e', 'g')
    # g.add_edge('h', 'i')
    # g.add_vertex('j')
    # print()
    djset = DisjointSet()
    djset.make_set(0)
    djset.make_set(1)
    djset.make_set(2)
    print(djset.parent)

    # print(djset.find_set(0))
    # print(djset.find_set(1))
    # print(djset.find_set(2))

    #              [0, 1, 2, 3, 4, 5]
    djset.parent = [1, 2, 3, 4, 5, 5]
    # djset.parent = [3, 2, 3, 4, 5, 5]
    print(djset.parent)
    print(djset.find_set(0))
    print(djset.parent)
