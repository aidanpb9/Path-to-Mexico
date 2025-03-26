# Path-to-Mexico

# Table of contents:

    1.Game overview
    2.How to play
    3.How the game works
    4.Hints


# Game Overview:

Path-to-Mexico is a simple game that runs in the terminal. The player navigates rooms and completes tasks in a house. The goal is to complete all necessary tasks to progress through the story. It is a ten minute playthrough. You will use provided commands to interact with the environment.

# How to play
Current Version:

1.Download Python from https://www.python.org/downloads/. You can check if python is downloaded by running "python" in your terminal

2.Clone this repository by typing in the terminal "git clone https://github.com/aidanpb9/Path-to-Mexico.git". You can simply delete the game later.

3.Navigate to the game with "cd Path-to-Mexico".

4.Start the game with "python main.py"

Important to know about gameplay:

The game will ask for a new or existing save upon startup. The save game feature will save your progress. You can close the terminal at any time after saving to exit the game. The game will prompt you for an input action. If you are stuck, scroll to the bottom of this file for help.

# How the game works

Read this section only if you want to know about the game's features, how each file works, and how I built the game + potential future plans.

# Game Features/Structures

-Python.

-Dictionary, Event Tracking.

-File I/O, JSON.

-Array.

-Randomization.

-Conditional Logic.

-Function Calling

-Modularity, Maintainability, Scalability.

-Text Rendering, UI.

-Game State Management.

-User Input Handling, Error Checking.

-Conditional Events.

-Player Choice Impact. 

-Game World Navigation.

-Project Management

-Git Version Control

# Code Breakdown

main.py: This file handles the game's flow by setting up the story to track events. It allows players to either load a saved game or start a new one, then enters a loop where they can explore rooms, interact with objects, and make choices. Players can save their progress at any time, and the game continues until a specific story goal is completed.

Modules_Rooms.py: This file contains the primary structure for the game’s rooms, where the player navigates. It also contains functions for each room's unique functionalities. It defines each room with attributes like name, interactable objects, and exits. It also tracks event occurrence within a room, which influences future interactions and story progression. The player can interact with objects in the room, move between rooms, and trigger story events.

Modules_Story.py: This file contains functions that print important narration sections in the game. It defines static functions that are called in Main or Modules_Rooms that give the player new story based information.

utils.py: This file contains helper functions with various functionalities which includes text rendering, save/load game, error checking, and randomly generating certain game features.

# Creator's thoughts

This game is part 1 of the story, which I may or may not finish. Part 2 would be a game to navigate to the airport; I would want to have a totally different type of gameplay to practice new skills for this part like driving a car around the city. Part 3 would be navigating to the resort in Mexico; I have not decided what unique gameplay mechanic I could use for this. 

I created this game as a project mainly to familiarize myself with Python. The next steps for the current game (part 1) is to host the game on a website; I would use Django for this. Then I can add a GUI to make it feel like a proper game. This would be great front-end practice.

# Hints

The ">" expects you to press enter.

For other inputs, type a number like '1', or a character like 'y', then press enter to choose that option.

You can only navigate to a room that you are currently next to.

To complete the game, you need to pack the suitcase, obtain the car keys, and buy a plane ticket. When you have done all of these, you should prepare the car in the garage. Keep exploring the house to complete the necessary tasks. There are certain things that need to be discovered or unlocked.

If you see "all flights are too expensive", keep trying, as a new flight is randomly generated each time you access the pc. Eventually, you should find a ticket that is affordable.