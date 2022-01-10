# THE NUMBERS, MASON! WHAT DO THEY MEAN?!
# Придумать 2 способа нахождения количества цифр в числе,
# при этом только один из них может использовать строки.

def string_counter(n):
    return len(n.replace('.', ''))


def math_counter(n):
    n = abs(int(n.replace('.', '')))
    k = 0
    while n > 0:
        n //= 10
        k += 1
    return k


if __name__ == '__main__':
    name = input()
    print(string_counter(name))
    print(math_counter(name))
