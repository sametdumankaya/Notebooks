import sys


# read test field's size and input values (x-y coordinates, initial orientation and exploration path) for each robot
# from command line arguments
test_field_rows = int(sys.argv[1])
test_field_columns = int(sys.argv[2])


# for each robot, we should print out the last x-y coordinate and orientation
for i in range(3, len(sys.argv), 4):
    x = int(sys.argv[i])
    y = int(sys.argv[i+1])
    orientation = sys.argv[i+2]
    path = sys.argv[i+3]

    # for each char in current robot's path, we should update the orientation if it's "L" or "R" and if it's "M" then
    # we should update the position of that robot.
    for char in path:
        if char == "R":
            if orientation == "N":
                orientation = "E"
            elif orientation == "E":
                orientation = "S"
            elif orientation == "S":
                orientation = "W"
            else:
                orientation = "N"
        elif char == "L":
            if orientation == "N":
                orientation = "W"
            elif orientation == "W":
                orientation = "S"
            elif orientation == "S":
                orientation = "E"
            else:
                orientation = "N"
        else:
            # There are extra checks for the limits of the test field. If any robot tries to move outside the test field
            # we should not update its position, for instance a robot may try to move with orientation "N" when it has
            # x-y coordinates of (9, 9) and if the field size is 10-10, we should not move it because it will
            # move outside of the field.
            if orientation == "N":
                y = y + 1 if y < test_field_rows - 1 else test_field_rows - 1
            elif orientation == "E":
                x = x + 1 if x < test_field_columns - 1 else test_field_columns - 1
            elif orientation == "S":
                y = y - 1 if y > 0 else 0
            else:
                x = x - 1 if x > 0 else 0
    # lastly, print each robot's x-y coordinates and its last orientation
    print(f"{x} {y} {orientation}")




