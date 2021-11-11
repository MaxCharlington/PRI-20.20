
# написать функции:
# get_max
# get_min
# get_mid
# get_med без сортировки
# get_metrics
# для сортированных массивов

def get_max(num_array):
    max_value = None
    for n in num_array:
        if (max_value is None or n > max_value):
            max_value = n
    return(max_value)

def get_min(num_array):
    min_value = None
    for n in num_array:
        if (min_value is None or n < min_value):
            min_value = n
    return(min_value)

def get_mid(num_array):
    mid_value = int(len(num_array) / 2)
    return(num_array[mid_value - 1])

def get_med(num_array):
    med_value = int(len(num_array) // 2)
    return(num_array[med_value - 1] + num_array[med_value]) / 2

def get_met(num_array):
    count = 0
    for n in num_array:
        if (n % 2 != 0):
            count += 1
    return(count)


def main():
    numbers = [167,108,99,87,79,65,43,23,13,5,1,0]
    print('Массив: ', end='')
    for n in numbers:
        print(str(n) + ' ', end='')
    print('')
    print('get_max: ' + str(get_max(numbers)))
    print('get_min: ' + str(get_min(numbers)))
    print('get_mid: ' + str(get_mid(numbers)))
    print('get_med: ' + str(get_med(numbers)))
    print('get_metrics_amount_of_odd_numbers: ' + str(get_met(numbers)))


if __name__ == '__main__':
  main()
