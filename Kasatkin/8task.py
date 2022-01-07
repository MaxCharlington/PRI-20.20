def isPerfect(n):
    count = 0
    for i in range(1,n // 2 + 1):
        if n % i == 0:
            count += i
    return count == n

def main():
    print('Введите число: ')
    n = int(input())
    if(isPerfect(n)):
        print('Число совершенное')
    else:
        print('Число несовершенное')

if __name__ == '__main__':
  main()
