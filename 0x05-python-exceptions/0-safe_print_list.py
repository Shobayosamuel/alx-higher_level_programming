#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for u in my_list:
        num += 1
    if x > num:
        x = num
    else:
        x = x
    try:
        for elem in range(x):
            print("{:d}".format(my_list[elem]), end="")
        print("\n")
    except ValueError:
        print("x is invalid")
    return x
