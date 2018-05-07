class Character(object):
    def __init__(self, name, inventory, abilities, stats, health):
        self.name = name
        self.inventory = inventory
        self.abilities = abilities
        self.stats = stats
        self.health = health

    def attack(self, Enemy):
        Enemy.damage()
        self.health -= 25
    def inventory(self, health):
        self.health()
    print("You have")

player = Character("Willy", "Gun", "Fast Sprint", "Kills", "100",)


print(player.name)
print(player.inventory)
print(player.abilities)
print(player.stats)
print(player.health)
print(player.attack)