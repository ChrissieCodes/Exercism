# {"value":[], "next":node
# }
class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next
    

class LinkedList:
    def __init__(self, values=[]):
        self._head=None
        
        for i in values:
            self.push(i)

    def __iter__(self):
        self._walk = self._head
        return self
    
    def __next__(self):
        if not self._walk:
            raise StopIteration
        current_node=self._walk
        self._walk = current_node._next
        self._value = current_node._value
        return self._value
        
    
    def __len__(self):
        try:
            current_node = self.head()
        except EmptyListException:
            return 0
        i = 1
        while current_node._next is not None:
            i += 1
            current_node = current_node._next
        return i
    

    def head(self):
        if self._head is not None:
            return self._head
        raise EmptyListException("The list is empty.")
        

    def push(self, value):
        node = Node(value)
        if len(self) == 0:
            self._head = node
        else:
            node._next = self.head()
            self._head = node

    def pop(self):
        old_head = self.head()
        if old_head is not None:
            self._head = old_head.next()
            return old_head.value()
        raise EmptyListException("The list is empty.")

    def reversed(self):
        return LinkedList(list(self))
            

class EmptyListException(Exception):
    pass


if __name__ == "__main__":
    for i in LinkedList([1,2]):
        print(dir(i),i)
