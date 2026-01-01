# A text-based adventure game with sound effects using pygame

import pygame
import time

# Initialize the mixer for sound
pygame.mixer.init()

# Load sound files
win_sound = pygame.mixer.Sound("win_music.mp3")
lose_sound = pygame.mixer.Sound("lose_music.mp3")

def play_win_sound():
    win_sound.play()
    time.sleep(2)

def play_lose_sound():
    lose_sound.play()
    time.sleep(2)

def start_game():
    name = input("Enter your name: ")
    print(f"Welcome to the adventure game! {name}, your journey begins now.")

    # Loop until a valid choice is made
    while True:
        initial_choice = input("Do you want to explore a forest or enter a cave? (forest/cave): ").lower()
        if initial_choice == "forest":
            forest_path()
            break
        elif initial_choice == "cave":
            cave_path()
            break
        else:
            print("Invalid choice. Please choose 'forest' or 'cave'.")

def forest_path():
    while True:
        print("\n--------You enter a lush forest filled with towering trees and chirping birds--------")
        choice = input("Do you want to follow the river or climb the tree? (river/tree): ").lower()
        if choice == "river":
            print("\n-------You follow the river and hear rushing water ahead.---------")
            river_choice = input("Do you want to investigate the sound or look for fish? (investigate/fish): ").lower()
            if river_choice == "investigate":
                print("\n------You find a waterfall hiding a secret cave! Inside, you discover ancient paintings.-------")
                more_info = input("Do you want to explore the cave or return to the forest? (explore/return): ").lower()
                if more_info == "explore":
                    print("-----------🏆🏆🏆YOU WIN! Tresure chest filled with gold and jewels!----------")
                    play_win_sound()
                    break  # End game after win
                elif more_info == "return":
                    print("-------😒😒😒YOU LOSE,You take a souvenir and feel lucky!-------------")
                    play_lose_sound()
                    break  # End game after lose    
                else:
                    print("Invalid choice. You return to the forest path.")
                    continue

            elif river_choice == "fish":
                print("-------You catch a magical fish that grants you a wish. -------")
                more_choice = input("Do you want to make a wish or release the fish? (wish/release): ").lower()
                if more_choice == "wish":
                    generate_wish = input("What do you wish for? (riches/power/friendship): ").lower()
                    if generate_wish in ["riches", "power", "friendship"]:
                        print(f"---🏆🏆🏆YOU WIN!Your wish for {generate_wish} comes true!----")
                        play_win_sound()    
                    else:                             
                        print("Invalid wish. The fish swims away.")
                elif more_choice == "release":
                    print("-- 😒😒😒 YOU LOSE!You release the fish back into the river!---")
                    play_lose_sound()
                else:
                    print("Invalid choice. The fish escapes on its own.")
                break  # End this path
            else:
                print("Invalid choice by the river. You return to the forest path.")
                continue

        elif choice == "tree":
            print("\n-------You climb the tree and get a view of the entire forest.-----")
            tree_choice = input("Do you want to look for smoke or search for fruit? (smoke/fruit): ").lower()
            if tree_choice == "smoke":
                print("------You see smoke rising in the distance. You follow it and find a peaceful village.------")
                find_treasure = input("Do you want to explore the village or look for treasure? (explore/treasure): ").lower()
                if find_treasure == "explore":
                    print("----😒😒😒YOU LOSE!, You explore the village and make new friends.----")
                    play_lose_sound()
                elif find_treasure == "treasure":
                    print("----🏆🏆🏆YOU WIN!, You find a hidden treasure chest in the village!----")
                    play_win_sound()
                else:
                    print("Invalid choice. The villagers guide you back to safety.")
                break  # End this path
            elif tree_choice == "fruit":
                print("-----You find glowing fruit that heals your wounds. You feel stronger!-----")
                fruit_choice = input("Do you want to eat the fruit or save it for later? (eat/save): ").lower()

                if fruit_choice == "eat":
                    print("---🏆🏆🏆 YOU WIN!You eat the fruit and gain magical powers!----")
                    play_win_sound()
                elif fruit_choice == "save":
                    print("😒😒😒YOU LOSE!You save the fruit for later and continue your adventure feeling prepared.")
                    play_lose_sound()
                else:
                    print("Invalid choice. You accidentally drop the fruit.")
                break  # End this path

            else:
                print("Invalid choice. You climb down unsure of what to do next.")
                continue

        else:
            print("Invalid path. Please choose 'river' or 'tree'.")

def cave_path():

    print("-------You step into a dark, damp cave.-------")
    while True:
        choice = input("Do you want to light a torch or proceed in the dark? (torch/dark): ").lower()
        if choice == "torch":
            print("----You light a torch, revealing ancient carvings on the walls.-----")
            torch_choice = input("Do you want to examine the carvings or follow the tunnel? (examine/follow): ").lower()
            if torch_choice == "examine":
                print("---🏆🏆🏆YOU WIN The carvings reveal a map and you find gold.--")
                play_win_sound()
            elif torch_choice == "follow":
                print("---😒😒😒YOU LOSE.You find rock crystals but they are cursed!-----")
                play_lose_sound()
            else:
                print("Invalid torch choice. You drop the torch and return to the entrance.")

            break

        elif choice == "dark":
            print("------You move forward slowly in the darkness, feeling your way.-----")
            dark_choice = input("You hear a growl nearby. Do you run or hide? (run/hide): ").lower()
            
            if dark_choice == "run":
                print("----You trip and fall into a pit. Luckily, it leads to an underground lake with a boat!---")
                more_option = input("Do you want to take the boat or swim? (boat/swim): ").lower()
                if more_option == "boat":
                    print("----🏆🏆🏆YOU WIN!You sail to safety and find a treasure island!----")
                    play_win_sound()
                elif more_option == "swim":
                    print("----😒😒😒YOU LOSE!You swim but the current is too strong and you get lost.----")
                    play_lose_sound()
                else:
                    print("Invalid choice. You decide to stay in the pit and wait for help.")
            elif dark_choice == "hide":
                print("You hide quietly. The growl fades. You discover a glowing mushroom path leading to safety.")
                more_option = input("Do you want to follow the mushroom path or go back? (follow/back): ").lower()
                if more_option == "follow":
                    print("----🏆🏆🏆YOU WIN!You follow the path and find a hidden treasure chest!----")
                    play_win_sound()
                elif more_option == "back":
                    print("😒😒😒YOU LOSE,You go back to the cave entrance safely.")
                    play_lose_sound()
                else:
                    print("Invalid choice. You stay hidden until you are rescued.")
            else:
                print("Invalid choice in the dark. You get lost and must exit the cave.")

            break
        else:
            print("Invalid cave action. Please choose 'torch' or 'dark'.")



if __name__ == "__main__":
    while True:
        start_game()
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye!")
            break