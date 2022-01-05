import random


class BloomFilter:
    """BloomFilter"""
    def __init__(self, num_of_elements, num_of_bits, num_of_hashes):
        """
        Initialize the BloomFilter
        :param num_of_elements: number of elements to be encoded
        :param num_of_bits: number of bits in the filter
        :param num_of_hashes: number of hash functions
        """
        self.num_of_elements = num_of_bits
        self.num_of_bits = num_of_bits
        self.num_of_hashes = num_of_hashes

        self.num_of_found = 0

        self.s = [0 for i in range(self.num_of_hashes)]
        self.bitmap = [0 for i in range(self.num_of_bits)]
        self.elements = [0 for i in range(num_of_elements)]

        self.generate_k_hash_functions()
        self.generate_elements()

    def generate_elements(self):
        for i in range(len(self.elements)):
            self.elements[i] = random.randint(0, 1000000000)

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
                hash_index = (self.elements[i] ^ self.s[j]) % len(self.bitmap)
                if self.bitmap[hash_index] != 1:
                    self.bitmap[hash_index] = 1

    def look_up(self, element):
        """
        To look up whether an element is in the bitmap
        :return:
        """
        for i in range(len(self.s)):
            hash_index = (element ^ self.s[i]) % len(self.bitmap)
            if self.bitmap[hash_index] != 1:
                return False
        self.num_of_found += 1
        return True


if __name__ == "__main__":

    num_of_elements = int(input("Please input the number of elements: "))
    num_of_bits = int(input("Please input the number of bits: "))
    num_of_hashes = int(input("Please input the number of hashes: "))
    bf = BloomFilter(num_of_elements, num_of_bits, num_of_hashes)
    bf.encode_elements()
    # print(bf.elements)
    # print(bf.s)
    # print(bf.bitmap)

    # output file
    doc = open('output1.txt', 'w')
    print()
    # look up setA, print the result
    result_a = []
    for i in range(len(bf.elements)):
        result_a.append(bf.look_up(bf.elements[i]))
    # print(result_a)
    # print(bf.num_of_found)
    print("By looking up of elements in set A, "
          "the number of elements in the filter is: " + str(bf.num_of_found))
    print("By looking up of elements in set A, "
          "the number of elements in the filter is: " + str(bf.num_of_found), file=doc)

    bf.num_of_found = 0
    # print()

    # look up setB, print the result
    bf.generate_elements()
    # print(bf.elements)
    result_b = []
    for i in range(len(bf.elements)):
        result_b.append(bf.look_up(bf.elements[i]))
    # print(result_b)
    # print(bf.num_of_found)

    print("By looking up of elements in set B, "
          "the number of elements in the filter is: " + str(bf.num_of_found))
    print("By looking up of elements in set B, "
          "the number of elements in the filter is: " + str(bf.num_of_found), file=doc)

















