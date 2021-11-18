
# Напсать функцию, которая будет определять максимальную длину слова в файле

def word_length(f_name):
    try:
        with open(f_name) as f_file:
            list_word = f_file.read().split(' ')
            f_file.close()
            word = sorted(list_word, key=len, reverse=True)[0]
            max_len = len(sorted(list_word, key = len, reverse = True)[0])
            print("\033[34m", 'Максимальная длина слова = ',
                max_len, '\n', 'Это слово - ', word, sep='')
    except FileNotFoundError:
        print('\033[31m', 'Такого файла не существует')


def main():
    print('Введите наименование файла и его расширение: ')
    file_name = input()
    word_length(file_name)

if __name__ == '__main__':
  main()
