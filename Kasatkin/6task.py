def wordLen(f_name):
    try:
        with open(f_name) as f_file:
            wordList = f_file.read().split()
            wordList.sort(key=len)
            word = wordList[-1]
            maxLen = len(word)
            return [word, maxLen]
    except FileNotFoundError:
        print('Такого файла не существует')

def main():
    print('Введите наименование файла и его расширение: ')
    word, maxLen = wordLen(input())
    print('Самое длинное слово ', word, 'и его длина', maxLen)

if __name__ == '__main__':
    main()
