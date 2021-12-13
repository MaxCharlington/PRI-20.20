def bank(time, summ, percent):
    percent = 1 + percent / 100
    for i in range(time):
       summ *= percent
    return summ

def main():
    print('Введите время вклада, сумму и процент: ')
    print(bank(int(input()), int(input()), float(input())))

main()
