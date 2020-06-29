from __future__ import annotations

from abc import ABC, abstractmethod

from AbstractFactory import PizzaIngredientFactory


class Pizza(ABC):
    name: str = None
    dough: str = None
    sauce: str = None
    cheese: str = None
    clams: str = None
    toppings: [str] = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('Objet Pizza : cuisson 15min à 180°')

    def cut(self):
        print('Objet Pizza : découpe de la pizza')

    def box(self):
        print('Objet Pizza : emballage de la Pizza')

    def getName(self) -> str:
        return self.name

    def setName(self, name: str):
        self.name = name

class CheesePizza(Pizza):
    ingredientFactory: PizzaIngredientFactory = None
    name = "CheesePizza"

    def __init__(self, ingredientFactory: PizzaIngredientFactory) -> None:
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print(f"Préparation d'une pizza {self.name}")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()


class ClamPizza(Pizza):
    ingredientFactory: PizzaIngredientFactory = None
    name = "ClamPizza"

    def __init__(self, ingredientFactory: PizzaIngredientFactory) -> None:
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print(f"Préparation d'une pizza {self.name}")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.clams = self.ingredientFactory.createClam()
