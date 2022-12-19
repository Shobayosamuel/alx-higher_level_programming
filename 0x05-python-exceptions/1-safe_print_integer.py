
def safe_print_integer(value):
    try:
        li = []
        li1 = ["a", "b", "c", "d", "e", "f", 'g', "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        li2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for i in range(len(value)):
            li.append(value[i])
        if (li[0] in li1) or (li[0] in li2):
            return False


    except ValueError:
        print("{:d}".format(value))
        return True
