
class Calculator():
    def addition(self, num1, num2):
        return num1 + num2
    def subtraction(self, num1, num2):
        return num1- num2
    def devision(self, num1, num2):
        if num2 == 0:
            return 0
        else:
            return num1/num2
    def multiplication(self, num1, num2):
        return num1*num2
        

if __name__ == "__main__":
    cal = Calculator()
    print(cal.addition(2, 6))
    print(cal.subtraction(9, 2))
    print(cal.multiplication(2, 9))
    print(cal.devision(19, 3))
