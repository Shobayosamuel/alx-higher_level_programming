def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()
