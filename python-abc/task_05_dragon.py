#!/usr/bin/env python3
"""
Module defining Mixin classes for swimming and flying,
and a Dragon class that uses these mixins.
"""


class SwimMixin:
    """Mixin class to add swimming functionality."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying functionality."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from SwimMixin and FlyMixin.
    Also has its own unique method roar.
    """

    def roar(self):
        """Prints a roaring message."""
        print("The dragon roars!")
