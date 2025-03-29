from Modules.utils import clear, slow_print, text_buffer


#prints large narration sections
class Story:


    @staticmethod
    def intro() -> None:
        clear()
        slow_print("You wake up to your phone playing a voicemail.")
        slow_print(f"It is your mother's voice: \"Don't be late!\"")
        slow_print("\"What is she talking about?\", I think.")
        slow_print("Press enter to continue")
        text_buffer()


    @staticmethod
    def intro2() -> None:
        clear()
        slow_print("\"Ah I remember now...")
        slow_print("My parents are waiting for me at a resort in Mexico!")
        slow_print("I need to pack my bag, book a plane ticket, and head for the airport!\"")
        text_buffer()
        slow_print("GOALS: pack bag, book plane ticket, start car")
        text_buffer()


    @staticmethod
    def leave_first_room() -> None:
        clear()
        slow_print("Note: you can type the first letter(s) of a room name to choose it.")
        text_buffer()


    @staticmethod
    def need_bedroom_key() -> None:
        clear()
        slow_print("\"Seems the bedroom door is locked.")
        slow_print("I'll look around for a key...\"")
        text_buffer()


    @staticmethod
    def bedroom_unlock() -> None:
        clear()
        slow_print("You used the bedroom key to unlock the door!")
        text_buffer()

    @staticmethod
    def attic_discovery() -> None:
        slow_print("As you step away from the pc, you notice an out of place painting leaning against the wall.")
        slow_print("You move the painting to reveal a tunnel to the attic. Let's explore!")
        text_buffer()
        slow_print("You crawl through the hole. There must be a light around here somewhere...")
        slow_print("\"Got it! I can see.\"")
        text_buffer()
        slow_print("Map has been updated. You can now access the attic by examining the upstairs room.")
        text_buffer()


    @staticmethod
    def website_instructions() -> None:
        clear()
        slow_print("\"Oh, it looks like my parents left the website open to buy plane tickets.")
        text_buffer()
        slow_print("To buy a plane ticket, I'll enter the letter then the number, like A1 or E4.")
        text_buffer()
        slow_print("An x means the seat is full, but a number means I can buy it.\"")
        text_buffer()


    #next Tv channel for cycle channel in Rooms_tv()
    next_tv_program = {
        "News Channel": "Cooking Show",
        "Cooking Show": "Crime Show",
        "Crime Show": "Comedy Channel",
        "Comedy Channel": "Commercial Break",
        "Commercial Break": "Action Movie",
        "Action Movie": "News Channel"
    }

    #Tv channel script for Rooms_tv()
    tv_program = {
        "News Channel":'''BREAKING NEWS! A new species of frog has been discovered in the Amazon,
and scientists are calling it a game-changer for medicine!
These frogs produce a rare enzyme that could be the key to curing multiple diseases.
But wait—researchers just found out these frogs are extremely shy.''',

        "Cooking Show": '''Oops, I dropped the cake! But it’s not a disaster—it’s an artistic reimagining of a classic!
Welcome to today’s episode of "Unpredictable Bakes." The chef quickly picks up the pieces and calls it "deconstructed cake."
Hey, it’s all about presentation, right? And today's secret ingredient is... avocado! Yes, you heard that right.''',

        "Crime Show": '''The investigation just took a shocking turn...
The fingerprints found at the crime scene match the victim’s best friend!
But here’s the twist—the best friend wasn’t even supposed to be in town that night. 
Was it a setup? A hidden affair? Or could the true culprit still be out there?''',

        "Comedy Channel":'''Why do programmers prefer dark mode? Because the light attracts bugs. 
If debugging is the process of removing software bugs, then programming must be the process of putting them in.
I don’t have a bug, I have an undocumented feature.
Why do programmers hate nature? It has too many bugs.''',

        "Commercial Break":'''Introducing the brand-new SuperCar X9000!
With cutting-edge technology, a built-in espresso machine, self-healing paint, and an AI-powered backseat driver who gives motivational speeches
(because you deserve it), the SuperCar X9000 is more than a car—it’s your new best friend.
Ready for any road trip, adventure, or high-speed chase. Get yours today before they’re all gone!''',

        "Action Movie":'''The helicopter blades spin violently, cutting through the stormy skies.
"We don't need a plan. We just need to survive!"
The explosion behind them lights up the night as the heroes race towards their only escape.
"Get to the chopper! It's our only way out!"
As they dive into the helicopter, the enemy's forces are closing in fast.'''
    }