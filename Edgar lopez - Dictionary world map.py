world_map = {
    'START': {
        'NAME': "Starting Room",
        'DESCRIPTION': "Where you start and activate the teloporter.",
        'PATHS': {
            'EAST': 'FIRE PAD',
            'WEST': 'LOOKOUT OUT ROOM',
        }
    },
    'Theater': {
        'NAME': "",
        'DESCRIPTION': "Where the teloporter is at",
        'PATHS': {
            'EAST': 'LIBRARY',
            'WEST': 'TRAP',
            'SOUTH': 'STARTTING ROOM',
        }
    },
    'Fire Pad': {
        'NAME': "",
        'DESCRIPTION': "You activate a trap",
        'PATHS': {
            'EAST': 'Starting Room',
            'North': 'Outside',
        }
    },
    'Outside': {
        'NAME': "",
        'DESCRIPTION': "Where you can take a perk('double tap')",
        'PATHS': {
            'SOUTH': 'Fire Pad',
            'North': 'Fence Room',
        }
    }


current_node = world_map ['START']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
           name_of_node = current_node['PATHS'] [command]
           current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print('Command not Recognized')
