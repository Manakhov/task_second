def summ(value_1, value_2):
    return value_1 + value_2


def multiply(value_1, value_2):
    return value_1 * value_2


x = 5
y = 7
mult = 2
print("(", x, "+", y, ") *", mult, "=", multiply(summ(x, y), mult))
