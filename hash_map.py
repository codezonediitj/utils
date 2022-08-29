class Dict:

    __slots__ = ['n', 'capacity', 'key_list', 'value_list',
                 'collisions', 'load_factor', 'hashes', 'config',
                 'hash_function', 'prob_length', 'hash_calls']

    def __init__(self, hash_function_):
        self.n = 0
        self.capacity = 0
        self.key_list = []
        self.value_list = []
        self.collisions = 0
        self.load_factor = 0.6
        self.hashes = set()
        self.config = {'p': 31, 'm': 10**9 + 9}
        self.hash_function = hash_function_
        self.prob_length = 0
        self.hash_calls = 0

    def hash(self, key):
        self.hash_calls += 1
        hash_value = self.hash_function(self, key) % self.capacity
        self.hashes.add(hash_value % self.capacity)
        return hash_value

    def rehash_if_needed(self):
        if self.capacity > 0 and (self.n + 1)/self.capacity < self.load_factor:
            return None
        self.hashes.clear()
        self.capacity = 2 * len(self.key_list) + 1
        new_key_list = [None for _ in range(self.capacity)]
        new_value_list = [None for _ in range(self.capacity)]
        for key, value in zip(self.key_list, self.value_list):
            if key != None:
                self._write(key, value, new_key_list, new_value_list)
        del self.key_list
        del self.value_list
        self.key_list = new_key_list
        self.value_list = new_value_list

    def _write(self, key, value, key_list_, value_list_):
        key_hash = self.hash(key)
        self.collisions += int(not (key_list_[key_hash] == key or key_list_[key_hash] == None))
        pos = key_hash
        self.prob_length += 1
        while key_list_[pos] != None and key_list_[key_hash] != key:
            pos = (pos + 1) % self.capacity
            self.prob_length += 1
        key_list_[pos] = key
        value_list_[pos] = value
        self.n += 1

    def write(self, key, value):
        self.rehash_if_needed()
        self._write(key, value, self.key_list,
                    self.value_list)

    def read(self, key):
        key_hash = self.hash(key)
        pos = key_hash
        self.prob_length += 1
        while self.key_list[pos] != key:
            pos = (pos + 1) % self.capacity
            self.prob_length += 1
        return self.value_list[pos]

def polynomial_rolling(self, key):
    p = self.config['p']
    m = self.config.get('m', self.capacity)
    hash_value = 0
    p_pow = 1
    for c in key:
        hash_value = (hash_value + (ord(c) + 1) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value % self.capacity

def djb2(self, key):
    hash_value = 5381
    for c in key:
        hash_value = ((hash_value << 5) + hash_value) + ord(c)
    return hash_value % self.capacity

def sdbm(self, key):
    hash_value = 0
    for c in key:
        hash_value = ord(c) + (hash_value << 6) + (hash_value << 16) - hash_value
    return hash_value % self.capacity

sizes = [1000000]
c = 1048576
max_collisions = -1
answer = 0
for size in sizes:
    d = 1
    correct = 0
    rollnumber2cpi = Dict(polynomial_rolling)
    for i in range(1000, 1000 + size, d):
        rollnumber2cpi.write(str(i + c), i)
    answer = 0
    for i in range(1000, 1000 + size, d):
        answer += rollnumber2cpi.read(str(i + c))
    assert answer == ((size - 1) * size)//2 + 1000 * size, (answer, (size - 1) * size)
    print(rollnumber2cpi.hash_function,
          rollnumber2cpi.prob_length/rollnumber2cpi.hash_calls,
          size/rollnumber2cpi.hash_calls,
          rollnumber2cpi.prob_length/size)
