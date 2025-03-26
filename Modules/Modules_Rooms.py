from Modules.utils import clear, slow_print, text_buffer, yes_no_input, nums_input, room_u_to_s, room_input
from Modules.Modules_Story import Story
import random


#navigation and tasks for each room
class Rooms:


    def __init__(self, story_sequence):
        self.story_sequence = story_sequence


    @staticmethod
    def main_options() -> int:
        prompt = "1-leave room     2-examine room     3-map     4-save game\n"
        valid_options = [1,2,3,4]
        return nums_input(prompt, valid_options)


    def get_current_room(self):
        clear()
        slow_print(f"You are in the {room_u_to_s(self.story_sequence["current_room"])}.")


    def get_adj_rooms(self):
        adjacent_rooms = {
            "bedroom": ["living_room"],
            "living_room": ["bedroom", "kitchen", "entrance_room", "upstairs_room"],
            "kitchen": ["living_room", "garage"],
            "garage": ["kitchen"],
            "upstairs_room": ["living_room"],
            "attic": ["upstairs_room"],
            "entrance_room": ["living_room"]
        }
        return adjacent_rooms.get(self.story_sequence["current_room"], [])


    def leave_room(self) -> str:
        if self.story_sequence["has_bedroom_key"]:
            if not self.story_sequence["unlocked_bedroom"]:
                clear()
                slow_print("You used the bedroom key to unlock the door!")
                text_buffer()
                self.story_sequence["unlocked_bedroom"] = True
            clear()

            adjacent_rooms = self.get_adj_rooms()
            room_select = room_input(adjacent_rooms)
            self.story_sequence["current_room"] = room_select
        else:
            clear()
            slow_print("\"Seems the bedroom door is locked.")
            slow_print("I'll look around for a key...\"")
            text_buffer()
        return self.story_sequence["current_room"]


    def examine_room(self):
        examine_room = f"examine_{self.story_sequence["current_room"]}"
        call_examine = getattr(self, examine_room)
        call_examine()


    @staticmethod
    def map_no_attic():
        clear()
        slow_print("Here is a map of the house:\n")
        print("             entrance")
        print("                 |    ")
        print("bedroom-----living room-----kitchen-----garage")
        print("                 |    ")
        print("             upstairs-----?????")
        text_buffer()


    @staticmethod
    def map_with_attic():
        clear()
        slow_print("Here is a map of the house:\n")
        print("             entrance")
        print("                 |    ")
        print("bedroom-----living room-----kitchen-----garage")
        print("                 |    ")
        print("             upstairs-----attic")
        text_buffer()


    def examine_bedroom(self):

        if not self.story_sequence["examined_bedroom"]:
            clear()
            Story.intro2()
            self.story_sequence["examined_bedroom"] = True

        if not self.story_sequence["packed_bag"]:
            while True:
                clear()
                slow_print("There is a window, a suitcase, and a dresser.")
                slow_print("What would you like to examine?")
                prompt = "1-window\t2-suitcase\t 3-dresser\t4-stop examining\n"
                valid_options = [1, 2, 3, 4]
                user_action = nums_input(prompt, valid_options)

                if user_action == 1:
                    clear()
                    slow_print("A nice day outside, I should pack my suitcase for Mexico!")
                    text_buffer()

                elif user_action == 2:
                    clear()
                    prompt = "Will you pack your suitcase? y/n: "
                    pack_case_input = yes_no_input(prompt)
                    if pack_case_input:
                        clear()
                        slow_print("Suitcase all packed!")
                        text_buffer()
                        self.story_sequence["packed_bag"] = True
                        return self.examine_bedroom()
                    else:
                        clear()
                        slow_print("You did not pack your suitcase.")
                        text_buffer()

                elif user_action == 3:
                    self.examine_bedroom_dresser()

                elif user_action == 4:
                    break

        else:
            while True:
                clear()
                slow_print("There is a window and a dresser.")
                slow_print("What would you like to examine?")
                prompt = "1-window\t 2-dresser\t3-stop examining\n"
                valid_options = [1, 2, 3]
                user_action = nums_input(prompt, valid_options)

                if user_action == 1:
                    clear()
                    slow_print("It's a lovely day outside!")
                    text_buffer()

                elif user_action == 2:
                    self.examine_bedroom_dresser()

                elif user_action == 3:
                    break


    def examine_bedroom_dresser(self):
        clear()
        if self.story_sequence["has_bedroom_key"]:
            slow_print("You check the dresser, but don't find anything.")
            text_buffer()
        else:
            slow_print("There seems to be a key hidden in the sock drawer!")
            prompt = "Will you take the key? y/n: "
            takes_key_input = yes_no_input(prompt)

            if takes_key_input:
                clear()
                slow_print("Acquired the bedroom key.")
                text_buffer()
                self.story_sequence["has_bedroom_key"] = True
            else:
                clear()
                slow_print("You did not grab the key.")
                text_buffer()


    @staticmethod
    def examine_living_room():
        while True:
            clear()
            slow_print("There is a couch and a tv in the living room.")
            slow_print("What would you like to examine?")
            prompt = "1-couch     2-tv     3-stop examining\n"
            valid_options = [1, 2, 3]
            user_action = nums_input(prompt, valid_options)

            if user_action == 1:
                clear()
                slow_print("The couch is quite comfortable.")
                text_buffer()
            elif user_action == 2:
                clear()
                slow_print("The tv isn't working right now.")
                text_buffer()
            elif user_action == 3:
                break


    @staticmethod
    def examine_kitchen():
        while True:
            clear()
            slow_print("The kitchen is well lit and has a large fridge.")
            slow_print("What would you like to examine?")
            prompt = "1-fridge     2-stop examining\n"
            valid_options = [1, 2]
            user_action = nums_input(prompt, valid_options)

            if user_action == 1:
                clear()
                slow_print("The fridge is packed! But I'm not hungry now.")
                text_buffer()
            elif user_action == 2:
                break


    def examine_entrance_room(self):
        if self.story_sequence["has_car_keys"]:
            clear()
            slow_print("The hall is well decorated.")
            text_buffer()
        else:
            clear()
            slow_print("There is a table with some keys on it.")
            prompt = "Will you take the keys? y/n: "
            take_car_keys_input = yes_no_input(prompt)

            if take_car_keys_input:
                clear()
                slow_print("Acquired car keys.")
                text_buffer()
                self.story_sequence["has_car_keys"] = True
            else:
                clear()
                slow_print("You did not take the keys")
                text_buffer()


    def examine_garage(self):
        while True:
            clear()
            slow_print("The car in here can take you to the airport.")
            slow_print("What would you like to do?")
            prompt = "1-unlock car     2-place suitcase in car     3-start car     4-stop examining\n"
            valid_options = [1, 2, 3, 4]
            user_input = nums_input(prompt, valid_options)

            if user_input == 1:
                if not self.story_sequence["has_car_keys"]:
                    clear()
                    slow_print("You do not have the car keys.")
                    text_buffer()
                else:
                    clear()
                    slow_print("Car is unlocked.")
                    text_buffer()
                    self.story_sequence["unlock_car"] = True

            elif user_input == 2:
                if not self.story_sequence["unlock_car"]:
                    clear()
                    slow_print("You need to unlock the car first.")
                    text_buffer()
                elif not self.story_sequence["packed_bag"]:
                    clear()
                    slow_print("You have not packed a suitcase yet.")
                    text_buffer()
                else:
                    clear()
                    slow_print("Suitcase is in the car.")
                    text_buffer()
                    self.story_sequence["suitcase_in_car"] = True

            elif user_input == 3:
                if not self.story_sequence["unlock_car"]:
                    clear()
                    slow_print("You need to unlock the car first.")
                    text_buffer()
                elif not self.story_sequence["suitcase_in_car"]:
                    clear()
                    slow_print("Leaving without your suitcase?")
                    text_buffer()
                elif not self.story_sequence["bought_ticket"]:
                    clear()
                    slow_print("How will you board a flight with no plane ticket?")
                    text_buffer()
                else:
                    clear()
                    slow_print("Headed to the airport. Part 1 complete!")
                    text_buffer()
                    self.story_sequence["part1_complete"] = True
                    break

            elif user_input == 4:
                break


    def examine_upstairs_room(self):
        if not self.story_sequence["access_pc_once"]:
            clear()
            slow_print("Seems like the room is empty except for the computer.")
            prompt = "Will you turn on the computer? y/n: "
            start_pc_input = yes_no_input(prompt)

            if start_pc_input:
                Story.attic_discovery()
                self.story_sequence["access_pc_once"] = True
                return self.examine_attic()
            else:
                clear()
                slow_print("That's fine. It didn't want to be turned on anyways.")
                text_buffer()

        else:
            while True:
                clear()
                slow_print("What would you like to examine?")
                prompt = "1-pc     2-super duper top secret hole in the wall     3-stop examining\n"
                valid_options = [1, 2, 3]
                user_action = nums_input(prompt, valid_options)

                if user_action == 1:
                    clear()
                    slow_print("Booting up the pc...")
                    text_buffer()
                    self.pc_pass()

                elif user_action == 2:
                    clear()
                    slow_print("Entering the attic.")
                    text_buffer()
                    return self.examine_attic()

                elif user_action == 3:
                    break


    def pc_pass(self):
        user_pass = input("Enter pc password: ")
        if user_pass == self.story_sequence["pc_password"]:
            if not self.story_sequence["website_open"]:
                Story.website_instructions()
                self.story_sequence["website_open"] = True
            self.buy_tickets()
        else:
            clear()
            slow_print("Incorrect Password.")
            text_buffer()


    @staticmethod
    def generate_flight():
        # initialize seats 6 rows 4 cols
        seats = [['x' for _ in range(4)] for _ in range(6)]

        # initialize prices 6 rows 4 cols
        prices = [[0 for _ in range(4)] for _ in range(6)]

        # open seats
        num_open_seats = random.randint(2, 8)
        open_seats = random.sample(range(24), num_open_seats)

        # make array
        for seat in open_seats:
            row = seat // 4
            col = seat % 4

            # price increases for front seats
            price = 0
            if row == 0 or row == 1:
                price = random.randint(140, 180)
            elif row == 2 or row == 3:
                price = random.randint(110, 140)
            elif row == 4 or row == 5:
                price = random.randint(80, 120)

            seats[row][col] = col + 1
            prices[row][col] = price
        return seats, prices


    @staticmethod
    def display_flight(seats):
        row_labels = ('A', 'B', 'C', 'D', 'E', 'F')

        for i, row in enumerate(seats):
            row_label = row_labels[i]
            seat_row = ' '.join(str(seat) for seat in row)
            print(f"{row_label} {seat_row}")


    def check_flight_prices(self) -> bool:
        prices = self.generate_flight()[1]
        min_price = float("inf")

        for row in prices:
            for price in row:
                if price > 0:
                    min_price = min(min_price, price)

        if min_price != float("inf") and self.story_sequence["money"] >= min_price:
            return True
        else:
            clear()
            print("All tickets are too expensive on this flight, try again later.")
            text_buffer()
            return False


    def buy_tickets(self):
        letter_convert = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5 }

        seats, prices = self.generate_flight()
        if not self.check_flight_prices():
            return

        ticket = None
        while ticket != 'Q':
            clear()
            slow_print(f"You have ${self.story_sequence["money"]}")
            self.display_flight(seats)
            ticket = input("Which seat would you like to buy (Q to quit): ").strip().upper()

            if ticket == 'Q':
                break

            if len(ticket) != 2 or ticket[0] not in letter_convert or not ticket[1].isdigit():
                clear()
                slow_print(f"{ticket} does not exist.")
                text_buffer()
                continue

            row = letter_convert[ticket[0]]
            col = int(ticket[1]) - 1
            price = prices[row][col]

            if col < 0 or col >= 4:
                clear()
                slow_print(f"{ticket} does not exist.")
                text_buffer()
                continue

            if seats[row][col] == 'x':
                clear()
                slow_print(f"{ticket} is not available.")
                text_buffer()
                continue

            if seats[row][col] != 'x' and price > 0:
                clear()
                slow_print(f"The price of seat {ticket} is ${price}.")
                prompt = "Will you buy the ticket? y/n: "
                buy_seat_input = yes_no_input(prompt)

                if buy_seat_input:
                    if price <= self.story_sequence["money"]:
                        clear()
                        slow_print(f"Congrats! Purchased seat {ticket} for ${price}!")
                        text_buffer()
                        self.story_sequence["bought_ticket"] = True
                        self.story_sequence["money"] -= price
                        seats[row][col] = 'x'
                        prices[row][col] = 0
                    else:
                        clear()
                        slow_print(f"Sorry, you don't have enough money for {ticket}.")
                        text_buffer()
                else:
                    clear()
                    slow_print(f"Did not purchase seat {ticket}.")
                    text_buffer()
            else:
                clear()
                slow_print(f"{ticket} not available.")
                text_buffer()


    def examine_attic(self):
        self.story_sequence["current_room"] = "attic"

        while True:
            clear()
            slow_print("There isn't much in here. A couple of old boxes. But there's a sticky note on the wall.")
            slow_print("What would you like to examine?")
            prompt = "1-sticky note     2-stop examining\n"
            valid_options = [1, 2]
            user_action = nums_input(prompt, valid_options)

            if user_action == 1:
                clear()
                slow_print(f"Scribbled on the sticky note is: \033[4m{self.story_sequence["pc_password"]}\033[0m")
                text_buffer()

            elif user_action == 2:
                break