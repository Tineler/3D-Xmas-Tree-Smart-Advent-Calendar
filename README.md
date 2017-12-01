# 3D-Xmas-Tree-Smart-Advent-Calendar
A smart advent calendar written in Python 3 for PiHut's 3D Xmas Tree for Raspberry Pi

## Setup
1. Prepare an SD card for your raspberry pi. I suggest using an headless setup:
- Create SD card as described here: https://www.raspberrypi.org/documentation/installation/installing-images/
- Creating empty file called "ssh" in boot partition
- Creating file "wpa_supplicant.conf" with respective settings in boot partition.
- Login via ssh and change pi's password!
2. Build and attach the 3D Xmas Tree according to the instructions: https://thepihut.com/blogs/raspberry-pi-tutorials/3d-xmas-tree-for-raspberry-pi-assembly-instructions
2. Install GPIO Zero: `sudo apt-get install python-gpiozero python3-gpiozero`
3. Checkout this repository
4. Go into src folder and run `python3 main.py`

### Testing
There is some kind of test script (test.py) which simulates all days in december. This way you can test if 1. your tree is working and 2. if the script itself is working.
