# PRODIGY_CS_04 – Simple Keylogger

## Project Overview
This Python program records key presses and saves them to a text file (`keylog.txt`).  
It was created as **Task-04** of my **Cyber Security Internship at Prodigy InfoTech**.

The keylogger captures letters, numbers, spaces, tabs, and line breaks
while ignoring control keys (Shift, Ctrl, etc.) for a cleaner log.
Press **ESC** to stop recording.

## Features
- Logs only readable text for easy review
- Ignores noisy keys like Shift, Ctrl, or Backspace
- Saves all captured keys to a plain text file
- Starts and stops directly from the terminal

## How to Run
1. Install Python and the `pynput` library:
   ```bash
   pip install pynput
   ```
2. Save the file as `keylogger.py` in a folder of your choice.
3. Open a terminal in that folder and run:
   ```bash
   python keylogger.py
   ```
4. Type anywhere on your own computer.  
   The keys will be logged in **keylog.txt**.  
5. Press **ESC** to stop logging.

## Example
Typing:
```
Hello World
```
will produce:
```
Hello World
```
inside `keylog.txt`.

## Tech Used
- Python
- `pynput` library for capturing key events

## ⚠️ Disclaimer
This project is for **educational use only**.  
Run it **only on your own computer** with your own consent.  
Never use a keylogger on another system without permission,
as doing so may violate privacy laws.
