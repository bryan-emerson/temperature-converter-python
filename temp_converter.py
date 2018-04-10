temp_unit = input("What is the temperature unit? ")
degrees = int(input("What is the temperature to convert? "))

if temp_unit == "f":
    converted_temp = (degrees - 32) / 1.8
    print(converted_temp)
elif temp_unit == "C":
    converted_temp = degrees * 1.8 + 32
    print(converted_temp)
else:
    print("We haven't implemented that unit yet!")
