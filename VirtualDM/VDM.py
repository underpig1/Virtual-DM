import random
import re
import os.path
from os import path
import ast
from graphics import *
import itertools
import time
import tkinter as tk

playerhealth = ""
prints = "Launching..."
location = ""
locations = ["bar", "mountain", "castle", "village", "town", "dungeon"]
loot = ["health potion", "levitation potion", "strength potion", "flight potion", "10 gold", "10 copper", "5 copper", "1 gold", "5 gold", "1 copper", "20 gold",]
searchedloot = []
iinventory = []
enemytypes = ["orc", "human",]

def graphics():
    global win
    win = GraphWin("Launcher", 500, 500)
    win.setBackground("white")
    topbox = Rectangle(Point(0,500), Point(500, 250))
    topbox.setFill("black")
    topbox.draw(win)
    centercircle = Circle(Point(250,250), 90)
    centercircle.setFill("black")
    centercircle.draw(win)
    centertext = Text(Point(250,250), "VDM")
    centertext.setTextColor("white")
    centertext.setStyle("bold")
    centertext.setSize(30)
    centertext.draw(win)
    printtext = Text(Point(250,400), prints)
    printtext.setTextColor("white")
    printtext.setStyle("italic")
    printtext.setSize(30)
    printtext.draw(win)
    time.sleep(random.randint(1,5))
    for i in range(101):
        printtext.setText(str(i) + "%")
        time.sleep(random.randint(1, 10)/1000)
        if random.randint(1, 10) == 1:
            time.sleep(random.randint(1,5)/100)
    time.sleep(random.randint(1,20)/10)
    printtext.setText("")
    playbutton = tk.Button(win, text = "New Game", command = new_session, width = 100, height = 50)
    playbutton.place(x = 200, y = 300)

def playwindow():
    global play
    play = GraphWin("Virtual Dungeon Master", 1000, 500)
    play.setBackground("white")
    topbox = Rectangle(Point(0, 1000), Point(1000, 500))

def say(noun):
    return 'You said "{}"'.format(noun)
    prints = 'You said "{}"'.format(noun)
    
def move():
    global location
    print("You left the {}".format(location))
    prints = "You left the {}".format(location)
    location = random.choice(locations)
    add_enemy()
    return

def iloot():
    global iinventory
    global searchedloot
    if not searchedloot == None:
        print("There is: {} on the ground".format(searchedloot))
        prints = "There is: {} on the ground".format(searchedloot)
        print("You collected {}".format(searchedloot))
        prints = "You collected {}".format(searchedloot)
        iinventory.append(searchedloot)
        searchedloot = []
    else:
        print("There is no loot.")
        prints = "There is no loot."

def dodge():
    if counter == True:
        prints = "Roll for dexterity"
        dexterity = int(input("Roll for dexterity"))
        if dexterity >= 10:
            print("Dodged attack.")
            prints = "Dodged attack."
            dodged = True
    else:
        print("There is nothing to dodge.")
        prints = "There is nothing to dodge."
        return

def teleport(noun):
    global locations
    global location
    global developer
    if noun in locations:
        location = noun
    else:
        if developer == True:
            print("developer: teleport_error: No such location exists: {}".format(noun))
            prints = "developer: teleport_error: No such location exists: {}".format(noun)
            return

def inventory():
    global iinventory
    if not iinventory == None:
        print(iinventory)
        prints = iinventory
    else:
        print("You have nothing in your inventory.")
        prints = "You have nothing in your inventory."

def use(noun):
    global iinventory
    if noun in iinventory:
        if "health" in noun:
            char.health = char.health + 10
            msg = "You gained health."
        elif "flight" or "levitation" in noun:
            msg = "You are now flying."
        else:
            msg = "You used {}".format(noun)
        iinventory.remove(noun)
        prints = msg
        return msg

