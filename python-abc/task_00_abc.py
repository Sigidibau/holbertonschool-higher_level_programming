#!/usr/bin/python3
"""_summary_"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):

        class Dog(Animal):
            def sound(self):
                return 'Bark'

        class Cat(Animal):
            def sound(self):
                return 'Meow'
