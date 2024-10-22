# importing modules
import pyfirmata
from time import sleep

# connecting to COM5 port
board = pyfirmata.Arduino('COM5')

# starting iterator
it = pyfirmata.util.Iterator(board)
it.start()

# connecting to pin 5 of arduino uno
servo = board.get_pin('d:9:s')

# declaring wasteType variable
wasteType = 0

# turn recycle list text fille into array
f = open('recycle.txt', 'r')
recycle = f.read()
recycleList = recycle.split(",")

# arduino servo function
def motor(object):

    # assign waste type based on whether or not the detected object is in the list of recyclable objects
    if object in recycleList:
        wasteType = 1
    else:
        wasteType = 2

    # if waste is recyclable
    if wasteType == 1:

        # rotate flap towards recycling bin
        for x in range(0, 45, 2):
            servo.write(x)
            sleep(0.002)

        # return flap to original position
        for x in range(90, 135, 2):
            servo.write(x)
            sleep(0.002)

    # if waste is not recyclable
    elif wasteType == 2:

        # rotate flap towards garbage bin
        for x in range(90, 135, 2):
            servo.write(x)
            sleep(0.002)

        # return flap to original position
        for x in range(0, 45, 2):
            servo.write(x)
            sleep(0.002)

    # exit arduino board
    board.exit()