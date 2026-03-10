#!/usr/bin/env python3
"""Send POST requests to the Flask level API, cycling level 0–100 with time between updates."""
import time
import requests

API_URL = "http://127.0.0.1:5000/"
UPDATE_PERIOD_S = 1 # seconds between each POST
LEVEL_MAX = 75
LEVEL_MIN = 25
DELTA = 1
MODE = 'fill' # can be either 'fill' or 'drain'


def validate_range(value,min,max):
    """Validator for min-max range."""
    num = int(value)
    if num <= min:
        num = min
    elif num >= max:
        num = max
    return num


def main():
    print(f"POSTing level to {API_URL} every {UPDATE_PERIOD_S} s ({LEVEL_MIN}–{LEVEL_MAX}). Ctrl+C to stop.")
    print(f"fill URL = {API_URL}fill")
    print(f"drain URL = {API_URL}drain")

    # start off at minimum, set the level
    level = LEVEL_MIN
    MODE = 'fill'
    try:
        resp = requests.post(API_URL+'level', json={'level': level}, timeout=2)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"POST failed: {e}")


    # loop until ctrl-c
    while True:      
        try:
            resp = requests.post(API_URL+MODE, json={'delta_level': DELTA}, timeout=2)
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"POST failed: {e}")
        
        if (MODE == 'fill'):
            level = validate_range(level+DELTA,LEVEL_MIN,LEVEL_MAX)
            if (level >= LEVEL_MAX):
                # time to switch directions
                MODE = 'drain'
        else:
            level = validate_range(level-DELTA,LEVEL_MIN,LEVEL_MAX)
            if (level <= LEVEL_MIN):
                # time to switch directions
                MODE = 'fill'   
        
        # sleep
        time.sleep(UPDATE_PERIOD_S)


if __name__ == "__main__":
    main()
