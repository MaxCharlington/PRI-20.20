
#Написать аналог функции cat

def cat(f_name):
    try:
        with open(f_name) as f_file:
            for line in f_file:
                print("\033[34m", line, end='')
            print()
        f_file.close()
    except FileNotFoundError:
        print('\033[31m', 'Такого файла не существует')
 

def main():
    print('Введите наименование файла и его расширение: ')
    file_name = input()
    cat(file_name)

if __name__ == '__main__':
  main()
