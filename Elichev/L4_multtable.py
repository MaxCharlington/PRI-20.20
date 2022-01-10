# Написать программу, которая выводит таблицу умножения

def multiplication_table():
    for i in range(1, 10):
        for j in range(i, i*10, i):
            print(j, end='\t')
        print()


if __name__ == '__main__':
    multiplication_table()
