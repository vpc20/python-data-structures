class DisjointSet:
    def __init__(self):
        self.disj_list = list()

    def make_set(self, e):
        self.disj_list.append({e})

    def find_set(self, e):
        for disj_set in self.disj_list:
            if e in disj_set:
                return disj_set
        return None

    def union(self, set1, set2):
        self.disj_list.append(set().union(set1, set2))
        self.disj_list.remove(set1)
        self.disj_list.remove(set2)


if __name__ == '__main__':
    djset = DisjointSet()
    djset.make_set('a')
    djset.make_set('b')
    djset.make_set('c')
    djset.make_set('d')
    djset.make_set('e')
    djset.make_set('f')
    djset.make_set('g')
    djset.make_set('h')
    djset.make_set('i')
    djset.make_set('j')

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
