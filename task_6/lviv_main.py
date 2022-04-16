"""
the main module
of the Lviv traveller game
"""
"""
the main module
of the Lviv traveller game
"""
import lviv_travel as lviv
Stryyska = lviv.Location('Stryyska street', 'The noisy and broad street. There are many people here right now.')
Kozelnytska = lviv.Location('Kozelnytska street', 'It is quite cozy here, and your journey becomes much easier.')
Ivana_Franka = lviv.Location('Ivana Franka street', 'The familiar street with beautiful architecture.')
Tarasa_Shevchenka = lviv.Location('Tarasa Shevchenka avenue', 'It is comfortable, fresh and calm here.')
Krakivska = lviv.Location('Krakivska street', 'It seems there are more people than free space on this street today.')
Horodotska = lviv.Location('Horodotska street', 'The sunny street. A group of pigeons is sitting nearby.')
Hnatyuka = lviv.Location('Hnatyuka street', 'There is some street action here. People are smiling and talking in the crowd.')
Teatralna = lviv.Location('Teatralna street', 'The groups of tourists are chatting and laughing.')

Stryyska.link_location(Kozelnytska, '200 m')
Kozelnytska.link_location(Stryyska, '200 m')
Kozelnytska.link_location(Ivana_Franka, '50 m')
Ivana_Franka.link_location(Kozelnytska, '50 m')
Ivana_Franka.link_location(Tarasa_Shevchenka, '130 m')
Tarasa_Shevchenka.link_location(Ivana_Franka, '130 m')
Tarasa_Shevchenka.link_location(Krakivska, '320 m')
Krakivska.link_location(Tarasa_Shevchenka, '320 m')
Tarasa_Shevchenka.link_location(Horodotska, '100 m')
Horodotska.link_location(Tarasa_Shevchenka, '100 m')
Hnatyuka.link_location(Horodotska, '153 m')
Horodotska.link_location(Hnatyuka, '153 m')
Hnatyuka.link_location(Krakivska, '220 m')
Krakivska.link_location(Hnatyuka, '220 m')
Ivana_Franka.link_location(Teatralna, '550 m')
Teatralna.link_location(Ivana_Franka, '550 m')
Teatralna.link_location(Tarasa_Shevchenka, '320 m')
Tarasa_Shevchenka.link_location(Teatralna, '320 m')

Stryyska.set_item(lviv.ActivationItem('old chest', 'ancient chest, can be opened with a code',\
lviv.Item('code on the paper', 'some weird code written on the paper'), lviv.Item('heavy key', 'heavy key with an ornament')))
Kozelnytska.set_item(lviv.Item('code on the paper', 'some weird code written on the paper'))
Hnatyuka.set_item(lviv.Item('tree branch', 'just an ordinary tree brach, nothing special about it'))
Ivana_Franka.set_item(lviv.Item('Physics book', 'Book on the physics basics'))
Tarasa_Shevchenka.set_item(lviv.Item('balloon', 'a big green balloon with white dots'))
Horodotska.set_item(lviv.Item('baseball bat', 'a professional baseball bat'))
Teatralna.set_item(lviv.Item('flute', 'A flute, nicely painted in pastel colours'))
Krakivska.set_item(lviv.ActivationItem('A door to the meeting house', 'you and your friends have decided to meet here',\
lviv.Item('heavy key', 'heavy key with an ornament'), final=True))


Kozelnytska.set_friend(lviv.BestFriend('Olena', 'Your best friend from 3rd grade'))
Stryyska.set_friend(lviv.Friend('classmate', 'your classmate you enjoy talking to'))
Ivana_Franka.set_enemy(lviv.Enemy('toxic acquaintant', 'the person you often have conflicts with'))
Hnatyuka.set_enemy(lviv.Criminal('runaway murderer', 'A runaway murderer you have heard about on the news!'))

current_location = Stryyska
backpack = []

dead = False
print()
print('You have to reach Krakivska street to study together with your collegues, \
and you have to get the key to enter the building.')
print('Good luck!')

while dead == False:

    print("\n")
    current_location.get_details()

    inhabitant = current_location.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_location.get_item()
    if item is not None:
        item.describe()
    print("(write the distance to the destination to move, for example '140 m'")
    print("write 'talk/sing together/tell a secret' to interact with the friendly character if there is one in this location")
    print("write 'fight/quarrel/call the police' to interact with the hostile character if there is one in this location")
    print("write 'take/activate' to interact with the item if there is one in this location)" )

    command = input("> ")

    if 'm' in command:
        # Move in the given direction
        try:
            current_location = current_location.move(command)
        except: print('(...Impossible to move in that direction)')
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print('There is nobody you can talk to')
    elif command == 'sing together':
        try:
            character = current_location.get_character()
            character.sing_nostalgic_song()
        except:
            print('There is nobody you can freely sing a song with')
    elif command == 'tell a secret':
        try:
            character = current_location.get_character()
            character.tell_a_secret()
        except:
            print("There is nobody close enough to hear out your secret")
    elif command == 'quarrel':
        try:
            character = current_location.get_character()
            character.quarrel()
        except:
            print('There is nobody you can quarrel with')
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_location.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "call the police":
        try:
            character = current_location.get_character()
            result = character.call_the_police()
            if not result:
                dead = True
            current_location.enemy = None
        except:
            print('There is nobody worth calling the police')
    elif command == "take":
        if item:
            if not item.take_possibility():
                continue
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_location.set_item(None)
        else:
            print("There's nothing here to take!")
    elif command == 'activate':
        try:
            found = False
            for elem in backpack:
                if elem == item.activation.name:
                    found = True
            if found is False:
                print('You do not know how to activate this item')
                continue
            result = item.activate(item.activation)
            if result:
                if result == 'end':
                    dead = True
                else:
                    print("You put the " + result.get_name() + " in your backpack")
                    backpack.append(result.get_name())
                    current_location.set_item(None)
        except:
            print('You can not activate this item')
    else:
        print("I don't know how to " + command)

