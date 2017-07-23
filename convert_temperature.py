def cube(number):
    sum = number ** 2
    return sum

def multiply(number1, number2):
    sum = number1 * number2
    return sum
## codes above are from functions activities


def c_to_f(c_temp):
    return c_temp * 9 / 5 + 32

def f_to_c(f_temp):
    return (f_temp - 32) * 5 / 9

test1 = f_to_c(72)
test2 = c_to_f(37)

print('72 degrees F = {} degrees C'.format(test1))
print('37 degrees C = {} degrees F'.format(test2))
