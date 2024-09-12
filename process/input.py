from io import FileIO
import keyboard
import json

keys = {
    "right":False,
    "left":False,
    "up":False,
    "down":False
}

def set_key(key: str, value: bool):
    keys[key] = value

def del_key(key: str) -> bool:
    return keys.pop(key)

def get_key(key: str) -> bool:
    return keys.get(key, None)

def upload_keys(file: FileIO):
    global keys
    keys = dict(zip(json.load(file).keys(), [False for i in range(len(json.load(file)))]))

keyboard.add_hotkey("right", set_key, args=('right', True))
keyboard.add_hotkey("right", set_key, args=('right', False), trigger_on_release=True)