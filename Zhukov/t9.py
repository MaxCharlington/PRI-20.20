
# Напишите функцию Python, чтобы проверить, является ли строка панграммой
# Примечание. Панограммы — это слова или предложения, содержащие каждую букву алфавита хотя бы один раз.
# Например: «Быстрая коричневая лиса перепрыгивает через ленивую собаку»
#
# Экс-граф? Плюш изъят. Бьём чуждый цен хвощ!
# Любя, съешь щипцы, — вздохнёт мэр, — кайф жгуч.

def is_pangram(string):
    return set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') - set(string.lower())
    

def main():
    print('Введите строку: ','\n')
    s = input()
    if(is_pangram(s)):
        print('\n', 'Введеная строкая не является панграммой')
    else:
        print('\n','Введеная строкая является панграммой')

if __name__ == '__main__':
  main()
