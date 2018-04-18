import random
text_file = open("level_random.game", "w")
width = 10
floors = 10

'''
Need to do:
-Add walls to the sides
-Make the holes wider

'''

for x in range(floors * 10):
    text_file.write("1")
    if x == 0:
        for y in range(1, width - 1):
            text_file.write("0")
    elif (x == 5):
        for y in range(1, width - 1):
            if y == 1:
                text_file.write("P")
            else:
                text_file.write("0")
    elif (x % 6) == 0:
        zero_spot = random.randrange(1, width - 1)
        zero_spot_two = zero_spot + 1
        if zero_spot == 1:
            zero_spot_two = 2
        elif zero_spot == (width - 1):
            zero_spot_two = width - 2
        elif zero_spot == (width - 2):
            zero_spot_two = width - 3
        for y in range(1, width - 1):
            if y == zero_spot:
                text_file.write("0")
            elif y == zero_spot_two:
                text_file.write("0")
            else:
                text_file.write("1")
    else:
        for y in range(1, width - 1):
            text_file.write("0")
    text_file.write("1")
    text_file.write("\n")
for y in range(width):
    text_file.write("E")
text_file.close()
