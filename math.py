def summ(value_1, value_2, value_3=0):
    return value_1 + value_2 + value_3


def multiply(value_1, value_2):
    return value_1 * value_2


x = 1
y = 2
z = 3
print(x, "+", y, "+", z, "=", summ(x, y, z))
x = 5
y = 7
mult = 2
print("(", x, "+", y, ") *", mult, "=", multiply(summ(x, y), mult))
