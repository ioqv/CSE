import sys

def fight(target):
    while player.health > 0 and target.health > 0:
        print("You have %d Health left" % player.health)
        print("Target has %d Health left" % target.health)
        cmd = input("What do you want to do? ")
        if cmd == 'attack':
            player.attack(target)
        if target.health > 0:
            target.attack(player)
        if player.health <= 0:
            print("You died")
            sys.exit(0)


class Item(object):
    def __init__(self, name):
        self.name = name

    def name(self):
        print("You have %s" % self.name)


class Consumable(Item):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name(self):
        print("You drink %s" % self.name)


class Speedcola(Consumable):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name(self):
        print("You drink %s to get more speed" % self.name)


class Jerganaut(Consumable):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name(self):
        print("You drink %s to take more hits" % self.name)


class Doubletap(Consumable):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name(self):
        print("You drink %s to fast reload" % self.name)


class Wearable(Item):
    def __init__(self, name, cloth):
        super(Wearable, self).__init__(name)
        self.cloth = cloth

    def name(self):
        print("You where cloth %s" % self.name)


class Helmet(Wearable):
    def __init__(self, name, cloth):
        super(Helmet, self).__init__(name, cloth)

    def protection(self):
        print("My %s has a lot of protection for my head" % self.name)


class Shoes(Wearable):
    def __init__(self, name, cloth):
        super(Shoes, self).__init__(name, cloth)

    def laces(self):
        print("Makes me take more %s hits" % self.name)


class Shirt(Wearable):
    def __init__(self, name, cloth):
        super(Shirt, self).__init__(name, cloth)

    def brand(self):
        print("Makes me have more %s damage" % self.name)


class Weapons(Item):
    def __init__(self, name, attack):
        super(Weapons, self).__init__(name)
        self.attack = attack

    def attack(self):
        print("%s attacks a zombie" % self.name)


class Hands(Weapons):
    def __init__(self):
        super(Hands, self).__init__("Your Hands", 30)


class ThunderGun(Weapons):
    def __init__(self, name, attack):
        super(Weapons, self).__init__(name)
        self.attack = attack


class RayGun(Weapons):
    def __init__(self, name, attack):
        super(Weapons, self).__init__(name)
        self.attack = attack


class MK(Weapons):
    def __init__(self, name, attack):
        super(Weapons, self).__init__(name)
        self.attack = attack


class AK47(Weapons):
    def __init__(self, name, attack):
        super(Weapons, self).__init__(name)
        self.attack = attack


class AR15(Weapons):
    def __init__(self, name, attack):
        super(Weapons, self).__init__(name)
        self.attack = attack


class Character(object):
    def __init__(self, name, inventory, abilities, stats, health, weapon):
        self.name = name
        self.inventory = inventory
        self.abilities = abilities
        self.stats = stats
        self.health = 100
        self.weapon = weapon

    def attack(self, enemy):
        enemy.take_damage(self.weapon.attack)

    def take_damage(self, amt):
        self.health -= amt

    def add_ability(self, ability):
        self.abilities.append(ability)


hands = Hands()


class Zombie(Character):
    def __init__(self):
        super(Zombie, self).__init__("Zombie", [], [], [], 100, hands)

zombie = Zombie()
thunder_Gun = ThunderGun("Thunder Gun", 50)

ar15 = Weapons("AR15", 35)
mk = MK("MK", 35)
raygun = RayGun("RayGun", 55)
ak47 = AK47("AK47", 30)

player = Character('Willy', [], ['Fast_Sprint'], 'Kill', 100, thunder_Gun)
shirt = Shirt("Red Shirt", "cotton")

print(player.name)
print(player.abilities)
print(player.stats)
print(player.health)
print(player.attack)


class Room(object):
    def __init__(self, name, north, west, south, east, description, ability=None, enemies=None, items=[]):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.south = south
        self.east = east
        self.ability = ability
        self.enemies = enemies
        self.items = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
Start = Room("Start", 'Theater', 'lookout', None, 'Fire_pad',
             'Where you start the teleporter.')
Theater = Room("Theater", 'Projector', 'Trap_Room', 'Start',
               'Library', 'You can take weapon "MK".', None, [zombie],
               [MK("MK", 35)])
Fire_pad = Room("Fire_pad", 'Outside', None, None, 'Start',
                'You can take weapon "AR15".', None, None, [zombie],
                [AR15("AR15", 35)])
Outside = Room("Outside", 'Fence_Room', None, 'Fire Pad', None,
               'You could take a perk " Double Tap.', 'double tap')
Fence_Room = Room("Fence_Room", 'Trap Room', None, 'Outside', 'Theater',
                  'You can take weapon "Thunder_gun".', None, [zombie],
                  [ThunderGun("Thunder_gun", 50)])
Library = Room("Library", None, 'Theater', 'Living_Room', None,
               'you can take weapon "AK47".', None, None,
               [AK47("AK47", 40)])
Living_Room = Room("Living_Room", 'Library', None, 'Kodino',
                   'None', 'You could take a perk "Fast Hands.')
Kodino = Room("Kodino", 'Living_Room', 'Look_out Room', None, None,
              'You can drink a perk "Juggernaut.')
Projector = Room("Projector", None, 'Dresser', 'Theater', None,
                 'you can pick up a wearable and take RayGun.', None, None,[RayGun("RayGun", 100)])
Trap_Room = Room("Trap_Room", None, None, Fence_Room, 'Theater', 'take weapon"AR15".', None, None, [AR15("AR15", 35)])
Dresser = Room("Dresser", None, None, None, 'Projector', 'Pick up shirt, pants, and helmet.', None, None, [shirt])

current_node = Start
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:

    print(current_node.name)
    print(current_node.description)
    if current_node.enemies is not None:
        for char in current_node.enemies:
            print("You see a %s" % char.name)
            fight(char)
            if player.health <= 0:
                sys.exit(0)
        current_node.enemies = None
        continue
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form*
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")

    elif command == "take ability":
        if current_node.ability is not None:
            player.add_ability(current_node.ability)
            print("you pick up the perk %s" % current_node.ability)
            current_node.ability = None
        else:
            print("There is no perk here")
    elif command == "take":
        item_name = input("Take what? ")
        found = False
        if current_node.items is not None:
            for item in current_node.items:
                if item_name == item.name:
                    print("Taken.")
                    player.inventory.append(item)
                    found = True
        if not found:
            print("It isn't here")

    elif command == 'inventory':
        for item in player.inventory:
            print(item.name)

    else:
        print('Command not Recognized')
    print()
