class Beverage:

    _description: str = "Unknown Beverage"

    def getDescription(self) -> str:
        return self._description

    def cost(self) -> float:
        pass

class Espresso(Beverage):
    def __init__(self) -> None:
        self._description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self) -> None:
        self._description = "House Blend"

    def cost(self) -> float:
        return 0.89


class CondimentDecorator(Beverage):
    _beverage: Beverage = None

    def __init__(self, beverage:Beverage) -> None:
        self._beverage = beverage

    @property
    def beverage(self):
        return self._beverage

    def getDescription(self) -> str:
        return self._beverage.getDescription()

    def cost(self) -> float:
        return self._beverage.cost()


class Mocha(CondimentDecorator):
    def getDescription(self) -> str:
        return self.beverage.getDescription() + ", Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.2


class Soy(CondimentDecorator):
    def getDescription(self) -> str:
        return self.beverage.getDescription() + ", Soy"

    def cost(self) -> float:
        return self.beverage.cost() + 0.5


class Foam(CondimentDecorator):
    def getDescription(self) -> str:
        return self.beverage.getDescription() + ", Foam"

    def cost(self) -> float:
        return self.beverage.cost() + 0.7

class PumpkinSpice(CondimentDecorator):
    def getDescription(self) -> str:
        return self.beverage.getDescription() + ", PumpkinSpice"

    def cost(self) -> float:
        return self.beverage.cost() + 1.0


if __name__ == "__main__":
    # This way the client code can support both simple components...
    boisson = Espresso()
    print(f"{boisson.getDescription()} ${boisson.cost()}")

    boisson = Soy(Mocha(HouseBlend()))
    print(f"{boisson.getDescription()} ${boisson.cost()}")

    boisson = PumpkinSpice(Soy(Mocha(Espresso())))
    print(f"{boisson.getDescription()} ${boisson.cost()}")