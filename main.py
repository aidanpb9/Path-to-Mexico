from Modules.utils import load_game, rand_pc_password, player_money, clear, slow_print, text_buffer, yes_no_input, encode_password
from Modules.Modules_Rooms import Rooms
from Modules.Modules_Story import Story
import random


def main():
    #making story object
    story = Story()

    #a dict of story events
    story_sequence = {
        "current_room": "bedroom",
        "money": None,
        "tv_on": False,
        "tv_channel": random.choice(list(Story.tv_program.keys())),
        "leave_first_room": False,
        "has_bedroom_key": False,
        "unlocked_bedroom": False,
        "examined_bedroom": False,
        "packed_bag": False,
        "has_car_keys": False,
        "access_pc_once": False,
        "attic_discovered": False,
        "knows_password": False,
        "pc_password": None,
        "website_open": False,
        "bought_ticket": False,
        "unlock_car": False,
        "suitcase_in_car": False,
        "part1_complete": False
    }

    #loading new or existing game
    clear()
    start_game_input = yes_no_input("Do you have an existing game? y/n: ")
    if start_game_input:
        new_data = load_game()
        if new_data:
            story_sequence = new_data
            slow_print("Game Loaded!")
            text_buffer()
        else:
            clear()
            slow_print("No game found...Press Enter")
            text_buffer()
            start_game_input = False
    if not start_game_input:
        story_sequence["money"] = player_money()
        story_sequence["pc_password"] = encode_password(rand_pc_password())
        clear()
        slow_print("Starting new game...Press Enter")
        text_buffer()
        story.intro()

    room = Rooms(story_sequence)

    #main loop for game
    while not story_sequence["part1_complete"]:
        #room.get_current_room()
        room.main_options()


if __name__ == "__main__":
    main()