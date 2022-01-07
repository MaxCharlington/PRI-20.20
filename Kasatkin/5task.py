def cat(f_name):
    try:
        with open(f_name) as f_file:
            for line in f_file:
                print(line, end='')
            print()
    except FileNotFoundError:
        print('Нет файла') 

def main():
    print('Введите название файла: ')
    file_name = input()
    cat(file_name)

if __name__ == '__main__':
  main()
