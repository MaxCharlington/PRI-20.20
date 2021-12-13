def intCounter(x):
    x = abs(int(x.replace('.', '')))
    c = 0
    while x > 0:
        x = x // 10
        c += 1
    return c

def main():
    print('введите число:')
    print('колличество цифр - ', intCounter(input()))

main()