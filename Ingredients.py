from __future__ import annotations
from abc import ABC, abstractmethod


# Creation des interfaces ingredients
class Dough(ABC):
    pass


class Sauce(ABC):
    pass


class Clams(ABC):
    pass


class Cheese(ABC):
    pass


# Creation d'ingredients concrets
class ThinCrustDough(Dough):
    def __str__(self):
        return "ThinCrustDugh"


class ThickCrustDough(Dough):
    def __str__(self):
        return "ThickCrustDough"


class MarinaraSauce(Sauce):
    def __str__(self):
        return "MarinaraSauce"


class PlumTomatoSauce:
    def __str__(self):
        return "PlumTomatoSauce"


class FreshClams:
    def __str__(self):
        return "FreshClams"


class FrozenClams:
    def __str__(self):
        return "FrozenClams"


class RegianoCheese:
    def __str__(self):
        return "RegianoCheese"


class MozarellaCheese:
    def __str__(self):
        return "MozarellaCheese"