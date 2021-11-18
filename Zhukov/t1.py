
# Написать программу, принимающую пользовательский ввод — год,
# при помощи функции input(), и печатающая True,
# если год високосный, и False если нет.

def main():
  try:
    year = int(input())
    print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
  except ValueError:
    print('\033[31m', 'Некорректный ввод')

if __name__ == '__main__':
  main()