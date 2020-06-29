from __future__ import annotations
from abc import ABC, abstractmethod
import Pizza, AbstractFactory

class PizzaStore(ABC):
    @abstractmethod
    def createPizza(self, typePizza: str):
        pass

    def orderPizza(self, typePizza: str) -> Pizza:
        print("Pizza Store : on m'a demandé un objet Pizza, je le crée via ma méthode createPizza")
        pizza = self.createPizza(typePizza)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYPizzaStore(PizzaStore):

    ingredientFactory: AbstractFactory.PizzaIngredientFactory = None

    def __init__(self) -> None:
        self. ingredientFactory = AbstractFactory.NYIngredientFactory()

    def createPizza(self, typePizza: str) -> Pizza.Pizza:
        pizza: Pizza.Pizza = None

        print("NYPizzaStore : c'est moi qui crée l'objet Pizza")
        if typePizza ==  "Cheese":
            pizza = Pizza.CheesePizza(self.ingredientFactory)
            pizza.setName("NY Style Cheese Pizza")
        elif typePizza == "Clam":
            pizza = Pizza.ClamPizza(self.ingredientFactory)
            pizza.setName("NYStyle Clam Pizza")

        return pizza


class ChicagoPizzaStore(PizzaStore):
    ingredientFactory: AbstractFactory.PizzaIngredientFactory = None

    def __init__(self) -> None:
        self.ingredientFactory = AbstractFactory.NYIngredientFactory()

    def createPizza(self, typePizza: str) -> Pizza.Pizza:
        pizza: Pizza.Pizza = None

        print("NYPizzaStore : c'est moi qui crée l'objet Pizza")
        if typePizza == "Cheese":
            pizza = Pizza.CheesePizza(self.ingredientFactory)
            pizza.setName("NY Style Cheese Pizza")
        elif typePizza == "Clam":
            pizza = Pizza.ClamPizza(self.ingredientFactory)
            pizza.setName("NYStyle Clam Pizza")

        return pizza

if __name__ == "__main__":
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza1 = nyStore.orderPizza("Cheese")
    print(f"Ethan a commandé une pizza {pizza1.getName()}")
    pizza2 = chicagoStore.orderPizza("Clam")
    print(f"Joen a commandé une pizza {pizza2.getName()}")