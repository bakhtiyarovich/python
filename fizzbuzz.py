for fizzzbuzz in range( 1,100):
  if fizzzbuzz % 5 == 0 and fizzzbuzz % 3 == 0:
    print("fizzbuzz")
  elif fizzzbuzz % 5 == 0:
    print("buzz")
  elif  fizzzbuzz % 3 == 0:
    print("fizz")
  else:
    print(fizzzbuzz)

