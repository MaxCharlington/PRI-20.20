# Написать функцию, определяющую максимальную длину слова в файле

def max_l(file):
    try:
        with open(file) as file:
            words = file.read().split(' ')
            file.close()
            sorted_words = sorted(words, key=len, reverse=True)
            print(f'Максимальная длина слова в файле: {len(sorted_words[0])}')
    except FileNotFoundError:
        print('Такого файла не существует')


if __name__ == '__main__':
    max_l(input('Введите название файла: '))
