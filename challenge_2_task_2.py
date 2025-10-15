import random

def reverse_name (name):
  name = list(name)
  name.reverse()
  name = ''.join(name)
  return name

def intersperse_name(name, surname):
  interspersed_name = ''
  name = reverse_name(name)
  if len(name) > len(surname):
    for i in range(len(surname)):
      interspersed_name += name[i] + surname[i]
    interspersed_name += name[len(surname):]
  else:
    for i in range(len(name)):
      interspersed_name += name[i] + surname[i]
    interspersed_name += surname[len(name):]
  return interspersed_name

def format_name(name, surname):
  interspersed_name = intersperse_name(name, surname)
  first_name = interspersed_name[:len(interspersed_name)//2]
  second_name = interspersed_name[len(interspersed_name)//2:]
  user_name = first_name.capitalize() + " " + second_name.capitalize()
  return user_name

def random_username():
  username = ''
  for i in range(10):
    character = random.choice("1234567890abcdefghijklmnopqrstuvwxyz")
    username += character
  username = username[:len(username)//2] + " " + username[len(username)//2:]
  return username

print("Welcome to the username creator... Please choose one of the following options:")
print("1. Create a username based on a name")
print("2. Generate a random username")
choice = input("Enter your choice here: ")
if choice == '1':
  first_name = input("Enter your first name here: ")
  surname = input(" Enter your surname here: ")
  print(f"Your username is: {format_name(first_name, surname)}")
elif choice == '2':
  print(f"Your random username is: {random_username()}")
else:
  print("That is not one of the choices")
