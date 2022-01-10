def is_perfect(num):
	sum = 0
	for i in range(1, num//2 + 1):
		if num % i == 0:
			sum += i
	print(f'Число {num} совершенно?', sum == num)
        
#Совершенные числа: 6, 496, 8128, 33550336 (долго считает)
def main():
	is_perfect(6)
	is_perfect(5)
	is_perfect(14)
	is_perfect(496)
	is_perfect(8128)

if __name__ == '__main__':
	main()