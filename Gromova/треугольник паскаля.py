def pascal_triangle():
    num = int(input("Введите кол-во строк треугольника Паскаля: "))
    triangle = ['1']
    print(triangle[0])
    for i in range(num - 1):
        triangle_1 = triangle.copy()
        triangle.clear()
        triangle = [str(int(triangle_1[j]) + int(triangle_1[j + 1])) for j in range(len(triangle_1) - 1)]
        triangle.insert(0, '1')
        triangle.append('1')
        print('\t'.join(triangle))

def main():
    pascal_triangle()

if __name__ == '__main__':
	main()