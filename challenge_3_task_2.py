def ask_user_for_number():
  while True:
    number = input("Enter an integer: ")
    try:
      number = int(number)
      return number
    except ValueError:
      print("That's not an integer try again")

def total_sum(number):
  sum_number = 0
  for i in range(number + 1):
    sum_number += i
  return sum_number

def mult_3_5_sum(number):
  sum_number = 0
  for i in range(number + 1):
    if i % 3 == 0 or i % 5 == 0:
      sum_number += i
  return sum_number

def total_product(number):
  product_number = 1
  for i in range(number):
    product_number *= (i + 1)
  return product_number

def sum_or_product():
  number = ask_user_for_number()
  print("Please choose one of the options below:")
  print(f"1. Compute the sum of the numbers from 1 to {number}")
  print(f"2. Compute the product of the numbers from 1 to {number}")
  choice = input("Enter your choice here: ")
  if choice == '1':
    print(total_sum(number))
  elif choice == '2':
    print(total_product(number))
  else:
    print("That is not one of the choices")

sum_or_product()