def throw(noun, objecttype):
    global iinventory
    global searchedloot
    if noun in iinventory:
        if objecttype in GameObject.objects:
            prints = "Roll for strength."
            strength = input("Roll for strength.")
            if strength >= 10:
                print("You threw your {}".format(noun))
                prints = "You threw your {}".format(noun)
                iinventory.remove(noun)
                searchedloot.append(noun)
            else:
                print("You missed!")
                prints = "You missed!"
                return
        else:
            return "There is no {} here.".format(object)
            prints = "There is no {} here.".format(object)
    else:
        return "You do not have a {}".format(object)
        prints = "You do not have a {}".format(object)

def rest(time):
    global rests
    if rests - time >= 0:
        print("You are resting")
        prints = "You are resting"
        char.health = char.health + time * 2
    else:
        print("You do not have enough rests for {} hours".format(time))
        prints = "You do not have enough rests for {} hours".format(time)
    return

def start_game():
    global dodged
    global playerhealth
    global locations
    global loot
    global searchedloot
    global iinventory
    global enemytypes
    global location
    rests = 5
    dodged = False
    playerhealth = int(input("Your health points "))
    print("Welcome!")
    print("Command list: \n say () \n examine () \n attack () \n look \n move \n loot \n dodge \n inventory \n use() \n throw()() \n rest() \n inventory \n save \n open() \n new")
    locations = ["bar", "mountain", "castle", "village", "town", "dungeon"]
    loot = ["health potion", "levitation potion", "strength potion", "flight potion", "10 gold", "10 copper", "5 copper", "1 gold", "5 gold", "1 copper", "20 gold",]
    searchedloot = []
    iinventory = []
    enemytypes = ["orc", "human",]
    location = random.choice(locations)
    print("You are at a {}".format(location))
    prints = "Welcome!" + "Command list: \n say () \n examine () \n attack () \n look \n move \n loot \n dodge \n inventory \n use() \n throw()() \n rest() \n inventory \n save \n open() \n new" + "You are at a {}".format(location)

def move():
    global location
    print("You left the {}".format(location))
    prints = "You left the {}".format(location)
    location = random.choice(locations)
    add_enemy()
    return

class GameObject:
    class_name = ""
    desc = ""
    objects = {}
    
    def __init__(self, name):
        class_name = ""
        self.name = class_name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc

class Orc(GameObject):
    def __init__(self, name):
        self.class_name = "orc"
        self.health = 50
        self._desc = "A beast"
        super().__init__(name)

    @property
    def desc(self):
        global loot
        global searchedloot
        if self.health >=50:
            return self._desc
        elif self.health == 2:
            health_line = "It took damage."
        elif self.health == 1:
            health_line = "It took critical damage."
        elif self.health <= 0:
            health_line = "It is dead."
            searchedloot.append(random.choice(loot))
            searchedloot.append("orc body")
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

class Human(GameObject):
    def __init__(self, name):
        self.class_name = "human"
        self.health = 30
        self._desc = "An adventurer"
        super().__init__(name)

    @property
    def desc(self):
        global loot
        global searchedloot
        if self.health >=30:
            return self._desc
        elif self.health == 2:
            health_line = "They took damage."
        elif self.health == 1:
            health_line = "They took critical damage."
        elif self.health <= 0:
            health_line = "They are dead."
            searchedloot.append(random.choice(loot))
            searchedloot.append("human body")
        return self._desc + "\n" + health_line
    
    @desc.setter
    def desc(self, value):
        self._desc = value

class Char(GameObject):
    def __init__(self, name):
        self.class_name = "Char"
        self.health = playerhealth
        self._desc = "Yourself"
        #super().__init__(name)

    @property
    def desc(self):
        global playerhealth
        if self.health >= playerhealth:
            return self._desc
        elif self.health == 2:
            health_line = "You are badly damaged."
        elif self.health == 1:
            health_line = "You are terribly damaged."
        elif self.health <= 0:
            health_line = "You are dead."
        return self._desc + "\n" + health_line
    
    @desc.setter
    def desc(self, value):
        self._desc = value

