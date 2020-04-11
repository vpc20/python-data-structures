class HashTable:
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.hash_table = [[] for _ in range(bucket_count)]

    def insert(self, key, value):
        bucket_pos = self.hash_value(key)  # compute for bucket position
        self.hash_table[bucket_pos].append([key, value])

    def hash_value(self, string):
        sum_ch_ord = sum([ord(ch) for ch in string])
        return sum_ch_ord % self.bucket_count

    def search(self, key):
        bucket_pos = self.hash_value(key)  # compute for bucket position
        for k, v in self.hash_table[bucket_pos]:
            if k == key:
                return v
        return -1

    def get_hash_table(self):
        return self.hash_table


ht = HashTable(5)
# print ht.get_hash_table()
# print ht.hash_value('a')

ht.insert('a', 1)
ht.insert('b', 2)
ht.insert('c', 3)
ht.insert('d', 4)
ht.insert('e', 5)
ht.insert('f', 6)
# ht.insert(1, 6)

print(ht.get_hash_table())

print(ht.search('a'))
print(ht.search('b'))
print(ht.search('c'))
print(ht.search('d'))
print(ht.search('e'))
print(ht.search('f'))
print(ht.search('g'))
# print ht.get_hash_table()[2][1]
