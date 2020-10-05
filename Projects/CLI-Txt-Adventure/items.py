# this is where all of my classes have been initialized
# Super classes are here on top and specific subclasses follow
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create Raw Weapon Objects!!!")

    def __str__(self):
        return self.name


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


# weapons for attack
class Salt(Weapon):
    def __init__(self):
        self.name = "Salt"
        self.description = "A small salt shaker, perfect for making a salt circle."
        self.damage = 10
        self.value = 15


class SilverDagger(Weapon):
    def __init__(self):
        self.name = "Silver Dagger"
        self.description = (
            "A small dagger with some rust. " "Best used with a salt circle."
        )
        self.damage = 15
        self.value = 20


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = (
            "This sword is showing its age,  " "but still has some fight in it."
        )
        self.damage = 20
        self.value = 100


# Consumables for healing


class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 12


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60