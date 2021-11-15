
# написать функции:
# get_max
# get_min
# get_mid
# get_med без сортировки
# get_metrics
# для сортированных массивов

def get_max(num_array):
    if num_array[0] > num_array[-1]:
        return num_array[0]
    else:
        return num_array[-1]

def get_min(num_array):
    
    if num_array[0] < num_array[-1]:
        return num_array[0]
    else:
        return num_array[-1]

def get_mid(num_array):
    mid_value = int(len(num_array) / 2)
    return num_array[mid_value - 1]

def get_med(num_array):
    med_value = int(len(num_array) // 2)
    return (num_array[med_value - 1] + num_array[med_value]) / 2

def get_met(num_array):
    max_tulpe = ('Max', get_max(num_array))
    min_tulpe = ('Min', get_min(num_array))
    mid_tulpe = ('Mid', get_mid(num_array))
    med_tulpe = ('Med', get_med(num_array))
    return max_tulpe, min_tulpe, mid_tulpe, med_tulpe


def get_max_un(num_array):
    max_value = num_array[0]
    for n in num_array:
        if (max_value is None or n > max_value):
            max_value = n
    return max_value
    
def get_min_un(num_array):
    min_value = num_array[0]
    for n in num_array:
        if (min_value is None or n < min_value):
            min_value = n
    return min_value

def get_mid_un(num_array):
    s_num_array = sorted(num_array)
    mid_value = int(len(s_num_array) / 2)
    return s_num_array[mid_value - 1]

def get_med_un(num_array):
    s_num_array = sorted(num_array)
    med_value = int(len(s_num_array) // 2)
    return (s_num_array[med_value - 1] + s_num_array[med_value]) / 2

def get_met_un(num_array):
    s_arr = sorted(num_array)
    mid_med = int(len(s_arr) // 2)
    max_tulpe = ('Max',s_arr[-1])
    min_tulpe = ('Min',s_arr[0])
    mid_tulpe = ('Mid',s_arr[mid_med-1])
    med_tulpe = ('Med',(s_arr[mid_med - 1] + s_arr[mid_med]) / 2)
    return max_tulpe, min_tulpe, mid_tulpe, med_tulpe
    

def main():
    numbers_sorted = [167,108,99,87,79,65,43,23,13,5,4,1,0]
    numbers_unsorted = [-1,95,134,99,14,11,0,4,1233,43,55,77]
    print('')
    print('-----Функции с нетсортированным массивом-----', '\n')
    print('Массив: ', end='')
    for n in numbers_unsorted:
        print(str(n) + ' ', end='')
    print('')
    print('get_metrics: ', get_met_un(numbers_unsorted))

    print('\n','-----Функции с отсортированным массивом-----','\n')
    print('Массив: ', end='')
    for n in numbers_sorted:
        print(str(n) + ' ', end='')
    print('')
    print('get_metrics: ', get_met(numbers_sorted))

if __name__ == '__main__':
  main()
