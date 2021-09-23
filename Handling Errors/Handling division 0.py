x = 10
y = 0


#  sayin I want 0 instead
def division_x_y(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 0


def division_x_y_2(x, y):
    return x / y if y != 0 else 0


print(division_x_y(x, y))
print(division_x_y_2(x, y))
