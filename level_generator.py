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
    if x == 0:
        for y in range(width):
            text_file.write("0")
    elif (x == 5):
        for y in range(width):
            if y == 0:
                text_file.write("P")
            else:
                text_file.write("0")
    elif (x % 6) == 0:
        zero_spot = random.randrange(0, width)
        for y in range(width):
            if y == zero_spot:
                text_file.write("0")
            else:
                text_file.write("1")
    else:
        for y in range(width):
            text_file.write("0")
    text_file.write("\n")
text_file.close()
