import random as r
import checkifprime as check
import fileoperation as file



def addNumbers(*num):
    sum = 0
    for i in num:
        sum = sum + i
        print(sum)


def printMemberAge(**age):
    for i, j in age.items():
        print("Name = %s, Age = %s" %(i, j))

r.randrange(1, 10)

answer = check.checkIfPrime(13)

print(answer)

    
printMemberAge(Peter = 5, Jhon = 7, Ivone = 10)


#file.WriteFile()

file.ReadFile()