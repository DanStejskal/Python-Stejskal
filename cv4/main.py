
def prime_number(number):
  i = number ** 0.5
  while i > 1:
    if number % i == 0:
      return False
    i = i - 1
  return True  

def factorial (number):
  result = 1
  index = 1
  while index < number:
    result = result * number 
    index += 1

def factorial_recursion (number):
  if number < 0:
    return 1
  return factorial_recursion(number - 1) * number

def fibbonachi():
  
  pass

def fibbonachi_recursion(number):
  if number == 0 or number == 1:
    return 1
  return fibbonachi_recursion(number -1) + fibbonachi_recursion (number - 2)

def combination_number():
  pass

def pascal_triangle():
  pass

if __name__ == "__main__":
   lst = []
   number = None
   while number is None or number != -1:
    number = int(input("Zadejte hodnotu: "))
    if number == -1:
       break
    lst.append(number)

   print (f"Max value {max(lst)}")
   print (f"Min value {min(lst)}")
   print (f"Mean value {sum(lst) / len(lst)}")
      