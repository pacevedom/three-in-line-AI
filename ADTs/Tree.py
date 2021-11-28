from Node import Node

class Tree:
    def __init__(self, nodes, values, parent_node):
        self._nodes = nodes
        self._values = values
        self._parent_node = parent_node

        for index in range(0, len(self._nodes)-1):
            self._nodes[index].set_parent(self._parent_node)
            self._nodes[index].set_value(self._values[index])