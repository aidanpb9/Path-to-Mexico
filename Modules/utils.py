import os
import sys
import time
import json
import random
import string
import msvcrt


#constants
MIN_MONEY = 110
MAX_MONEY = 200


#checks if terminal is real or pycharm
def in_ide():
    return 'PYCHARM_HOSTED' in os.environ


#clears terminal
def clear():
    if in_ide():
        print("\n" * 50)
    else:
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")


#prints to terminal slowly
def slow_print(text, delay=0.017, end="\n"):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

    while msvcrt.kbhit():
        msvcrt.getch()


#to pause text in terminal
def text_buffer():
    input(">")


#to save the game
def save_game(story_sequence: dict, filename="saved_game.json") -> None:

    with open(filename, 'w') as file:
        # noinspection PyTypeChecker
        json.dump(story_sequence, file)
    clear()
    slow_print("Game Saved!")


#to load an existing game
def load_game(filename = "saved_game.json") -> dict:
    try:
        with open (filename, 'r') as file:
            story_sequence = json.load(file)
        return story_sequence
    except FileNotFoundError:
        return {}


#error checking for yes/no options
def yes_no_input(prompt: str) -> bool:
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'y' or user_input == "yes":
            return True
        elif user_input == 'n' or user_input == "no":
            return False
        else:
            clear()
            slow_print("Invalid input. Enter 'y' for yes or 'n' for no.")
            text_buffer()
            clear()


#error checking for num options
def nums_input(prompt: str, valid_options: list) -> int:
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in valid_options:
                return user_input
            else:
                clear()
                slow_print(f"Invalid input.")
                text_buffer()
                clear()
        except ValueError:
            clear()
            slow_print(f"Invalid input.")
            text_buffer()
            clear()


#error checking for changing rooms
def room_input(adjacent_rooms: list) -> str:
    while True:
        formatted_rooms = [room_u_to_s(room) for room in adjacent_rooms]
        room_select = input(f"What room? {', '.join(formatted_rooms)}: ").strip()
        real_room = room_s_to_u(room_select)

        if real_room in adjacent_rooms:
            return real_room
        else:
            clear()
            slow_print("Invalid input.")
            text_buffer()
            clear()


#format room underline to space
def room_u_to_s(room_name: str) -> str:
    return room_name.replace('_', ' ')


#format room space to underline
def room_s_to_u(room_name: str) -> str:
    return room_name.replace(' ', '_')


#generates random pc password each game
def rand_pc_password():
    pc_password = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return pc_password


#generates random player money amount each game
def player_money():
    start_money = random.randint(MIN_MONEY, MAX_MONEY)
    return start_money