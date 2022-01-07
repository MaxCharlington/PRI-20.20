def getMax(array):
    maxN = array[0]
    for n in array:
        if n > maxN:
            maxN = n
    return maxN
    
def getMin(array):
    minN = array[0]
    for n in array:
        if n < minN:
            minN = n
    return minN

def getMid(array):
    sortedArr = sorted(array)
    midVal = int(len(sortedArr) / 2)
    return sortedArr[midVal - 1]

def getMed(array):
    sortedArr = sorted(array)
    medVal = int(len(sortedArr) // 2)
    return (sortedArr[medVal - 1] + sortedArr[medVal]) / 2

def getMet(array):
    maxMet = ('Max', getMax(array))
    minMet = ('Min', getMin(array))
    midMet = ('Mid', getMid(array))
    medMet = ('Med', getMed(array))
    return maxMet, minMet, midMet, medMet
    

def main():
    array = [222, 134, -101, 1, 0, -1, 4, -9, 16, 19, 20]
    print('Массив:')
    for n in array:
        print(n, ' ', end='')
    print()
    print('Метрики:')
    print(getMet(array))

if __name__ == '__main__':
  main()
