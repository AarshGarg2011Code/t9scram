import json

def loadkeypad(filename: str = "keypad.json"):
    with open(filename, "r") as file: keypad = json.load(file)
    keypad = {int(k): v for k, v in keypad.items()}
    return keypad

def loadkeys(filename: str = "keys.json"):
    with open(filename, "r") as file: keys = json.load(file)
    return keys
