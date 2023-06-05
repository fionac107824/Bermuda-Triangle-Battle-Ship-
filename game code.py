from adafruit_crickit import crickit
from adafruit_motor import stepper
from adafruit_circuitplayground import cp
import time



def wave_hello():
    print("Attacked!")

def custom_hello(name):
    print("Attacked" + name)



name_list = []

for person in name_list:
    custom_hello(person)

tap_count = 0
while tap_count < 3:
    if cp.tapped:
        tap_count += 1
print("Reached 3 single-taps!")
tap_count = 0
cp.detect_taps = 3

while tap_count < 2:
    if cp.tapped:
        wave_hello(Attacked)
        tap_count += 1
        time.sleep(0.8)
print("Reached 3 double-taps!")
print("Done.")

while True:
    if cp.button_a:
        wave_hello(Attacked)
        time.sleep(0.5)

