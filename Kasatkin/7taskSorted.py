def getMax(array):
    if array[0] > array[-1]:
        return array[0]
    else:
        return array[-1]

def getMin(array):
    
    if array[0] < array[-1]:
        return array[0]
    else:
        return array[-1]

def getMid(array):
    midVal = int(len(array) / 2)
    return array[midVal - 1]

def getMed(array):
    medVal = int(len(array) // 2)
    return (array[medVal - 1] + array[medVal]) / 2

def getMet(array):
    maxMet = ('Max', getMax(array))
    minMet = ('Min', getMin(array))
    midMet = ('Mid', getMid(array))
    medMet = ('Med', getMed(array))
    return maxMet, minMet, midMet, medMet

def main():
    array = [222, 189, 150, 133, 99, 98, 79, 68, 36, 25, 16, 1, 0]
    
    print('Массив:')
    for n in array:
        print(n, ' ', end='')
    print()
    print('Метрики:')
    print(getMet(array))

if __name__ == '__main__':
  main()
