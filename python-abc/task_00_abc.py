#!/usr/bin/python3
"""This module defines an abstract base class for animals
and provides concrete implementations for Dog and Cat classes.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Return the sound that the animal makes."""

        class Dog(Animal):
            """Class representing a Dog, which is a type of Animal."""

            def sound(self):
                """Return the sound made by a Dog."""

                return 'Bark'

        class Cat(Animal):
            """Class representing a Cat, which is a type of Animal."""

            def sound(self):
                """Return the sound made by a Cat."""

                return 'Meow'
