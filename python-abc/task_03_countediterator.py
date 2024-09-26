#!/usr/bin/python3


class CountedIterator:

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with the given iterable.

        :param iterable: An iterable (like a list or a tuple) to iterate over.
        """
        self.iterable = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        Retrieve the next item from the iterable and increment the counter.

        :return: The next item in the iterable.
        :raises StopIteration: When there are no more items to iterate over.
        """
        item = next(self.iterable)
        self.counter += 1
        return item

    def get_count(self):
        """
        Get the current count of items that have been iterated over.

        :return: The number of items returned by __next__.
        """
        return self.counter
