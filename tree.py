from gpiozero import LEDBoard
from gpiozero.tools import random_values

from helper import is_december, is_christmas


class Tree:
    def __init__(self):
        self.leds = LEDBoard(*range(2,28),pwm=True)

    def reset(self):
        print("turn all leds off")
        for led in self.leds:
            led.off()

    def party_mode(self):
        for led in self.leds:
            led.source_delay = 0.1
            led.source = random_values()

    def handle_date(self, date):
        if not is_december(date):
            print("reset LEDs, because advent season is over")
            self.reset()
        elif is_christmas(date):
            print("It's christmas time!!")
            self.party_mode()
        else:
            for index in range(0,date.day):
                print("turn on LED %d" % index)
                self.leds[index].on()
