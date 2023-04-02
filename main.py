# python3
# Egija Kokoreviča 	221RDB288

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.s = query[1]
        if self.type == 'add':
            self.name = query[2]

class HashTable:
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]
        self._prime = 100000000
        self._multiplier = 263

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime 
        return ans % self.bucket_count

    def add(self, string, name):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i][0] == string:
                bucket[i] = (string, name)
                return
        self.buckets[hashed].append((string, name))

    def delete(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i][0] == string:
                bucket.pop(i)
                break

    def find(self, string):
        hashed = self._hash_func(string)
        for key, name in self.buckets[hashed]:
            if key == string:
                return name
        return "not found"

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    phone_book = HashTable(100000)
    for query in queries:
        if query.type == 'add':
            phone_book.add(query.s, query.name)
        elif query.type == 'del':
            phone_book.delete(query.s)
        else:
            response = phone_book.find(query.s)
            result.append(response if response != None else "not found")
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
