class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

    def is_dead(self):
        return self.hp < 0


class Ghost(Enemy):
    def __init__(self):
        self.name = "Ghost"
        self.hp = 25
        self.damage = 10


class HauntedKettle(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 10


class HauntedChairs(Enemy):
    def __init__(self):
        self.name = "Haunted Chairs"
        self.hp = 100
        self.damage = 4


class HauntedChandiler(Enemy):
    def __init__(self):
        self.name = "Haunted Chandiler"
        self.hp = 80
        self.damage = 15