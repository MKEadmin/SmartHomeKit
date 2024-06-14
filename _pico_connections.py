"""
                        ---usb---
                GP00 1  |o     o| -1  VBUS 
                GP01 2  |o     o| -2  VSYS
                GND  3  |o     o| -3  GND 
                GP02 4  |o     o| -4  3V3_EN    - DO NOT USE
                GP03 5  |o     o| -5  3V3(OUT)
                GP04 6  |o     o| -6           ADC_VREF
                GP05 7  |o     o| -7  GP28     ADC2
                GND  8  |o     o| -8  GND      AGND
                GP06 9  |o     o| -9  GP27     ADC1
                GP07 10 |o     o| -10 GP26     ADC0
                GP08 11 |o     o| -11 RUN
                GP09 12 |o     o| -12 GP22
                GND  13 |o     o| -13 GND
                GP10 14 |o     o| -14 GP21
                GP11 15 |o     o| -15 GP20
                GP12 16 |o     o| -16 GP19
                GP13 17 |o     o| -17 GP18
                GND  18 |o     o| -18 GND
                GP14 19 |o     o| -19 GP17
 SOILHUMIDITY ->GP15 20 |o     o| -20 GP16
                        ---------
"""

class Pico:
    PIN_SOILHUMIDITY = 15   # GP 15
    
    
    
    