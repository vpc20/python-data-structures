from collections import defaultdict


class DisjointSet:
    # def __init__(self):
    #     self.disj_list = list()
    #
    # def make_set(self, e):
    #     self.disj_list.append({e})
    #
    # def find_set(self, e):
    #     for disj_set in self.disj_list:
    #         if e in disj_set:
    #             return disj_set
    #     return None
    #
    # def union(self, set1, set2):
    #     self.disj_list.append(set().union(set1, set2))
    #     self.disj_list.remove(set1)
    #     self.disj_list.remove(set2)

    def __init__(self):
        self.parent = {}

    def make_set(self, x):
        self.parent[x] = x

    def find_set(self, x):
        return self.parent[x]

    def union(self, x, y):
        py = self.parent[y]  # save value as this could be updated in loop below
        for k in self.parent:
            if self.parent[k] == py:
                self.parent[k] = self.parent[x]

    def get_set(self):
        conn_comps = defaultdict(set)
        for k, v in self.parent.items():
            conn_comps[v].add(k)
        return list(conn_comps.values())


if __name__ == '__main__':
    djset = DisjointSet()
    djset.make_set(1)
    djset.make_set(2)
    djset.make_set(3)
    djset.make_set(4)
    djset.make_set(5)
    djset.make_set(6)
    djset.make_set(7)
    # print(djset.parent)
    print(djset.get_set())

    djset.union(1, 2)
    print(djset.get_set())
    djset.union(4, 5)
    print(djset.get_set())
    djset.union(1, 5)
    print(djset.get_set())
    djset.union(6, 7)
    print(djset.get_set())
    djset.union(4, 6)
    print(djset.get_set())

    # for edge1, edge2 in [('b', 'd'), ('e', 'g'), ('a', 'c'), ('h', 'i'),
    #                      ('a', 'b'), ('e', 'f'), ('b', 'c')]:
    #     set1 = djset.find_set(edge1)
    #     set2 = djset.find_set(edge2)
    #     if set1 != set2:
    #         djset.disj_list.append(djset.union(set1, set2))
    #         djset.disj_list.remove(set1)
    #         djset.disj_list.remove(set2)
    # print(djset.disj_list)

    # disjoint_list = [{1}, {2}, {3}, {4}, {5}]
    # x = find_set(disjoint_list, 3)
    # disjoint_list.remove(x)
    # print(disjoint_list)

    # disjoint_list = [{1}, {2}, {3}, {4}, {5}]
    # set1 = disjoint_list[0]
    # set2 = disjoint_list[2]
    # disjoint_list.append((set1.union(set2)))
    # disjoint_list.remove(set1)
    # disjoint_list.remove(set2)
    # print(disjoint_list)
