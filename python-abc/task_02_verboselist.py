#!/usr/bin/python3


from typing import Iterable


class VerboseList(list):
    """A list that provides verbose output on certain operations."""
    def append(self, item):
        """Add an item to the end of the list and print a message.

        Args:
            item: The item to be added to the list.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable: Iterable):
        """Extend the list by appending elements from
        the iterable and print a message.
        Args:
            iterable: An iterable (like a list or tuple)
            containing items to be added.
        """
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """Remove the first occurrence of a value from
        the list and print a message.

        Args:
            value: The item to be removed from the list.

        Raises:
            ValueError: If the value is not found in the list.
        """
        super().remove(item)
        print(f'Removed [{item}] from the list.')

    def pop(self, index=-1):
        """Remove and return an item at the given index and print a message.

        Args:
            index: The index of the item to be removed
            (default is -1, which pops the last item).

        Returns:
            The item that was removed from the list.

        Raises:
            IndexError: If the list is empty or the index is out of range.
        """
        item = super().pop(index)
        print(f'Popped [{item}] from the list.')
        return item
