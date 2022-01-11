def leap(year):
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        return 'yes'
    else:
        return 'no'

def main():
    print('Введите год: ')
    print(leap(int(input())))

if __name__ == '__main__':
  main()
