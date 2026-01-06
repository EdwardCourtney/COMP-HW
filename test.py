#W8A4
class Calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def subtract(self):
        return self.x - self.y
    def multiply(self):
        return self.x * self. y
    def divide(self):
        if self.y == 0:
            return "ERROR: DIVIDE BY 0"
        else:
            return self.x/self.y
    def mod(self):
        if self.y == 0:
            return "ERROR: DIVIDE BY 0"
        else:
            return self.x%self.y
    def power(self):
        return self.x ** self.y
    def update(self, x, y):
        self.x = x
        self.y = y
print("**Welcome to Calculator**")
x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))
C = Calculator(x,y)
while True:
    print(f"**Your numbers are {C.x} and {C.y}**")
    print("COMMAND GUIDE: ")
    print("- 1. Add")
    print("- 2. Subtract")
    print("- 3. Multiply")
    print("- 4. Divide")
    print("- 5. Mod")
    print("- 6. Power")
    print("- 7. Update numbers")
    I = int(input("Please input Command: "))
    print("Output:")
    if I == 1:
        print(C.add())
    if I == 2:
        print(C.subtract())
    if I == 3:
        print(C.multiply())
    if I == 4:
        print(C.divide())
    if I == 5:
        print(C.mod())
    if I == 6:
        print(C.power())
    if I == 7:
        x = int(input("Please enter the first number: "))
        y = int(input("Please input the second number: "))
    print("Do you want to exit the program? Enter Yes to Exit")
    O = input()
    if (O == "Yes"):
        print("Thank you for using Calculator")
        break
    print("---------------")