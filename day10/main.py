import replit
from art import logo

# def add(n1, n2):
#   return n1+n2

# def subtract(n1,n2):
#   return n1-n2

# def multiply(n1,n2):
#   return n1*n2

# def divide(n1,n2):
#   return n1/n2

# n1 = int(input("Enter the first number.\n"))
# n2 = int(input("Enter the second number.\n"))
# operation = input("Which operation would you like to perform? add, subtract, multiply. divide \n")

# def calc(n1,n2):
#   if operation == 'add':
#       result = add(n1,n2)
#       return result
#   elif operation == 'subtract':
#       result = subtract(n1,n2)
#       return result
#   elif operation == 'multiply':
#       result = multiply(n1,n2)
#       return result
#   elif operation == 'divide':
#       result = divide(n1,n2)
#       return result
  

# print(calc(n1,n2))
# result = calc(n1,n2)
# cont = input('Would you like to continue the operation with the result? If yes, enter y, else n \n') 

# while cont == 'y':
#   n3 = int(input('Enter the number. \n'))
#   operation = input("Which operation would you like to perform? add, subtract, multiply, divide \n")
#   print(calc(result, n3))
#   result = calc(result,n3)
#   cont = input('Would you like to continue the operation with the result? If yes, enter y, else n \n')

# if cont == 'n':
#   replit.clear()
#   n1 = int(input("Enter the first number.\n"))
#   n2 = int(input("Enter the second number.\n"))
#   operation = input("Which operation would you like to perform? add, subtract, multiply. divide \n")

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      replit.clear()
      calculator()

calculator()
