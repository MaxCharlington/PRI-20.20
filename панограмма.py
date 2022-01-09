from string import ascii_lowercase as alphabet

def is_pangram(s):
    ru_alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    if set(alphabet) - set(s.lower()) == set([]) or ru_alphabet - set(s.lower()) == set([]):
        print("Данная строка является панграммой")
    else:
        print("Данная строка панграммой не является")

def main():
    test1 = 'Съешь же ещё этих мягких французских булок да выпей чаю' #панграмма на кириллице
    print(test1)
    is_pangram(test1) 
    test2 = 'Съешь ещё этих мягких французских булок да выпей чаю' #та же строка без буквы ж
    print(test2)
    is_pangram(test2)   
    test3 = 'The quick brown fox jumps over the lazy dog' #панграмма на латинице
    print(test3)
    is_pangram(test3) 
    test4 = 'The quick brown fox jumps over the laxy dog' #та же строка без буквы z
    print(test4)
    is_pangram(test4) 
    test5 = input("Введите строку:") #йцукеёнгшщзхъфывапролджэячсмитьбю - например эту 
    is_pangram(test5)

if __name__ == '__main__':
    main()
