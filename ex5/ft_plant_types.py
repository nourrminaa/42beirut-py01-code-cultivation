class Plant:
    def __init__(
        self, name: str, height: float, age: int, height_growth_value: float
    ) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age
        self.height_growth_value = height_growth_value

    def grow(self) -> None:
        self.height = round(self.height + self.height_growth_value, 1)

    def age_update(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        height_growth_value: float,
        color: str,
    ) -> None:
        super().__init__(name, height, age, height_growth_value)
        self.color = color
        self.is_bloomed = False

    def bloom(self) -> None:
        self.is_bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        height_growth_value: float,
        trunk_diameter: float,
    ):
        super().__init__(name, height, age, height_growth_value)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        height_growth_value: float,
        harvest_season: str,
    ):
        super().__init__(name, height, age, height_growth_value)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def age_update(self):
        super().age_update()
        self.nutritional_value += 1

    def grow(self):
        super().grow()
        self.nutritional_value += 1

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 3.5, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age_update()
    tomato.show()


if __name__ == "__main__":
    main()
