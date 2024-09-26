#!/usr/bin/python3


class Fish:
    """Fish class representing aquatic animals with swimming capabilities."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The bird lives in the sky")


class Bird:
    """Bird class representing avian creatures with flying capabilities."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlayingFish(Fish, Bird):
    """FlyingFish class that inherits from both Fish and Bird."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
