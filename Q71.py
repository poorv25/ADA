import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        return self.freq < other.freq
        
class HuffmanCode:
    def __init__(self):
        self.freq = defaultdict(int)
        self.codes = {}

    def get_frequency(self, data):
        for char in data:
            self.freq[char] += 1

    def build_tree(self):
        nodes = []
        for char, freq in self.freq.items():
            nodes.append(HuffmanNode(char, freq))

        heapq.heapify(nodes)

        while len(nodes) > 1:
            node1 = heapq.heappop(nodes)
            node2 = heapq.heappop(nodes)

            parent = HuffmanNode(None, node1.freq + node2.freq, node1, node2)

            heapq.heappush(nodes, parent)

        return nodes[0]

    def traverse_tree(self, node, code):
        if node.char:
            self.codes[node.char] = code
            return

        self.traverse_tree(node.left, code + "0")
        self.traverse_tree(node.right, code + "1")

    def get_encoded_data(self, data):
        encoded_data = ""

        for char in data:
            encoded_data += self.codes[char]

        return encoded_data

    def compress(self, data):
        self.get_frequency(data)
        root = self.build_tree()
        self.traverse_tree(root, "")
        encoded_data = self.get_encoded_data(data)

        return encoded_data
