#!/usr/bin/python3

# if __name__ == "__main__":
#     """Print the number of and list of arguments."""
#     import sys

#     count = len(sys.argv) - 1
#     if count == 0:
#         print("0 arguments.")
#     elif count == 1:
#         print("1 argument:")
#     else:
#         print("{} arguments:".format(count))
#     for i in range(count):
#         print("{}: {}".format(i + 1, sys.argv[i + 1]))
import sys
number = len(sys.argv)
if number == 0:
    print("0 argument")
elif number == 1:
    print("1 argument")
    print("{}: {}".format(number, sys.argv[0]))
else:
    print("{} arguments".format(number))
    for x in range(number):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