char = Char("Character")

def look():
    global location
    global searchedloot
    print("You are at a {}".format(location))
    prints = "You are at a {}".format(location)
    print("There are:" + str(GameObject.objects))
    prints = "There are:" + str(GameObject.objects)
    if not searchedloot == None:
        print("There is: {} on the ground".format(searchedloot))
        prints = "There is: {} on the ground".format(searchedloot)
    return "You are at a {}".format(location) + "There are:" + str(GameObject.objects) + "There is: {} on the ground".format(searchedloot) 


def new_session():
    playwindow()
    global win
    win.close()
    pathnum = 1
    while path.exists("D&DCampaign{}.txt".format(str(pathnum))) == True:
        if path.exists("D&DCampaign{}.txt".format(str(pathnum))) == False:
            sessionfile = open("D&DCampaign{}.txt".format(str(pathnum)), "w+")
            sessionname = "D&DCampaign{}.txt".format(str(pathnum))
            break
        else:
            pathnum = pathnum + 1
    print("New campaign created. Access it through D&DCampaign{}.txt.".format(str(pathnum)))
    prints = "New campaign created. Access it through D&DCampaign{}.txt.".format(str(pathnum))
    start_game()

def delete_campaign_data(name):
    name.seek(0)
    name.truncate()

def save_session():
    delete_campaign_data(sessionname)
    sessionfile = open(sessionname, "a+")
    sessionfile.write(str(location))
    sessionfile.write(str(iinventory))
    sessionfile.write(str(searchedloot))
    sessionfile.write(str(char.health))
    sessionfile.write(str(rests))
    sessionfile.write(str(GameObject.objects))
    sessionfile.close()
    print("Saved!")
    prints = "Saved!"

def open_session(name):
    playwindow()
    global win
    global location
    global iinventory
    global searchedloot
    global rests
    win.close()
    if path.exists(name) == True:
        name = open(name, "r")
        sessionlines = name.readlines()
        location = ast.literal_eval(sessionlines[0])
        iinventory = ast.literal_eval(sessionlines[1])
        searchedloot = ast.literal_eval(sessionlines[2])
        char.health = sessionlines[3]
        rests = sessionlines[4]
        GameObject.objects = ast.literal_eval(sessionlines[5])
        print("Opened!")
        prints = "Opened!"
    else:
        print("This file doesn't exist. Try D&DCampaign.txt files.")
        prints = "This file doesn't exist. Try D&DCampaign.txt files."

def add_enemy():
    global developer
    enemychoice = random.choice(enemytypes)
    if enemychoice == "orc":
        orc = Orc("orc")
    else:
        if enemychoice == "human":
            human = Human("human")
        else:
            if developer == True:
                print("developer: summon_error: No such class exists: {}".format(enemychoice))
                prints = "developer: summon_error: No such class exists: {}".format(enemychoice)
                return

def developer():
    global developer
    if developer == True:
        print("developer: Developer deactivated")
        prints = "developer: Developer deactivated"
        developer = False
    else:
        developer = True
        print("developer: Developer activated")
        prints = "developer: Developer activated"
        print("Developer command list:")
        prints = "Developer command list:" + developercommands
        print(developercommands)
    return

def summon(noun):
    global developer
    if noun == "orc":
        orc = Orc("orc")
    else:
        if noun == "human":
            human = Human("human")
        else:
            if developer == True:
                print("developer: summon_error: No such class exists: {}".format(enemychoice))
                prints = "developer: summon_error: No such class exists: {}".format(enemychoice)
                return

def counter(noun):
    global counter
    global dodged
    global prints
    counter = True
    character = GameObject.objects[noun]
    if dodged == False:
        character.health = character.health - 10
        if character.health <= 0:
            msg = "You are dead."
        else:
            print("They attacked back.")
            msg = "You took damage."
    else:
        msg = "Dodged attack."
    dodged = False
    counter = False
    prints = msg
    return msg

