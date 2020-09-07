def hello(count):

    if count == 0:
        return

    hello(count)

    print('Hello world! ', count)
    count -= 1


hello(5)