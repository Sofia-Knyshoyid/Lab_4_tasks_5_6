"""
the game has the plot
of the person walking the Lviv streets
and having different adventures on the way
"""
from cmath import phase
from xml.dom import ValidationErr
import lviv_travel as travel
import random
import sys

class Location:
    "class for the city locations"
    def __init__(self, name, descr=None, locations_near=None, enemy=None, friend=None, item=None):
        self.name = name
        self.descr = descr
        self.locations_near = locations_near or {}
        self.enemy = enemy
        self.friend = friend
        self.item = item

    def set_description(self, new_descr):
        "sets the right location description"
        self.descr = new_descr

    def link_location(self, location, distance):
        "links to the mentioned room"
        self.locations_near[distance] = location

    def set_enemy(self, enemy):
        "sets the enemy in the location"
        self.enemy = enemy
    
    def set_item(self, item):
        "sets the item in the location"
        self.item = item

    def get_details(self):
        print(self.name)
        print('──────⊱⁜⊰──────')
        if self.descr:
            print(self.descr)
        for key in self.locations_near:
            print(f"The distance to {self.locations_near[key].name} is {key}")
    
    def get_character(self):
        "gets the enemy"
        return self.enemy
    
    def get_item(self):
        "gets the item"
        return self.item

    def move(self, distance):
        "changes the location"
        return self.locations_near[distance]


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
            phrases = [f"{self.name} is here!", f"{self.name} is standing right on the street",
            f"In the corner of the alley stands {self.name}", f"{self.name} is looking at you from the cafe window",
            f"{self.name} talks with a group of people", f"A random person told you {self.name} is standing around the corner",
            f"{self.name} is sitting on the bench", f"{self.name} is feeding the pigeons with bread",
            f"It seems you have seen {self.name} going in the shop", f"{self.name} stands nearby and seems suprised to see you here"]
            the_phrase = random.choice(phrases)
            print(the_phrase)
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

    def quarrel(self):
        "quarrel with the enemy"
        phrase_ls = ['Remind about the failure of the last month',
        'Ignore the arguments of the interlocutor',
        'Laugh at the misfortunes of your enemy',
        "Pretend you are disappointed in the story of interlocutor's succes",
        "Tell an offensive joke", "Advise to get a better life in the future",
        "Be judgementall", "Act angry",
        "Pretend to be behind person's misfortunes"]
        print('Decide what phrase to choose in your argument:')
        phrases = list(random.choices(phrase_ls, k=3))
        for num in range(1,4):
            print(f"{num}.  -  {phrases[num-1]}")

    def get_reaction(self):
        "get the enemy's reaction"
        phrase_ls = [f"There was no reaction to your words at all",
        f"The person seemed irritated",
        f"The person seemed distracted and hardly reacted to your words",
        f"The person went mad after your statement!",
        f"You were told to wait and see for the consequences",
        f"You got yelled at!", f"You were told to mind your own bussiness"]
        phrase = random.choice(phrase_ls)
        print(phrase)


class AgressivetEnemy(Enemy):
    """this enemy is more hostile
    than the usual one"""
    def fight(self, tool):
        "fight with the character"
        if self.weak == tool:
            return True
        return 
    
    def get_defeated(self):
        "controls character's defeat"
        self.defeats += 1
        return self.defeats


class Criminal(AgressivetEnemy):
    """
    the criminals are a danger to your life
    """
    def call_the_police(self):
        "call the police to end the conflict"
        arrived_in_time = bool(random.getrandbits(1))
        if arrived_in_time:
            print('The police arrived on time and saved you from the conflict')
        else:
            print("The criminal's reaction was much quicker than that of a police")
            print('Unfortunatelly for you, the criminal had the deadly weapons, and you got killed immediately')
            raise ValidationErr
    
    def fight(self, tool):
        "fight with the criminal"
        if self.weak == tool:
            chances = [0,0,0,0,0,0,1]
            if random.choice(chances) == 1:
                return True
        return False





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


class BestFriend(Friend):
    "best friend class"
    def __init__(self, name, descr, conv=None, special_greeting=None, accepts=[]):
        super().__init__(name, descr, conv, special_greeting)
        self.accepts = accepts or []

    def sing_nostalgic_song(self):
        "sing a unique song from the past with a best friend"
        print('You decide to sing a song from the friendly memories with your best friend')
        print('You have to remember all the words...right?')
        choice_ls = [f"Sing with all the seriousness",
        f"Fake singing with opening the mouth", f"Laugh when you don't know the words",
        f"Ask the friend to sing alone", f"Quickly find the lyrics in the internet",
        f"Change the song to the known one", f"Whistle the melody"]
        choices = list(random.choices(choice_ls, k=3))
        for num in range(1,4):
            print(f"{num}  -  {choices[num-1]}")
        answer = input("*write the number of the action*")
        if answer in ['1', '2', '3']:
            print('You had fun with your friend!')
        else:
            print('You were to distracted to focus, and your friend did not enjoy time with you')

    def tell_a_secret(self):
        "tell a secret to your best friend"
        print("You want to share your secret with best friend")
        answer = input('Your friend is listening...')
        print("Your best friend swore this secret will remain a secret!")



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
            phrase_ls = [f"The {self.name} is here", f"The {self.name} is laying on the ground",
            f"The {self.name} is laying near the fountain", f"You notice the {self.name}. Nobody seems to own it.",
            f"Under the old tree ypu discern the {self.name}", f"The {self.name} has caught your attention",
            f"The magician stops you and offers you {self.name} for free!",
            f"The street lottery you participated in yesterday won you the {self.name}.",
            f"The {self.name} is at the door of the abandoned house"]
            the_phrase = random.choice(phrase_ls)
            print(the_phrase)
            print(f" - {self.descr}")

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


