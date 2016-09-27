def adder(number_one, number_two, message="no message passed", happy=True):
    print(message)
    print(happy)
    return number_one + number_two

print(adder(9, 4, message="do math son", happy=False))

print(adder("joel", " likes programming!"))


def add(*args):
    print(args)
    return sum(args)

print(add(1, 200, 3, 4, 5, 6))

print(adder(*[9, 4]))

print(add(*range(100)))

# key word arguements will always error on you.


def beginners_luck(*args, **kwargs):
    print(args)
    print(kwargs)
    return 1

print(beginners_luck("joel", 12312341235, [1, 2, 3], birthday="today", lol="joel"))
