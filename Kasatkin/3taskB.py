def stringCounter(s):
    return len(s) - s.count(".") - s.count("-")

def main():
    print('введите число:')
    print('колличество цифр - ', stringCounter(input()))

if __name__ == '__main__':
  main()
