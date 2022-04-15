"""
module contains classes
and methods for game implementation
"""
import sys
import os
import logging

class Room:
    "class for the rooms"
    def __init__(self, name, descr=None, linked_rooms=None, enemy=None, item=None):
        self.name = name
        self.descr = descr
        self.linked_rooms = linked_rooms or {}
        self.enemy = enemy
        self.item = item

    def set_description(self, new_descr):
        "sets the right room description"
        self.descr = new_descr

    def link_room(self, room, direction):
        "links to the mentioned room"
        self.linked_rooms[direction] = room

    def set_character(self, enemy):
        "sets the enemy in the room"
        self.enemy = enemy
    
    def set_item(self, item):
        "sets the item in the room"
        self.item = item

    def get_details(self):
        print(self.name)
        print('---------------')
        if self.descr:
            print(self.descr)
        for key in self.linked_rooms:
            print(f"The {self.linked_rooms[key].name} is {key}")
    
    def get_character(self):
        "gets the enemy"
        return self.enemy
    
    def get_item(self):
        "gets the item"
        return self.item

    def move(self, command):
        "changes the room"
        return self.linked_rooms[command]


class Character:
    "general class for the characters"
    def __init__(self, name, descr, conv=None):
        self.name = name
        self.descr = descr
        self.conv = conv
    
    def set_conversation(self, phrase):
        "sets a conversation phrase"
        self.conv = phrase

    def describe(self):
        "describes the character"
        if self:
            print(f"{self.name} is here!")
        if self.descr:
            print(self.descr)
    
    def talk(self):
        "talk to the character"
        print(f'{self.name} says:')
        print(self.conv)
    



class Enemy(Character):
    "class for the enemies"
    def __init__(self, name, descr, conv=None, weak=None, defeats=0):
        super().__init__(name, descr, conv)
        self.weak = weak
        self.defeats = defeats

    def set_weakness(self, weakness):
        "sets the enmy's weakness"
        self.weak = weakness

    def fight(self, tool):
        "fight with the character"
        if self.weak == tool:
            return True
        return 
    
    def get_defeated(self):
        "controls character's defeat"
        self.defeats += 1
        return self.defeats


class Friend(Character):
    "class for friends"
    def __init__(self, name, descr, conv=None, special_greeting=None):
        super().__init__(name, descr, conv)
        self.specgreet = special_greeting

    def set_special_greeting(self, phrase):
        "set the special greeting for a friend"
        self.specgreet = phrase
        self.conv = phrase + '\n' + self.conv
    
    def talk_about_life(self):
        "talk about life with a friend"
        print('You have talked and talked \
with your friend')
        print('It was interesting to share some thoughts about life')


class Item:
    "class for items"
    def __init__(self, name, descr=None):
        self.name = name
        self.descr = descr
    
    def set_description(self, new_descr):
        "sets the right item description"
        self.descr = new_descr

    def describe(self):
        "describes the item"
        if self:
            print(f"The [{self.name}] is here - \
{self.descr}")

    def get_name(self):
        "returns the name of the item"
        return self.name


class Protocol:
    "class for the protocols"
    def __init__(self, name='game_log.txt'):
        self.name = name

    def activate_protocol(self):
        "activates the protocol mode"
        self.old_stdout = sys.stdout
        self.file = open(self.name,"w")
        sys.stdout = self.file # write to file instead of the printing

    def deactivate_protocol(self):
        "deactivated the protocol mode"
        sys.stdout = self.old_stdout
        self.file.close()
