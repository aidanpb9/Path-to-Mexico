from Modules.utils import clear, slow_print, text_buffer


#prints large narration sections
class Story:


    @staticmethod
    def intro():
        clear()
        slow_print("You wake up to your phone playing a voicemail.")
        slow_print(f"It is your mother's voice: \"Don't be late!\"")
        slow_print("\"What is she talking about?\", I think.")
        slow_print("Press enter to continue")
        text_buffer()


    @staticmethod
    def intro2():
        clear()
        slow_print("\"Ah I remember now...")
        slow_print("My parents are waiting for me at a resort in Mexico!")
        slow_print("I need to pack my bag, book a plane ticket, and head for the airport!\"")
        text_buffer()
        slow_print("GOALS: pack bag, book ticket, get in the car")
        text_buffer()


    @staticmethod
    def attic_discovery():
        clear()
        slow_print("\"The pc needs a password...\"")
        text_buffer()
        slow_print("As you step away from the pc, you notice an out of place painting leaning against the wall.")
        slow_print("You move the painting to reveal a tunnel to the attic. Let's explore!")
        text_buffer()
        slow_print("You crawl through the hole. There must be a light around here somewhere...")
        slow_print("\"Got it! I can see.\"")
        text_buffer()
        slow_print("Map has been updated. You can now access the attic by examining the upstairs room.")
        text_buffer()


    @staticmethod
    def website_instructions():
        clear()
        slow_print("\"Oh, it looks like my parents left the website open to buy plane tickets.")
        text_buffer()
        slow_print("To buy a plane ticket, I'll enter the letter then the number, like A1 or E4.")
        text_buffer()
        slow_print("An x means the seat is full, but a number means I can buy it.\"")
        text_buffer()