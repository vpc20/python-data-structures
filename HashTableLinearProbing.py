ASCII_A = 65


class HashTable:
    def __init__(self, size):
        self.hash_table = []
        for i in range(size):
            self.hash_table.append([])

    def get_hash_table(self):
        return self.hash_table

    @staticmethod
    def hash_value(key):
        return ord(key[0].upper()) - ASCII_A

    def insert(self, key, value):
        hash_val = self.hash_value(key)
        if not self.hash_table[hash_val]:
            self.hash_table[hash_val] = [key, value]
        else:  # collision occured, find the next avalable slot
            for i in range(hash_val + 1, len(self.hash_table)):
                if not self.hash_table[i]:
                    self.hash_table[i] = [key, value]
                    return

    def search(self, key):
        hash_val = self.hash_value(key)
        if self.hash_table[hash_val][0] == key:
            return self.hash_table[hash_val][0], self.hash_table[hash_val][1]
        else:
            for i in range(hash_val + 1, len(self.hash_table)):
                if not self.hash_table[i]:
                    return None
                if self.hash_table[i][0] == key:
                    return self.hash_table[i][0], self.hash_table[i][1]


ht = HashTable(26)
ht.insert('Allan', 'Engineer')
ht.insert('Beth', 'Nutritionist')
ht.insert('Charlie', 'Painter')
ht.insert('Ben', 'Musician')
ht.insert('Brad', 'Professor')
print(ht.get_hash_table())

print(ht.search('Bradx'))
