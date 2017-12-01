from gpiozero import LEDBoard
from gpiozero.tools import random_values

from helper import is_december, is_between_christmas_eve_and_new_year


class Tree:
    def __init__(self):
        self.leds = LEDBoard(4, 15, 13, 21, 22, 6, 12, 25, 16, 17, 27, 26, 9, 23, 11, 5, 20, 19, 14, 18, 7, 8, 10, 24, 2,
                             pwm=True)

    def reset(self):
        print("turn all leds off")
        for led in self.leds:
            led.off()

    def party_mode(self):
        for led in self.leds:
            led.source_delay = 0.1
            led.source = random_values()

    def light_leds(self, date):
        for index in range(0, date.day):
            print("turn on LED %d" % index)
            self.leds[index].on()

    def tick(self, date):
        if not is_december(date):
            print("reset LEDs, because advent season is over")
            self.reset()
        elif is_between_christmas_eve_and_new_year(date):
            print("It's christmas time!!")
            self.party_mode()
        else:
            print("Light appropriate LEDs")
            self.light_leds(date)
