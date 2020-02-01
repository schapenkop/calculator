def add(number1,number2):
    return number1 + number2

#Inputs
print("What would you like to do?")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Select what you would like to do by selecting the number ")
number1 = float(input("Select number 1: "))
number2 = float(input("Select number 2: "))

if choice == '1': 
    print(add(number1,number2))
else: 
    print("Not a valid response")
    print("Stopping")