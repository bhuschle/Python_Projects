class Number:
  def __init__(self, num):
    self.number = num

  def printnum(self):
    print(self.number)

  def multipleOf(self):
    num = self.number
    if num % 10 == 0:
      multiple = 10
      break
    elif num % 9 == 0:
      multiple = 9
      break
    elif num % 8 == 0:
      multiple = 8
      break
    elif num % 7 == 0:
      multiple = 7
      break
    elif num % 6 == 0:
      multiple = 6
      break
    elif num % 5 == 0:
      multiple = 5
      break
    elif num % 4 == 0:
      multiple = 4
      break
    elif num % 3 == 0:
      multiple = 3
      break
    elif num % 2 == 0:
      multiple = 2
      break
    else:
      multiple = 1
      break

    if multiple == 1:
      print("Number is a prime number!")
    else:
      print("Number is a multiple of " + multiple)

  def divisibleBy(self):
    
