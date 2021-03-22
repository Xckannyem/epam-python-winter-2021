"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.
The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods getitem, setitem, delitem.
Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""


class Item:
    """
    A node in a unidirectional linked list.
    """

    def __init__(self, *data):
        self._data = data


class CustomList:
    """
    An unidirectional linked list.
    """

    def __init__(self, *values):
        """Initialize the class"""
        super(CustomList, self).__init__()
        self._list = list(values)

    # Add and remove elements.
    def append(self, value):
        self._list.append(value)

    def add_start(self, value):
        index = 0
        self._list.insert(index, value)

    def remove(self, value):
        if value in self:
            self._list.remove(value)
        else:
            raise Exception('Didn\'t find specific value')

    # Operations with elements by index.
    def __getitem__(self, index):
        if index in range(len(self)):
            return self._list[index]
        else:
            raise Exception('Index out of bound')

    def __setitem__(self, index, data):
        if index in range(len(self)):
            self._list[index] = data
            return data
        else:
            raise Exception('Index out of bound')

    def __delitem__(self, index):
        if index in range(len(self)):
            del self._list[index]
        else:
            raise Exception('Index out of bound')

    # Receive index of predetermined value.
    def find(self, value):
        if value in self:
            return self._list.index(value)
        else:
            raise Exception('Didn\'t find specific value')

    # Clear the list.
    def clear(self):
        return self._list.clear()

    # Receive list length.
    def __len__(self):
        return len(self._list)

    def __iter__(self):
        return iter(self._list)

    def __str__(self):
        return str(self._list)


if __name__ == '__main__':
    foo = CustomList(1, 2, 3, 4, 5, 7)
