import os
import sys
import time
import json
import random
import string
import msvcrt
import base64
from dataclasses import dataclass
from typing import Union

#constants
STARTING_MIN_MONEY = 110
STARTING_MAX_MONEY = 200
INSTANT_TYPE_SPEED = 0
FAST_TYPE_SPEED = .017
SLOW_TYPE_SPEED = .03


#class for user settings
@dataclass
class Settings:
    type_speed: float = FAST_TYPE_SPEED


    def to_dict(self):
        return {"type_speed": self.type_speed}


    def from_dict(self, settings_dict):
        self.type_speed = settings_dict.get("type_speed", self.type_speed)


#initialize settings
settings = Settings()


#checks if terminal is real or pycharm
def in_ide() -> bool:
    return 'PYCHARM_HOSTED' in os.environ


#clears terminal
def clear() -> None:
    if in_ide():
        print("\n" * 50)
    else:
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")


# prints text to terminal slowly
def slow_print(text, end="\n") -> None:
    delay = settings.type_speed

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

    while msvcrt.kbhit():
        msvcrt.getch()


#change user type speed in settings
def user_type_speed() -> None:
    clear()

    speed_mapping = {1: INSTANT_TYPE_SPEED, 2: FAST_TYPE_SPEED, 3: SLOW_TYPE_SPEED}
    name_mapping = {INSTANT_TYPE_SPEED: "Instant" , FAST_TYPE_SPEED: "Fast" , SLOW_TYPE_SPEED: "Slow"}

    current_mode = name_mapping[settings.type_speed]
    prompt = f"Current Mode: {current_mode}\n1-Instant     2-Fast     3-Slow\n"
    valid_options = [1,2,3]
    user_input = nums_input(prompt, valid_options)

    speed_select = speed_mapping[user_input]
    settings.type_speed = speed_select


#to pause text in terminal
def text_buffer() -> None:
    input(">")


#to save the game
def save_game(story_sequence: dict, filename: str ="saved_game.json") -> None:
    story_sequence["settings"] = settings.to_dict()
    with open(filename, 'w') as file:
        # noinspection PyTypeChecker
        json.dump(story_sequence, file)
    clear()
    slow_print("Game Saved!")
    text_buffer()


#to load an existing game
def load_game(filename: str = "saved_game.json") -> dict:
    try:
        with open (filename, 'r') as file:
            story_sequence = json.load(file)
        if "settings" in story_sequence:
            settings.from_dict(story_sequence["settings"])
        return story_sequence

    except FileNotFoundError:
        return {}


#quit running the program
def exit_game() -> None:
    clear()
    prompt = "Are you sure you want to exit? y/n: "
    exit_input = yes_no_input(prompt)

    if exit_input:
        clear()
        slow_print(exit_messages())
        sys.exit()


#gives different message when quitting game
def exit_messages() -> str:
    messages = ("Goodbye", "Adiós", "Au revoir", "Tschüss", "Ciao", "Sayonara", "До свидания", "Farewell")
    exit_message = random.choice(messages)
    return exit_message


#error checking for yes/no options
def yes_no_input(prompt: str) -> bool:
    while True:
        slow_print(prompt, end="")
        user_input = input().strip().lower()
        if user_input == 'y' or user_input == "yes":
            return True
        elif user_input == 'n' or user_input == "no":
            return False
        else:
            clear()
            slow_print("Invalid input. Enter 'y' for yes or 'n' for no.")


#error checking for num options
def nums_input(prompt: str, valid_options: list) -> int:
    while True:
        slow_print(prompt, end="")
        try:
            user_input = int(input())
            if user_input in valid_options:
                return user_input
            else:
                clear()
                slow_print(f"Invalid input. Enter a valid number.")
        except ValueError:
            clear()
            slow_print(f"Invalid input. Enter a valid number.")


#returns rooms, has error checking
def recursive_rooms(adjacent_rooms: list, current_room: str, room_select: str = None, original_rooms: list = None) -> Union[str, None]:
    if original_rooms is None:
        original_rooms = adjacent_rooms.copy()

    adjacent_rooms.append("cancel")
    if room_select is None:
        formatted_rooms = [format_room(room) for room in adjacent_rooms]
        slow_print(f"What room? {', '.join(formatted_rooms)}: ", end="")
        room_select = raw_room(input().strip().lower())

    new_rooms = []
    for room in adjacent_rooms:
        if room.startswith(room_select) and room_select != '':
            new_rooms.append(room)

    if len(new_rooms) == 0:
        clear()
        slow_print("No rooms match that entry.")
        text_buffer()
        clear()
        return recursive_rooms(original_rooms, current_room, room_select = None, original_rooms = original_rooms)

    elif len(new_rooms) == 1:
        if new_rooms[0] == "cancel":
            return current_room
        else:
            return new_rooms[0]

    else:
        clear()
        slow_print(f"Multiple rooms match \"{format_room(room_select)}\".")
        return recursive_rooms(new_rooms, current_room, room_select = None, original_rooms = original_rooms)


#format the room to have spaces instead of underlines
def format_room(room_name: str) -> str:
    formatted_room = room_name.lower()
    formatted_room = formatted_room.replace('_', ' ')
    return formatted_room


#formatted room to raw, replaces space with underline and adds space before room if none found
def raw_room(room_name: str) -> str:
    return room_name.replace(' ', '_').lower()


#generates random pc password each game
def rand_pc_password() -> str:
    pc_password = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return pc_password


#encode pc password
def encode_password(text_password: str) -> str:
    return base64.b64encode(text_password.encode()).decode()


#decode pc password
def decode_password(encoded_password: str) -> str:
    return base64.b64decode(encoded_password.encode()).decode()


#generates random player money amount each game
def player_money() -> int:
    start_money = random.randint(STARTING_MIN_MONEY, STARTING_MAX_MONEY)
    return start_money