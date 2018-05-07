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
theater = Room("Theater", None, 'Trap Room', 'Starting room',
               'Library', 'Is where you activate the teleporter.')
fire_pad = Room("Fire_pad", 'Outside', None, None, 'Starting Room',
                'You could activate a trap.')
Outside = Room("Outside", 'Fence_Room', None, 'Fire Pad', None,
               'You could take a perk " Double Tap.', 'double tap')
Fence_Room = Room("Fence_Room", 'Trap Room', None, 'Outside', 'Theater',
                  'You can activate a electricity trap.')
Library = Room("Library", None, 'Theater', 'Living_Room', None,
               'This is where you can flip a lever to make the mystery chest.')
Living_Room = Room("Living_Room", 'Library', None, 'Kodino',
                   'None', 'You could take a perk "Fast Hands.')
Kodino = Room("Kodino", 'Living_Room', 'Look_out Room', None, None,
              'You can drink a perk "Juggernaut.')
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
        # Change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")