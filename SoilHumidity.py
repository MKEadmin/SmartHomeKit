import sys
if sys.platform != 'rp2': # raspian pico
    print(40 * "-")
    print(">>>>>> Demo for Respberry Pi Pico <<<<<<")
    print(40 * "-")
    quit()
    
from machine import Pin

def getValue():
    return 42

if __name__ == "__main__":
    print(getValue())
    