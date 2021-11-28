class Node:
    def __init__(self, value, child, parent):
        self._value = value
        self._child = child
        self._parent = parent

    def get_value(self):
        #Return the value of a node
        return self._value

    def get_child(self):
        #Return the value of a node
        return self._child

    def get_parent(self):
        #Return the parent of a node
        return self._parent

    def set_value(self, value):
        #Change the value of a node
        self._value = value

    def set_child(self, child):
        #Change the value of a node
        self._child = child

    def set_parent(self, parent):
        #Change the parent reference
        self._parent = parent