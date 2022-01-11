def digitCounter(x):
    x = abs(float(x))
    c = 0
    while int(x) != x:
        x *= 10
    while x > 0:
        x = x // 10
        c += 1
    return c

def main():
    print('введите число:')
    print('колличество цифр - ', digitCounter(input()))

if __name__ == '__main__':
  main()
