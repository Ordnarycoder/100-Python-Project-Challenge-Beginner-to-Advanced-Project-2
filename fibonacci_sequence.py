def fibonacci_sequence():
    times = int(input("How many times to repeat fibonacci sequence?\n"))

    a, b = 0, 1
    i = 0

    while i < times:
        print(b)
        a, b = b, a + b
        i += 1

fibonacci_sequence()