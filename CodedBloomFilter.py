import random
import math


class Set:

    def __init__(self, num_of_elements_each_set):
        """
        Initialize each Set
        :param num_of_elements_each_set: ***
        """
        self.set_id = 0
        self.set_code = str(bin(self.set_id))[2:]  # ex. make '0b111' be '111'
        self.elements = [0 for i in range(num_of_elements_each_set)]
        self.generate_elements()

    def generate_elements(self):
        for i in range(len(self.elements)):
            self.elements[i] = random.randint(0, 1000000000)
            if self.elements[i] in self.elements:
                i -= 1
                continue


class Filter:

    def __init__(self, num_of_bits_each_filter):
        """
        Initialize each Filter
        :param num_of_bits_each_filter:
        """
        self.filter_id = 0
        self.bitmap = [0 for i in range(num_of_bits_each_filter)]


class CodedBloomFilter:
    """CodedBloomFilter"""
    def __init__(self, num_of_sets, num_of_elements_each_set,
                 num_of_filters, num_of_bits_each_filter,
                 num_of_hashes):

        self.num_of_sets = num_of_sets  # 7
        self.num_of_elements_each_set = num_of_elements_each_set  # 1000
        self.num_of_filters = num_of_filters  # 3
        self.num_of_hashes = num_of_hashes  # 7
        self.num_of_bits_each_filter = num_of_bits_each_filter

        self.num_of_found = self.num_of_sets * self.num_of_elements_each_set  # 假设都能找到
        self.set_code_length = math.ceil(math.log2(self.num_of_sets + 1))

        self.s = [0 for i in range(self.num_of_hashes)]
        self.sets = [Set(self.num_of_elements_each_set)
                     for i in range(self.num_of_sets)]
        self.filters = [Filter(self.num_of_bits_each_filter)
                        for i in range(self.num_of_filters)]

        self.generate_k_hashes()

    def generate_k_hashes(self):
        for i in range(len(self.s)):
            self.s[i] = random.randint(0, 1000000000)

    def setup_all_sets(self):
        """
        Initialize set_id and set_code for each set
        :return:
        """
        for i in range(self.num_of_sets):
            self.sets[i].set_id = i + 1
            self.sets[i].set_code = str(bin(self.sets[i].set_id)[2:])
            while len(self.sets[i].set_code) < self.num_of_filters:
                self.sets[i].set_code = '0' + self.sets[i].set_code

    def setup_all_filters(self):
        """
        Initialize filter_id for each filter
        :return:
        """
        for i in range(self.num_of_filters):
            self.filters[i].filter_id = i + 1

    def encode_elements(self):
        """
        Encode elements[] of one set to a filter
        :return:
        """
        for i in range(self.num_of_sets):
            for j in range(self.set_code_length):
                if self.sets[i].set_code[j] == "1":
                    for k in range(self.num_of_elements_each_set):
                        for m in range(len(self.s)):
                            hash_index = (self.sets[i].elements[k] ^ self.s[m]) \
                                         % self.num_of_bits_each_filter
                            if self.filters[j].bitmap[hash_index] != 1:
                                self.filters[j].bitmap[hash_index] = 1

    def look_up(self, element, filter):
        """
        To look up whether an element is in the filter
        :param element:
        :return:
        """
        for i in range(len(self.s)):
            hash_index = (element ^ self.s[i]) % self.num_of_bits_each_filter
            if filter.bitmap[hash_index] != 1:
                return False
        return True


if __name__ == "__main__":

    num_of_sets = int(input("Please input the number of sets: "))
    num_of_elements_each_set = int(input("Please input the number of elements each set: "))
    num_of_filters = int(input("Please input the number of filters: "))
    num_of_bits_each_filter = int(input("Please input the number of bits each filter: "))
    num_of_hashes = int(input("Please input the number of hashes: "))

    cobf = CodedBloomFilter(num_of_sets, num_of_elements_each_set,
                            num_of_filters, num_of_bits_each_filter, num_of_hashes)
    cobf.setup_all_sets()
    cobf.setup_all_filters()
    cobf.encode_elements()

    # print(type(cobf.sets[6].set_code[0]))
    # print(cobf.set_code_length)
    # print(cobf.filters[1].bitmap)

    doc = open('output3.txt', 'w')
    # looking up process
    for i in range(cobf.num_of_sets):
        for j in range(cobf.set_code_length):
            if cobf.sets[i].set_code[j] == "0":
                for k in range(cobf.num_of_elements_each_set):
                    if cobf.look_up(cobf.sets[i].elements[k], cobf.filters[j]):
                        cobf.num_of_found -= 1
    print()
    print("The number of elements whose lookup results are correct: " + str(cobf.num_of_found))
    print("The number of elements whose lookup results are correct: " + str(cobf.num_of_found), file=doc)




















