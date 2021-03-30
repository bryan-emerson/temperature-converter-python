temp_value = int(input("please enter temperature"))
temp_unit = input("please enter temp unit f, C, or K")

def convert_temp(temp, unit):
  if unit == "f":
    print(str((temp - 32) / 1.8) + "C")
    print(str((temp + 459.67) / 1.8) + "K")
  elif unit == "C":
    print(str(temp * 1.8 + 32) + "f")
    print(str(temp + 273.15) + "K")
  elif unit == "K":
    print(str(temp - 273.15) + "C")
    print(str(temp * 1.8 - 459.67) + "f")

convert_temp(temp_value, temp_unit)