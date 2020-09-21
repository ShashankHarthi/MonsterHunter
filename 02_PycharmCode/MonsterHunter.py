import time
import os
import threading
from queue import Queue

end_game = 0


class Hero:
    """
    Class to create Hero attributes and function.

    Attributes:
        health: the health points of the hero
        attack_strength: the attack strength of the hero object.
    """
    health = 40
    attack_strength = 2

    def __init__(self):
        """
        class instance initialisation function

        Object attributes:
            health: health points of the hero class object.
        """
        self.health = Hero.health


class Monster:
    """
    class to create Monsters attributes and methods.

    Methods:
        attack_hero: method to calculate the actions after a monster attack hero
        attacked_by_hero: method to calculate the actions after hero attack the monsters.
    """

    def __init__(self, health, attack_time, alive, attack_counter, attack_strength):
        """
        class instance initialisation function

        Object attributes:
            health: health points of the hero class object.
            attack_time: the attack time of the current instance monster.
            alive: the attribute to defines weather the monster is alive or dead.
            attack_counter: the number of time the monster has already attacked.
            attack_strength: the attack strength of the monster.
        """
        self.health = health
        self.attack_time = attack_time
        self.alive = alive
        self.attack_counter = attack_counter
        self.attack_strength = attack_strength

    def attack_hero(self, hero):
        """
        The method to update the attributes after a monster attack the man.

        :param hero: hero object to calculate the new health points based on the monster attack.

        :return: hero object after update.
        """
        hero.health = hero.health - self.attack_strength
        self.attack_counter = self.attack_counter + 1
        return hero

    def attacked_by_hero(self):
        """
        The mehod to update the attributes after the hero attack the monster.

        """
        self.health = self.health - Hero.attack_strength

def print_update(time_elapsed , hero , orc , dragon):
    """
    Function to print the updated health points after each action.
    :param time_elapsed: elapsed time
    :param hero: hero object
    :param orc: orc object
    :param dragon: dragon object
    """
    print("\nElapsed time = {}".format(time_elapsed))
    print("Remaining health of our Hero: {}".format(hero.health))
    print("Remaining health of the Orc: {}".format(orc.health))
    print("Remaining health of the Dragon: {}".format(dragon.health))


def game_loop(q):
    """
    The main game function. This function is called when the user starts the game.
    The main sequences ofthe game areimplemented here.

    :param q: 'q' is the queue to append the user commands used for the hero attacks.
    """

    #All the initial parameters to create monster and hero instances.
    time.sleep(0.1)
    orc_health = 7
    dragon_health = 20
    orc_alive = 1
    dragon_alive = 1
    orc_attack_time = 1.5
    dragon_attack_time = 2
    orc_attack_counter = 1
    dragon_attack_counter = 1
    orc_attack_strength = 1
    dragon_attack_strength = 3

    hero = Hero()
    orc = Monster(orc_health, orc_attack_time, orc_alive, orc_attack_counter, orc_attack_strength)
    dragon = Monster(dragon_health, dragon_attack_time, dragon_alive, dragon_attack_counter, dragon_attack_strength)

    time_0 = time.time() #initial time when the game play started
    global end_game

    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

    while end_game == 0:
        time_1 = time.time() #current time
        time_elapsed = time_1 - time_0

        # the player actions are checked and performed.
        while not q.empty():  # check queue for user action commands.
            hero_attack = q.get()

            # player attack orc
            if hero_attack == 'attack orc':
                if orc.alive == 1:
                    print("\n\nHero attacked Orc and Orc health reduced by 2")
                    orc.attacked_by_hero()
                    print_update(time_elapsed, hero, orc, dragon)

                    if orc.health <= 0:
                        print("\n\nGood Job the Orc is dead")
                        orc.alive = 0

                else:
                    print("\n\nOrc is already dead, kill the Dragon now")

            # player attack dragon
            elif hero_attack == 'attack dragon':
                if dragon.alive == 1:
                    print("\n\nHero attacked Dragon and Dragon health reduced by 2")
                    dragon.attacked_by_hero()
                    print_update(time_elapsed, hero, orc, dragon)

                    if dragon.health <= 0:
                        print("\n\nGood Job the Dragon is dead")
                        dragon.alive = 0

                else:
                    print("\n\nDragon is dead, kill the Orc now")

            else:
                print(
                    "\nInvalid attack input.\nPossible Inputs:\n'attack dragon' to attack the Dragon for 2 health points.\n'attack orc' to attack the Orc for 2 health points")

        #the Orc attack sequence.
        if orc.alive == 1:
            if (time_elapsed >= (orc.attack_time * orc.attack_counter)):
                print("\n\nOrc attacked our Hero")
                hero = orc.attack_hero(hero)
                print_update(time_elapsed, hero, orc, dragon)

        #the Dragon attack sequence.
        if dragon.alive == 1:
            if (time_elapsed >= (dragon_attack_time * dragon.attack_counter)):
                print("\n\nDragon attacked our Hero")
                hero = dragon.attack_hero(hero)
                print_update(time_elapsed, hero, orc, dragon)


        #check of the hero health is zero.
        if hero.health <= 0:
            print("\n***** L O S T *****\n\nHero died.\n\n*****GAME ENDED*****")
            print("\n\nType anything to exit game")
            end_game = 1

        #check if the hero killed both monsters.
        if ((orc.alive == 0) and (dragon.alive == 0)):
            print("\n***** V I C T O R Y *****\n\nHero killed both the monsters.\n\n*****GAME ENDED*****")
            print("Type anything to end game")
            end_game = 1



def start_game():
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

    start_game = 1

    #game start loop
    while start_game == 1:
        #welcome statements and the instructions
        user_input = input(
            "\n\n************* Welcome to **************\n***** M o n s t e r - H u n t e r *****"
            "\n\nInstructions: Our brave hero is attacked by an Orc and a Dragon."
            "\nOur hero involves in a fight with both the monsters.\nYou the player is the hero and you can attack the monsters by using below commands."
            "\n\na. To attack the Orc: type 'attack orc'\nb. To attack the Dragon: type 'attack dragon'"
            "\n\nThe game is won by killing both the monsters before they kill our hero"
            "\n\nEnter 'go' to start the game.\nEnter 'end' to exit game")
        user_input = user_input.lower()

        #user input check
        if user_input == 'go':
            print("\nMonster attack started")
            #game staeted
            start_game = 0

            #q - the queue to append the user commands.
            q = Queue()
            t = threading.Thread(target=game_loop, args=(q,), daemon=True) #thread the game loop to run parellel with input.
            t.start() #start the thread

            print("\nType input to attack: \n\n")
            #check for user attack inputs.
            while end_game == 0:
                hero_attack = input()
                hero_attack = hero_attack.lower()
                q.put(hero_attack)

            #end the thread after completion of the game loop
            t.join()

        #exit game as per user choice
        elif user_input == 'end':
            start_game = 0
            print("\nYou exitted the game")

        #invalid user input to start the game
        else:
            print("\nInvalid input. Please enter 'go' to start the game or Enter 'end' to exit game.")

    print("Game successfully exited")
    time.sleep(60)

if __name__ == "__main__":
    start_game()