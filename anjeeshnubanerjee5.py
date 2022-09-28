def household():
  print("\nCalculating household Eb price")
  unit=int(input("\nNumber of Units used: "))

  if unit<100:
    price=unit*0.50
    print("Your Price : Rs.",price)
  elif unit>101 and unit<200:
    price=unit*0.75
    print("Your Price : Rs.",price)
  elif unit>201 and unit<300:
    price=unit*1.20
    print("Your Price : Rs.",price)
  else:
    price=unit*1.50
    print("Your Price : Rs.",price)

household()
print("mam please give me good marks")

