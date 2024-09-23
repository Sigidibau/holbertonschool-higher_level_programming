#!/usr/bin/python3
"""MyList class that extends the built-in list with a method
to print sorted elements."""


class MyList:
    """A custom list class that inherits from the built-in list."""
    def print_sorted(self):
        """Prints the elements of the list in sorted order."""
        print(sorted(self))
