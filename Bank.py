class Atm(object):
    def __init__(self,pin,creditCardNumber,cash):
        self.pin=pin
        self.creditCardNumber=creditCardNumber
        self.cash=cash
    def withDraw(self):
        print("cash is successfully been withDraw")
    def balance(self):
        print("your balance is been shortly been noted")
    def Deposist(self):
        print("cash is successfully been Deposisted ")

Axis = Atm(1234,56789,3000)


print(Axis.pin)
print(Axis.cash)
print(Axis.creditCardNumber)

Axis.withDraw()
Axis.balance()
Axis.Deposist()
