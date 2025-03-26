from Modules.utils import load_game, save_game, rand_pc_password, player_money
from Modules.utils import clear, slow_print, text_buffer, yes_no_input
from Modules.Modules_Rooms import Rooms
from Modules.Modules_Story import Story


def main():
    #a dict of story events
    story_sequence = {
        "current_room": "bedroom",
        "money": None,
        "examined_bedroom": False,
        "has_bedroom_key": False,
        "unlocked_bedroom": False,
        "packed_bag": False,
        "has_car_keys": False,
        "access_pc_once": False,
        "pc_password": None,
        "website_open": False,
        "bought_ticket": False,
        "unlock_car": False,
        "suitcase_in_car": False,
        "part1_complete": False
    }

    clear()
    story = Story()

    #loading assets
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
        story_sequence["pc_password"] = rand_pc_password()
        clear()
        slow_print("Starting new game...Press Enter")
        text_buffer()
        story.intro()

    room = Rooms(story_sequence)

    #main loop for game
    while not story_sequence["part1_complete"]:
        room.get_current_room()
        action = room.main_options()

        if action == 1:
            story_sequence["current_room"] = room.leave_room()
        elif action == 2:
            room.examine_room()
        elif action == 3:
            if not story_sequence["access_pc_once"]:
                room.map_no_attic()
            else:
                room.map_with_attic()
        elif action == 4:
            save_game(story_sequence)
            text_buffer()


if __name__ == "__main__":
    main()