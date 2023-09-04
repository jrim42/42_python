import sys

def check_odd_even(number):
  try:
    if not isinstance(number, int):
      raise AssertionError("AssertionError: argument is not an integer")
  
    if number % 2 == 0:
      print("I'm Even.")
    else:
      print("I'm Odd.")
  except AssertionError as e:
    print(e)

if __name__ == "__main__":
  if len(sys.argv) == 1:
    exit(0)

  try:
    if len(sys.argv) > 2:
      raise AssertionError("AssertionError: more than one argument is provided")
    
    argument = sys.argv[1]
    
    try:
      num = int(argument)
      check_odd_even(num)
      
    except ValueError:
      raise AssertionError("AssertionError: argument is not an integer")
    
  except AssertionError as e:
    print(e)