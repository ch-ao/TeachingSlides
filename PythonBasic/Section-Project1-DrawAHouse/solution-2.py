# Step 1. Print the roof 
# i: 1    3    5   7   9   11  13  15
# j: 15   13  11   9   7   5   3    1
def print_the_roof():
    i = 1 # set the # of *
    while True:
        for x in range(15-i):
            print (" ", end = '')
        for y in range(i):
            print ("*", end = ' ')
        print (" ")
        i = i + 2
        if (i > 15):
            break

# Step 2: Print start * and end *
def print_start_end():
    print ("*", end='')
    for x in range(27):
        print (" ", end='')
    print ("*")

# Step 3: Print the window
def print_5_stars():
    print ('*  ', end='')
    for x in range(5):
        print ('*', end=' ')
    for x in range(15):
        print(' ', end='')
    print('*')

def print_3_stars():
    print ('*  ', end='')
    for x in range(3):
        print ('*  ', end=' ')
    for x in range(13):
        print(' ', end='')
    print('*')

def print_the_window():
    print_5_stars()
    print_3_stars()
    print_5_stars()
    print_3_stars()
    print_5_stars()

# Step 4: Print the door
def print_the_door():
    for x in range(3):
        print ('*', end='')
        for y in range(19):
            print (' ', end='')
        print("* * *   *")

# Step 5: Finish the house
def finish_the_house():
    for x in range(15):
        print('* ',end='')
    print('')

# Main Function
if __name__ == "__main__":
    print_the_roof()
    print_start_end()
    print_the_window()
    print_the_door()
    finish_the_house()
