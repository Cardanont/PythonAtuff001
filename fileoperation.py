

def ReadFile():
    f = open('../../files/myfile.txt', 'r')

    for line in f:
        print(line, end ='')

    f.close()

def WriteFile():
    f = open('../../files/myfile.txt', 'a')

    f.write('\nThis line will be appended.')
    f.write('\nPython is Fun!')

    f.close()