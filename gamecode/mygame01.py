#!/usr/bin/python3
"""
Driving a simple game framework with a dictionary object
"""
# a dictionary linking a room to other rooms
from rooms import rooms


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')


def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split w/ maxsplit=1 allows an item to have a space in it
    # "get golden key" is returned as ["get", "golden key"]
    move = move.lower().split(" ", maxsplit=1)

    # if they type 'go' first
    if move[0] == "go":
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print("you can't go that way")

    # if they type 'get' first
    if move[0] == "get":
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print(f"Can't get {move[1]}!")

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster got you... GAME OVER')
        break

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
