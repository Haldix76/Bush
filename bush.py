# ====== Bush 3 ======

import time
import os

COMMAND_LIST = ["hello", "version", "help", "exit", "time", "ls", "pwd", "color"]

COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "pink": "\033[35m",
    "white": "\033[37m"
}
CURRENT_COLOR = "\033[37m"

ASCII_ART = r"""
+-------------------------------+
| ____            _       _____ |
|| __ ) _   _ ___| |__   |___ / |
||  _ \| | | / __| '_ \    |_ \ |
|| |_) | |_| \__ \ | | |  ___) ||
||____/ \__,_|___/_| |_| |____/ |
+-------------------------------+
"""

def Boot():
    print("\n--- STARTING BUSH 3 ---\n")

    print("Loading packages...")
    time.sleep(1.5)

    print("Loaded 143 packages")
    time.sleep(1)

    print("Initialising user environment...")
    time.sleep(1.5)

    print("User environment ready")
    time.sleep(1)

    print("Switching to protected mode...")
    time.sleep(1)

    print("\nEverything is ready.\n")
    time.sleep(1)

    print(ASCII_ART)

    print("\nWelcome to Bush 3!\n")

Boot()

def HelloCommand():
    print("Hello, User!")

def VersionCommand():
    print("bush version: 3")

def HelpCommand():
    print("bush: available commands: ")
    for i in COMMAND_LIST:
        print("-", i)

def TimeCommand():
    print(time.strftime("%H:%M:%S"))

def PwdCommand():
    print(os.getcwd())

def LsCommand():
    for file in os.listdir():
        print(file)

def ColorCommand():
    global CURRENT_COLOR

    selectedColor = input("bush: Please select the color: ").lower()

    if selectedColor in COLORS:
        CURRENT_COLOR = COLORS[selectedColor]
        print(f"bush: color changed to {selectedColor}")
    else:
        print("bush: color not supported")

while True:
    try:
        command = str(input(CURRENT_COLOR + "bush> ").lower())
        match command:
            case "hello":
                HelloCommand()
            case "version":
                VersionCommand()
            case "help":
                HelpCommand()
            case "exit":
                print("bush: shutting down")
                break
            case "time":
                TimeCommand()
            case "pwd":
                PwdCommand()
            case "ls":
                LsCommand()
            case "color":
                ColorCommand()
            case _:
                print(f"bush: Unknown command {command}")
    except KeyboardInterrupt:
        print("bush: process interrupted, goodbye.")
        break