"""
def set_key(key: str):
    if keys[key]:
        keys[key] = False
    else:
        keys[key] = True

def del_key(key: str) -> bool:
    return keys.pop(key)

def get_value(key: str) -> bool:
    return keys.get(key, None)

for key in keys.keys():
    keyboard.add_hotkey(key, set_key, args=(key,))"""
import sys
from threading import Thread
from pynput import keyboard

keys = {
    "right":False,
    "left":False,
    "up":False,
    "down":False,
    "esc":False
}
listener = None

def on_press(key):
    if key == keyboard.Key.right:
        keys["right"] = True
    if key == keyboard.Key.left:
        keys["left"] = True
    if key == keyboard.Key.up:
        keys["up"] = True
    if key == keyboard.Key.down:
        keys["down"] = True
    if key == keyboard.Key.esc:
        keys["esc"] = True

def on_release(key):
    global listener
    if key == keyboard.Key.right:
        keys["right"] = False
    if key == keyboard.Key.left:
        keys["left"] = False
    if key == keyboard.Key.up:
        keys["up"] = False
    if key == keyboard.Key.down:
        keys["down"] = False
    if key == keyboard.Key.esc:
        keys["esc"] = False
        listener.stop()
        #sys.exit()

def listen():
    global listener
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

thd = Thread(target=listen)
thd.start()