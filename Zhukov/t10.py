
# Напишите функцию Python, которая печатает первые n строк треугольника Паскаля.
# Примечание. Треугольник Паскаля — это арифметическая и геометрическая фигура,
# впервые представленная Блезом Паскалем.

def pascal(N):
    strings_array = []
    for i in range(N):
        string = [1] * (i+1)
        for j in range(1,i):
                 string[j] = strings_array[i-1][j-1] + strings_array[i-1][j]
        strings_array.append(string)
    for k in strings_array:
        print(k)

def main():
    print('Введите число строк: ')
    pascal(int(input()))

if __name__ == '__main__':
  main()
