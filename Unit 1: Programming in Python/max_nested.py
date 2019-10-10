def f(x):
    if int(x) == x:
        if x % 2 == 0:
            if x % 3 == 0:
                return "{} is an divisible by 6".format(x)
            else:
                return "{} is even".format(x)
        else:
            return "{} is an odd number".format(x)
    else:
        return "{} isn't an int".format(x)
