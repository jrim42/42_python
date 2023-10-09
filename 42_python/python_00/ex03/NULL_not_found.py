def NULL_not_found(obj: any) -> int:

  if obj is None:
    print(f"{obj}: None <class 'NoneType'>")
  elif isinstance(obj, float) and obj != obj:
    print(f"{obj}: nan <class 'float'>")
  elif isinstance(obj, int) and obj == 0:
    print(f"{obj}: 0 <class 'int'>")
  elif isinstance(obj, str) and obj == '':
    print(f"{obj}: <class 'str'>")
  elif isinstance(obj, bool):
    print(f"{obj}: {obj} <class 'bool'>")
  else:
    print("Type not Found")
    return 1
  
  return 0