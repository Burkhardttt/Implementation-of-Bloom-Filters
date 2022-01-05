import random


class CountingBloomFilter:
    """CountingBloomFilter"""
    def __init__(self, num_of_elements, num_of_counters, num_of_hashes,
                 num_of_removed, num_of_added):
        """
        Initialize
        :param num_of_elements: number of elements to be encoded
        :param num_of_counters: number of counters in the filter
        :param num_of_hashes: number of hash functions
        :param num_of_removed: number of elements to be removed
        :param num_of_added: number of elements to be added
        """
        self.num_of_elements = num_of_elements
        self.num_of_counters = num_of_counters
        self.num_of_hashes = num_of_hashes
        self.num_of_removed = num_of_removed
        self.num_of_added = num_of_added

        self.num_of_found = 0

        self.s = [0 for i in range(self.num_of_hashes)]
        self.counter = [0 for i in range(self.num_of_counters)]
        self.elements = [0 for i in range(num_of_elements)]

        self.removed_elements = [0 for i in range(self.num_of_removed)]
        self.added_elements = [0 for i in range(self.num_of_added)]

        self.generate_k_hash_functions()
        self.generate_elements()
        self.generate_removed_elements()
        self.generate_added_elements()

    def generate_elements(self):
        for i in range(len(self.elements)):
            self.elements[i] = random.randint(0, 1000000000)

    def generate_removed_elements(self):
        for i in range(len(self.removed_elements)):
            self.removed_elements[i] = self.elements[i]

    def generate_added_elements(self):
        for i in range(len(self.added_elements)):
            self.added_elements[i] = random.randint(0, 1000000000)

    def generate_k_hash_functions(self):
        """
        List s[] to compute XOR with element
        :return:
        """
        for i in range(len(self.s)):
            self.s[i] = random.randint(0, 1000000000)

    def encode_elements(self):
        """
        Encode elements[] in the filter
        :return:
        """
        for i in range(len(self.elements)):
            for j in range(len(self.s)):
                hash_index = (self.elements[i] ^ self.s[j]) % len(self.counter)
                self.counter[hash_index] += 1

    def remove_elements(self):
        for i in range(len(self.removed_elements)):
            for j in range(len(self.s)):
                hash_index = (self.removed_elements[i] ^ self.s[j]) % len(self.counter)
                self.counter[hash_index] -= 1

    def add_elements(self):
        for i in range(len(self.added_elements)):
            for j in range(len(self.s)):
                hash_index = (self.added_elements[i] ^ self.s[j]) % len(self.counter)
                self.counter[hash_index] += 1

    def look_up(self, element):
        """
        To look up whether an element is in the filter
        :return:
        """
        for i in range(len(self.s)):
            hash_index = (element ^ self.s[i]) % len(self.counter)
            if self.counter[hash_index] == 0:
                return False
        self.num_of_found += 1
        return True


if __name__ == "__main__":

    num_of_elements = int(input("Please input the number of elements: "))
    num_of_removed = int(input("Please input the number of elements to be removed: "))
    num_of_added = int(input("Please input the number of elements to be added: "))
    num_of_counters = int(input("Please input the number of counters: "))
    num_of_hashes = int(input("Please input the number of hashes: "))

    cbf = CountingBloomFilter(num_of_elements, num_of_counters, num_of_hashes, num_of_removed, num_of_added)
    cbf.encode_elements()
    cbf.remove_elements()
    cbf.add_elements()

    result = []
    for i in range(len(cbf.elements)):
        result.append(cbf.look_up(cbf.elements[i]))

    print()
    doc = open('output2.txt', 'w')
    print("By looking up of elements in set A, "
          "the number of elements in the filter is: " + str(cbf.num_of_found))
    print("By looking up of elements in set A, "
          "the number of elements in the filter is: " + str(cbf.num_of_found), file=doc)






