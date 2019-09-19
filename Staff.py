
class Staff:
    def __init__(self, pPosition, pName, pPay):
        self.position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff object')

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" %(self.position, self.name, self.pay)


    def calculatePay(self):
        propmpt = '\n Enter number of hours worked for %s: ' %(self.name)
        hours = input(propmpt)
        propmpt = 'Enter the hourly rate of %s ' %(self.name)
        hourlyRate = input(propmpt)
        self.pay = int(hours) * int(hourlyRate)
        return self.pay


