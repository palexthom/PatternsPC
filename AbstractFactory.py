from __future__ import annotations
from abc import ABC, abstractmethod
import Ingredients


# AbstractFactory
class PizzaIngredientFactory(ABC):

    @abstractmethod
    def createDough(self):
        pass

    @abstractmethod
    def createSauce(self):
        pass

    @abstractmethod
    def createClam(self):
        pass

    @abstractmethod
    def createCheese(self):
        pass


# Concrete Factories
class NYIngredientFactory:

    def createDough(self):
        return Ingredients.ThinCrustDough()

    def createSauce(self):
        return Ingredients.MarinaraSauce()

    def createCheese(self):
        return Ingredients.RegianoCheese()

    def createClam(self):
        return Ingredients.FreshClams()


class ChicagoIngredientFactory:

    def createDough(self):
        return Ingredients.ThickCrustDough()

    def createSauce(self):
        return Ingredients.PlumTomatoSauce()

    def createCheese(self):
        return Ingredients.MozarellaCheese()

    def createClam(self):
        return Ingredients.FrozenClams()