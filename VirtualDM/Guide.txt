Welcome to the Virtual Dungeon Master guide

Using Commands:
Use a command simply by typing it in when prompted. The () is recognized as an input needed by the program to comprehend that action.
For Example: (| recognizes the program's output. \ recognizes the player's input)
Example quick campaign:
| New Game or Continue?
\ New Game
| Welcome!
\ inventory
| You have nothing in your inventory.
\ look around
| You are at bar.
\ move
| You moved from bar.
\ look around
| You are at bar.
| There are: [orc, char]
\ attack orc
| Type of attack:
\ spell
| Roll for strength:
\ 15
| Spell name:
\ Eldritch Blast
| You attacked the orc
\ attack orc
| Type of attack:
\ melee
| Roll for strength:
\ 9
| You missed!
| They attacked back.
| You took damage.
\ attack orc
| Type of attack:
\ melee
| Roll for strength:
\ 18
| You killed the creature
\ loot
| There is: [health potion, orc body] on the ground
| You collected [health potion, orc body]
\ inventory
| [health potion, orc body]
\ Use health potion
| You gained health.
\ save session
| Saved!


Commands Overview:
  say()
    Words
  examine()
    Object/Entity
  attack()
    Object/Entity
      Melee
      Ranged
      Spell()
        Spell Name [common spells]
  look around
  move
  loot
  dodge
  developer
    Add Enemy
    Summon()
      Object/Entity
    Teleport()
      Location
  use()
    Item
  throw()()
  rest()
  inventory
  save session
  open session()
    Session File Name
  new session

Commands:

Say:
Say() causes your character to say whatever is in the input ().
Example: Say hello

Examine:
Examine() gives information about the character or object in the input. If there is no object there, the player will be notified.

Attack:
Attack() will allow the player to attack the object in the input to attempt to attack an object.
