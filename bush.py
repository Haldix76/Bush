# ====== Bush 2 ======

import time
import os
import subprocess
import socket

COMMAND_LIST = ["hello", "version", "help", "exit", "time", "ls", "pwd", "color", "clear", "fastfetch", "start", "getip"]

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
| ____            _       ____  |
|| __ ) _   _ ___| |__   |___ \ |
||  _ \| | | / __| '_ \    __) ||
|| |_) | |_| \__ \ | | |  / __/ |
||____/ \__,_|___/_| |_| |_____||
+-------------------------------+
"""

def Boot():
    print("\n--- STARTING BUSH ---\n")

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

    print("\nWelcome to Bush 2!\n")

#Boot() # Comment this line to disable boot

def HelloCommand():
    print("Hello, User!")

def VersionCommand():
    print("bush 2")

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

def ClearCommand():
    subprocess.run("clear", shell=True)

def FastfetchCommand():
    try:
        subprocess.run("fastfetch")
    except Exception as e:
        print("bush: error while running fastfetch, please check if fastfetch is installed on your computer")

def StartCommand():
    program = str(input("bush: enter the program name ").lower())
    try:
        subprocess.run(program)
    except Exception as e:
        print(f"bush: cannot run {program}")

def GetIpCommand():
    hostname = socket.gethostname()
    ipAddress = socket.gethostbyname(hostname)

    print("-- Network information --\n")
    print(f"Hostname: {hostname}\nIP Adress: {ipAddress}")

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
            case "clear":
                ClearCommand()
            case "fastfetch":
                FastfetchCommand()
            case "start":
                StartCommand()
            case "getip":
                GetIpCommand()
            case _:
                print(f"bush: Unknown command {command}")
    except KeyboardInterrupt:
        print("bush: process interrupted, goodbye.")
        break