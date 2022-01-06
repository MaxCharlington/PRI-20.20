# Написать программу, выводящую первые n строк треугольника Паскаля

def pascal_triangle(n):
    row = [1]
    for i in range(n):
        print(row)
        row = [sum(j) for j in zip([0]+row, row+[0])]


if __name__ == '__main__':
    pascal_triangle(int(input('Введите число выводимых строк: ')))
