# Написать функцию, являющуюся аналогом cat

def cat(file):
    try:
        with open(file) as file:
            for line in file:
                print(line, end='')
            print()
        file.close()
    except FileNotFoundError:
        print('Такого файла не существует')


if __name__ == '__main__':
    cat(input('Введите название файла: '))