def attack(noun):
    global prints
    global searchedloot
    if noun in GameObject.objects:
        prints = "Type of attack"
        attacktype = input("Type of attack")
        prints = "Roll for strength"
        strength = int(input("Roll for strength"))
        if attacktype == "melee":
            attackdamage = 5 + int(strength)
        elif attacktype == "ranged":
            attackdamage = 4 + int(strength)
        elif attacktype == "spell":
            spell = input("Spell name")
            if spell == "Suggestion":
                action = input("Suggest:")
                print("They did '{}'".format(action))
            elif "fire" in spell:
                attackdamage = 8 + int(strength)
            elif "lightning" in spell:
                attackdamage = 5 + int(strength)
            elif spell == "Mage Hand":
                if not searchedloot == None:
                    prints = "What would you like to grab?" + searchedloot
                    magesearch = input("What would you like to grab?" + searchedloot)
                    if magesearch in searchedloot:
                        print("You collected a {}".format(magesearch))
                        prints = "You collected a {}".format(magesearch)
                        searchedloot.remove(magesearch)
                    else:
                        print("There is no {} here.".format(magesearch))
                        prints = "There is no {} here.".format(magesearch)
                else:
                    print("There is nothing to grab.")
                    prints = "There is nothing to grab."
            elif spell == "Fly":
                print("You are now flying.")
                prints = "You are now flying."
            elif spell == "Eldritch Blast":
                attackdamage = 10 + int(strength)
        else:
            print("{} does not exist. Try using melee, ranged, or a type of spell.".format(attacktype))
            prints = "{} does not exist. Try using melee, ranged, or a type of spell.".format(attacktype)
        if strength >= 10:
            thing = GameObject.objects[noun]
            thing.health = thing.health - attackdamage
            if thing.health <= 0:
                msg = "You killed the creature."
            else:
                msg = "You attacked the {}".format(thing.class_name)
        else:
            print("You missed!")
            prints = "You missed!"
            print(counter(Char))
    else:
        msg = "There is no {} here.".format(noun)
    prints = msg
    return msg
    print(msg)

def examine(noun):
    global prints
    if noun in GameObject.objects:
        prints = "Roll for intelligence."
        intelligence = int(input("Roll for intelligence."))
        if intelligence >= 10:
            return GameObject.objects[noun].get_desc()
        else:
            print("Failed!")
            prints = "Failed!"
            return "Failed!"
    else:
        prints = "There is no {} here.".format(noun)
        return "There is no {} here.".format(noun)

graphics()

prints = "New Game or Continue?"
if input("New Game or Continue? ") == "New Game":
    start_game()
else:
    prints = "Game File Name:"
    gamefile = input("Game File Name:")
    open_session(gamefile)

verb_dict = {"say": say, "examine": examine, "attack": attack, "look": look, "move": move, "loot": iloot, "dodge": dodge, "developer": developer, "inventory": inventory, "use": use, "throw": throw, "rest": rest, "save": save_session, "open": open_session, "new": new_session,}
developercommands = {"developer": developer, "summon": summon, "add enemy": add_enemy, "teleport": teleport,}

def getinput():
    command = input("").split()
    try:
        verb_word = command[0]
        if verb_word in verb_dict:
            verb = verb_dict[verb_word]
        else:
            if verb_word in developercommands:
                verb = developercommands[verb_word]
            else:
                print ("Unknown verb {}".format(verb_word))
                prints = "Unknown verb {}".format(verb_word)
    except:
        print("Insert a command")
        prints = "Insert a command"
        
    if len(command) >= 2:
        try:
            noun_word = command[1]
            print(verb(noun_word))
        except:
            print()
    else:
        print(verb())
        
while True:
    playwindow()
    getinput()
