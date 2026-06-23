class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        if (height < 0):
            self.height = 0.0
        else:
            self.height = height

        if (age < 0):
            self.age = 0
        else:
            self.age = age

        self.name = name.capitalize()

    def set_height(self, new_height: float) -> None:
        if (new_height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = new_height
            print(f"Height updated: {self.height}cm")

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.age = new_age
            print(f"Age updated: {self.age} days")

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10)
    print("Plant created:", end=" ")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-25)
    rose.set_age(-3)
    print()
    print("Current state:", end=" ")
    rose.show()


if __name__ == "__main__":
    main()
