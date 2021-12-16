def IsItSorted(list):
        i = 1
        sorted = 0
        while i < len(list):
            if list[i-1] <= list[i]:
                sorted = 1
            else:
                sorted = 0
            i += 1
        return sorted

class Metrics():
    
    cash = [-1,-1,-1,-1]

    def __init__(self,list):
        self.list = list
        self.sort = IsItSorted(self.list)
    
    ''' Поиск максимального числа списка '''
    def get_max(self):
        if self.sort: # Если список отсортированный
            if self.cash[0] == -1: # Если в кэше нет максимального элемента
                if (self.list[-1] > self.list[0]):
                    self.cash[0] = self.list[-1] # Добавляем максимальный в кэш
                    return self.list[-1]
                else:
                    self.cash[0] = self.list[0] # Добавляем максимальный в кэш
                    return self.list[0]
            else:
                return self.cash[0]
        else: # Если список НЕ отсортированный
            if self.cash[0] == -1: # Если в кэше нет максимального
                l_max = self.list[0]
                for i in self.list:
                    if i > l_max:
                        l_max = i
                self.cash[0] = l_max # Добавляем максимальный в кэш
                return l_max
            else:
                return self.cash[0]
    
    ''' Поиск минимального числа списка '''
    def get_min(self):
        if self.sort: # Если список отсортированный
            if self.cash[1] == -1: # Если в кэше нет минимального элемента
                if (self.list[-1] > self.list[0]):
                    self.cash[1] = self.list[0] # Добавляем минимальный в кэш
                    return self.list[0]
                else:
                    self.cash[1] = self.list[-1] # Добавляем минимальный в кэш
                    return self.list[-1]
            else:
                return self.cash[1]
        else: # Если список НЕ отсортированный
            if self.cash[1] == -1: # Если в кэше нет минимального элемента
                l_min = self.list[0]
                for i in self.list:
                    if i < l_min:
                        l_min = i
                self.cash[1] = l_min # Добавляем минимальный в кэш
                return l_min
            else:
                return self.cash[1]

    ''' Поиск среднего арифметического числа списка '''
    def get_mid(self):
        if self.cash[2] == -1: # Если в кэше нет среднего
            counter = 0
            summa = 0
            for i in self.list:
                summa += i
                counter += 1
            self.cash[2] = summa/counter # Добавляем средний в кэш
            return summa/counter
        else:
            return self.cash[2]

    ''' Поиск медианного числа списка '''
    ''' Медианное число - число, у которого '''
    ''' кол-во меньших его чисел равно кол-ву больших его чисел '''
    ''' Ну или если кол-во чисел нечетное, то число посередине (список отсортированный должен быть) '''
    ''' Если кол-во четно, то ср.арифметическое двух чисел посередине (список отсортированный должен быть) '''
    def get_med(self):
        if self.sort: # Если список отсортированный
            if self.cash[3] == -1: # Если в кэше нет медианного
                sr = self.list[len(self.list)//2]
                less = 0
                more = 0
                
                for i in self.list:
                    if i < sr:
                        less += 1
                    if i > sr:
                        more += 1
                if less == more:
                    self.cash[3] = sr # Добавляем медианный в кэш
                    return sr
                if (self.list[-1] > self.list[0]):
                    if less > more:
                        self.cash[3] = (sr + self.list[(len(self.list) // 2) - 1])/2 # Добавляем медианный в кэш
                        return (sr + self.list[(len(self.list) // 2) - 1])/2
                    if less < more:
                        self.cash[3] = (sr + self.list[(len(self.list) // 2) + 1])/2 # Добавляем медианный в кэш
                        return (sr + self.list[(len(self.list) // 2) + 1])/2
                else:
                    if less < more:
                        self.cash[3] = (sr + self.list[(len(self.list) // 2) - 1])/2 # Добавляем медианный в кэш
                        return (sr + self.list[(len(self.list) // 2) - 1])/2
                    if less > more:
                        self.cash[3] = (sr + self.list[(len(self.list) // 2) + 1])/2 # Добавляем медианный в кэш
                        return (sr + self.list[(len(self.list) // 2) + 1])/2
            else:
                return self.cash[3]
        else: # Если список НЕ отсортированный
            if self.cash[3] == -1: # Если в кэше нет медианного
                median = self.list[0]
                median_2 = 0
                less = 0
                more = 0
                
                for i in range(len(self.list)):
                    for j in range(len(self.list)):
                        if (self.list[i] < self.list[j]) and i!=j:
                            more+=1
                        if (self.list[i] >= self.list[j]) and i!=j:
                            less+=1
                    if len(self.list) % 2 == 1:
                        if less == more:
                            median = self.list[i]
                            break
                        else:
                            less = 0
                            more = 0
                    else:
                        if abs(less-more) == 1:
                            median_2 = self.list[i] + median_2
                        less = 0
                        more = 0
                if len(self.list) % 2 == 1:
                    self.cash[3] = median # Добавляем медианный в кэш
                    return median
                else:
                    self.cash[3] = median_2/2 # Добавляем медианный в кэш
                    return median_2/2
            else:
                return self.cash[3]

    ''' Функция, составляющая кортеж из значений 4-х предыдущих функций '''
    def get_metrics(self):

        if self.sort: # Если список отсортированный
            max_elem = self.list[0]
            min_elem = self.list[0]
            mid_elem = 0
            med_elem = 0
            
            sr = self.list[len(self.list)//2]
            less = 0
            more = 0
            summa = 0
            
            for i in self.list:
                if self.cash[2] == -1:
                    summa += i

                if self.cash[0] == -1:
                    if i > max_elem:
                        max_elem = i
                else:
                    max_elem = self.cash[0]
                
                if self.cash[1] == -1:
                    if i < min_elem:
                        min_elem = i
                else:
                    min_elem = self.cash[1]
                
                if self.cash[3] == -1:
                    if i < sr:
                        less += 1
                    if i > sr:
                        more += 1
                    
                    if less == more:
                        med_elem = sr
                    if (self.list[-1] > self.list[0]):
                        if less > more:
                            med_elem = (sr + self.list[(len(self.list) // 2) - 1])/2
                        if less < more:
                            med_elem (sr + self.list[(len(self.list) // 2) + 1])/2
                    else:
                        if less < more:
                            med_elem = (sr + self.list[(len(self.list) // 2) - 1])/2
                        if less > more:
                            med_elem = (sr + self.list[(len(self.list) // 2) + 1])/2
                else:
                    med_elem = self.cash[3]   

            if self.cash[0] == -1: # Добавляем максимальный в кэш
                self.cash[0] = max_elem

            if self.cash[1] == -1: # Добавляем минимальный в кэш
                self.cash[1] = min_elem

            if self.cash[3] == -1: # Добавляем медианный в кэш
                self.cash[3] = med_elem

            if self.cash[2] == -1: # Добавляем средний в кэш
                mid_elem = summa/len(self.list)
                self.cash[2] = summa/len(self.list)
                
            metrics = (max_elem,min_elem,mid_elem,med_elem)
            return metrics
        else: # Если список НЕ отсортированный
            max_elem = self.list[0]
            min_elem = self.list[0]
            mid_elem = 0
            med_elem = 0
            
            summa = 0
            median = self.list[0]
            median_2 = 0
            less = 0
            more = 0
            
            for i in range(len(self.list)):
                
                if self.cash[0] == -1: # Если нет максимального
                    if self.list[i] > max_elem:
                        max_elem = self.list[i]
                else:
                    max_elem = self.cash[0]
                
                if self.cash[1] == -1: # Если нет минимального
                    if self.list[i] < min_elem:
                        min_elem = self.list[i]
                else:
                    min_elem = self.cash[1]

                if self.cash[2] == -1: # Если нет среднего
                    summa += self.list[i]
                

                if self.cash[3] == -1: # Если нет медианного
                    for j in range(len(self.list)):
                        if (self.list[i] < self.list[j]) and i!=j:
                            more+=1
                        if (self.list[i] >= self.list[j]) and i!=j:
                            less+=1
                    if len(self.list) % 2 == 1:
                        if less == more:
                            median = self.list[i]
                            less = 0
                            more = 0
                        else:
                            less = 0
                            more = 0
                    else:
                        if abs(less-more) == 1:
                            median_2 = self.list[i] + median_2
                        less = 0
                        more = 0

            if self.cash[0] == -1: # Добавляем максимальный в кэш
                self.cash[0] = max_elem

            if self.cash[1] == -1: # Добавляем минимальный в кэш
                self.cash[1] = min_elem
            
            if self.cash[3] == -1: # Если нет медианного
                if len(self.list) % 2 == 1:
                    med_elem = median
                    self.cash[3] = median # Добавляем медианный в кэш
                else:
                    med_elem = median_2/2
                    self.cash[3] = median_2/2 # Добавляем медианный в кэш
            else:
                if len(self.list) % 2 == 1:
                    med_elem = self.cash[3]
                else:
                    med_elem = self.cash[3]
            
            if self.cash[2] == -1: # Если нет среднего в кэше
                mid_elem = summa/len(self.list)
                self.cash[2] = summa/len(self.list) # Добавляем средний в кэш
            else:
                mid_elem = self.cash[2]
            
            metrics = (max_elem,min_elem,mid_elem,med_elem)
            
            return metrics


def main():
    #a = Metrics([1,2,3,4,5,6])
    #a = Metrics([5,4,3,2,1])
    a = Metrics([1,2,3,4,5])
    print(a.cash)
    metrics = a.get_max()
    #metrics = a.get_min()
    #metrics = a.get_med()
    #metrics = a.get_metrics()
    print(metrics)
    print(a.cash)

if __name__ == "__main__":
    main()