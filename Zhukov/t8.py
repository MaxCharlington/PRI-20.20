
# Написать функцию проверки числа на совершенность:
# совершенное число — это положительное целое число, равное сумме его собственных
# положительных делителей, то есть сумме его положительных делителей, исключая само число

def is_perfect(n):
    count = 1
    for i in range(2,n // 2 + 1):
        if n % i == 0:
            count += i
    if count == n:
        return(1)
    else:
        return(0)

def main():
    print('Введите число: ')
    number = int(input())
    if(is_perfect(number) == 1):
        print(str(number) + ' - совершенное число')
    else:
        print(str(number) + ' - несовершенное число')

if __name__ == '__main__':
  main()
