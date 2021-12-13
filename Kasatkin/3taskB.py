def stringCounter(s):
    return len(s) - s.count(".") - s.count("-")

def main():
    print('введите число:')
    print('колличество цифр - ', stringCounter(input()))

main()