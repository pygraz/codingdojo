"""
Huffman code tree
=================

Huffman coding consists of the creation of a binary tree with signs from the
original data stream as leafs and receiving paths with their length being
indirectly proportional to their frequency. If a sign is very frequent in the
original stream it will receive a short path which in turn will result in a
sequence of 0s and 1s (left turn and right turn in the binary tree).

The tree is generated in an iterative fashion using weighted queues. First
all signs are put into the queue which is then sorted with least frequent
one in the front.

The first two are picked as leafs and a common parent node is created receiving
combined weight of its two leafs. This is then added to the queue again, which
is sorted again and the process repeats until only one node is left in the queue.
This is the root node of the tree.

The ``build_tree`` function receives the raw stream (in our case a simple string)
and should return tree that exposes a ``find`` method. This method gets passed
a sign and returns a list of 0s and 1s representing the path that sign can be
accessed from the root of the tree.

"""
import collections

Node = collections.namedtuple('Node', ['sign','frequency','left','right'])

class FindableQueue(object):
    def __init__(self, root_node):
        self.sign_to_frequency_map = {}
        self._sign_to_frequency_map(root_node)



    def _sign_to_frequency_map(self, node, path=""):
        if node.left and node.right:
            self._sign_to_frequency_map(node.left,path+"0")
            self._sign_to_frequency_map(node.right,path+"1")
        else:
            self.sign_to_frequency_map[node.sign]=path

    def find(self, sign):
        print(self.sign_to_frequency_map)
        return self.sign_to_frequency_map[sign]

def node_from_tuple(sign_and_frequency):
    sign,frequency = sign_and_frequency
    return Node(sign, frequency,None,None)


def build_root_node(data):
    f = collections.Counter(data)
    nodes_sorted_by_frequency = [node_from_tuple(sign_and_frequency) for sign_and_frequency in f.most_common()]

    while len(nodes_sorted_by_frequency)!=1:
        least = nodes_sorted_by_frequency.pop()
        second_least = nodes_sorted_by_frequency.pop()
        frequency = least.frequency + second_least.frequency

        new_node = Node("", frequency, least, second_least)
        nodes_sorted_by_frequency.append(new_node)
        nodes_sorted_by_frequency.sort(key=lambda v: v.frequency, reverse=True)

    return nodes_sorted_by_frequency[0]

def build_tree(data):
    node = build_root_node(data)
    return FindableQueue(node)

def test_very_simple_tree():
    data = "aaabbc"
    myresult = FindableQueue(build_root_node(data))
    assert len(myresult.find('a')) == 1
    assert len(myresult.find('b')) == 2
    assert len(myresult.find('c')) == 2

if __name__ == '__main__':
    print(build_tree("j'aime aller sur le bord de l'eau les jeudis ou les jours impairs"))
