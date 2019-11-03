from room import Room
from item import Item
from player import Player
import textwrap
from os import system

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

room['outside'].items.append(Item("ball", "Big red soccer ball"))
room['outside'].items.append(Item("matches", "Box of matches"))
room['foyer'].items.append(Item("hammer", "Thor's hammer"))
room['overlook'].items.append(Item("book", "An old dusty book"))
room['narrow'].items.append(Item("pencil", "Yellow pencil"))
room['narrow'].items.append(Item("telescope", "Professional telescope"))
room['treasure'].items.append(Item("phone", "IphoneX"))

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Pablo", room["outside"])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def print_instructions():
    print(" _________________________")
    print("|Enter 'n' to move North  |")
    print("|Enter 's' to move South  |")
    print("|Enter 'e' to move East   |")
    print("|Enter 'w' to move West   |")
    print("|Enter 'q' to quit        |")
    print("|Enter 'get [item]' to get|")
    print("|item                     |")
    print(" ------------------------- ")


while True:
    print_instructions()
    print(player1.location)
    print("Items in current location: ")
    for item in player1.location.items:
        print(f"- {item}")
    #print(f"** You are currently {player1.location} **")
    #print("Location Description:")

    #wrap = room[player1.location].args
    #for desc in wrap:
    #print(f" - {desc}")
    next_move = input("What to next? ") 
    if next_move is "n":
        if player1.location.n_to is None:
            print("Not a valid direction. Try again.")
        else:
            player1.location = player1.location.n_to
            print("You have moved North")
    elif next_move is "s":
        if player1.location.s_to is None:
            print("Not a valid direction. Try again.")
        else:
            player1.location = player1.location.s_to
            print("You have moved South!")
    elif next_move is "e":
        if player1.location is None:
            print("Not a valid direction. Try again.")
        else:
            player1.location = player1.location.e_to
            print("You have moved East!")
    elif next_move is "w":
        if player1.location.w_to is None:
            print("Not a valid direction. Try again.")
        else:
            player1.location = player1.location.w_to
            print("You have moved West!")
    elif len(next_move.split(" ")) is 2:
        if next_move.split(" ")[0] == "get":
            for item in player1.location.items:
                if item.name == next_move.split(" ")[1]:
                    player1.inventory.append(item)
                    print(player1.inventory[0], "Got the item!")
        else:
            print("Type 'get [item name]' to get item")
    elif next_move is "q":
        print("Goodbye!")
        system("clear")
        break
    else:
        print("Can't go there! Choose another direction")
    #rsystem("clear")

