
# Вывести таблицу умножения

def mult_table():
    for i in range(1,10):
        for j in range(i,i*10,i):
            print(j, end='\t')
        print()
def main():
    mult_table()

if __name__ == '__main__':
  main()
