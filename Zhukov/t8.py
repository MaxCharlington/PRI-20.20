
# Написать функцию проверки числа на совершенность:
# совершенное число — это положительное целое число, равное сумме его собственных
# положительных делителей, то есть сумме его положительных делителей, исключая само число

def is_perfect(n):
    count = 1
    for i in range(2,n // 2 + 1):
        if n % i == 0:
            count += i
        return count != n

def main():
    print('Введите число: ')
    number = int(input())
    if(is_perfect(number)):
        print(str(number), ' - совершенное число')
    else:
        print(str(number),' - несовершенное число')

if __name__ == '__main__':
  main()
