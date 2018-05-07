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
        self.health = health
        self.weapon = weapon

    def attack(self, enemy):
        enemy.take_damage(self.weapon.attack)

    def take_damage(self, amt):
        self.health -= amt

    def add_ability(self, ability):
        self.abilities.append(ability)


thunder_Gun = Weapons("Thunder Gun", 100)
player = Character('Willy', 'Gun', ['Fast_Sprint'], 'Kill', '100', thunder_Gun)


print(player.name)
print(player.abilities)
print(player.stats)
print(player.health)
print(player.attack)


class Room(object):
    def __init__(self, name, north, west, south, east, description, ability=None):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.south = south
        self.east = east
        self.ability = ability

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
start = Room("Starting Room", 'theater', 'lookout', None, 'fire_pad',
             'Where you start the teleporter.')
theater = Room("Theater", 'Projector', 'Trap Room', 'Starting room',
               'Library', 'Is where you activate the teleporter and take take weapon "MK".')
fire_pad = Room("Fire_pad", 'Outside', None, None, 'Starting Room',
                'You could activate a trap.')
Outside = Room("Outside", 'Fence_Room', None, 'Fire Pad', None,
               'You could take a perk " Double Tap.', 'double tap')
Fence_Room = Room("Fence_Room", 'Trap Room', None, 'Outside', 'Theater',
                  'You can activate a electricity trap.')
Library = Room("Library", None, 'Theater', 'Living_Room', None,
               'This is where you can flip a lever to make the mystery chest and take weapon "AK47".')
Living_Room = Room("Living_Room", 'Library', None, 'Kodino',
                   'None', 'You could take a perk "Fast Hands.')
Kodino = Room("Kodino", 'Living_Room', 'Look_out Room', None, None,
              'You can drink a perk "Juggernaut.')
Projector = Room("Projector", None, None, theater, None,
                 'you can pick up a weapon and can activate the movie.')
Trap_Room = Room("Trap_Room", None, None, Fence_Room, 'Theater', 'You can activate the electricity trap and '
                                                                 'take weapon"AR15".')

current_node = start
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:

    print(current_node.name)
    print(current_node.description)
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

        if current_node.ability is not None:
            player.add_ability(current_node.ability)
            print("you pick up the perk %s" % current_node.ability)
            current_node.ability = None
        else:
            print("There is no perk here")
        if current_node.ability is not None:
            player.add_ability(current_node.ability)

        if player.weapon is not None:
            player.add_ability(current_node.ability)
            print("you pick up weapon %s" % current_node.ability)
            current_node.ability = None
        else:
            print("There is no weapon here")
        if current_node.ability is not None:
            player.add_ability(current_node.ability)

    else:
        print('Command not Recognized')
    print()
