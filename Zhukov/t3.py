
# Придумайте как минимум 2 способа нахождения
# количества цифр в числе. Один из них не
# должен использовать строки, а основываться
# только на математических операторах и
# других конструкциях языка.

def first_counter(n):
    lengh = len(n) - n.count(".") - n.count("-") - n.count(",")
    return lengh

def second_counter(n):
    num = abs(int(n.replace('.', '')))
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

def main():
    print('Введите число:')
    n = input()
    print('1)Колличество цифр в введеном числе с помощью функции len: ',
          first_counter(n))
    print('2)Колличество цифр в введеном числе с помощью деления: ',
          second_counter(n))
    
if __name__ == '__main__':
  main()
