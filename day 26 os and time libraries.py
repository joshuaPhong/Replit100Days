# os allows communication with the console
# time library allows us to pause the program for a specified length of time
import os
import time

from replit import audio


def play():
    source = audio.play_file('audio.wav')
    source.paused = False  # unpause the playback
    while True:
        # Start taking user input and doing something with it
        user_input_stop = int(input("You can exit any time by entering 1 >>> "))
        if user_input_stop == 1:
            source.paused = True
            return
        else:
            continue


while True:
    # clear the screen
    os.system("clear")
    # Show the menu
    print("🎶 \033[36mLets play some music 🎶\n")
    time.sleep(1)
    print("Press 1 to Play.")
    time.sleep(1)
    print("Press 2 to Exit.\n")
    time.sleep(1)
    print("Press anything else to see the menu again >>> ")
    # take user's input
    user_input = int(input(""))
    # check whether you should call the play() subroutine depending on user's input
    if user_input == 1:
        play()
        break
    elif user_input == 2:
        exit()
    else:
        continue
