import enemies
import npc
import random


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        return """
      You find yourself at the entrance of a mansion that appears to be haunted.
      There is a sign above your head that reads 'The Mansion of No Escape. WARNING: Once you enter, you can't leave!'
      You avoid the warning and enter anyway
        """


class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.90:
            self.enemy = enemies.Ghost()
            self.alive_text = "A ghost materializes out of " "nowhere!"
            self.dead_text = (
                "The pile of ectoplasmic goop "
                "on the floor reminds you of of your victory."
            )
        elif r < 0.80:
            self.enemy = enemies.HauntedKettle()
            self.alive_text = "You hear the distinct squeal of boiled water in a kettle, but no one is home!"
            self.dead_text = "The silence of the mansion reminds you of your triumph.."
        elif r < 0.95:
            self.enemy = enemies.HauntedChairs()
            self.alive_text = (
                "You hear a squeaking noise growing louder"
                "...suddenly you are surrounded by a bunch of haunted dining room chairs!"
            )
            self.dead_text = "Dozens of broken chairs reminds you of your victory."
        else:
            self.enemy = enemies.HauntedChandiler()
            self.alive_text = (
                "You've disturbed a Haunted Chandiler " "from his slumber!"
            )
            self.dead_text = (
                "Defeated, the monster has reverted " "into a shattered chandiler."
            )
        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(
                "Enemy does {} damage. You have {} HP remaining.".format(
                    self.enemy.damage, player.hp
                )
            )


class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It appears to be sunlight!

        It is just a bright chandelier!
        """


class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            Another unremarkable room in the mansion. You must forge onwards.
            """
        else:
            return """
            There is some gold on the floor. You pick it up.
            """


class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ["Q", "q"]:
                return
            elif user_input in ["B", "b"]:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ["S", "s"]:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ["Q", "q"]:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def intro_text(self):
        return """
        A friendly ghost that is looking to trade.
        """


world_dsl = """
|EN|EN|EN|VT|EN|  |  |
|TT|  |  |EN|EN|TT|  |
|EN|FG|EN|EN|TT|EN|  |
|TT|  |EN|FG|EN|FG|  |
|FG|  |  |  |FG|  |  |
|EN|  |  |EN|TT|EN|  |
|FG|ST|EN|FG|  |EN|  |
|  |  |  |  |  |  |  |
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True


tile_type_dict = {
    "VT": VictoryTile,
    "EN": EnemyTile,
    "ST": StartTile,
    "FG": FindGoldTile,
    "TT": TraderTile,
    "  ": None,
}

world_map = []
start_tile_location = None


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)
        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None