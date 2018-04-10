temp_unit = input("What is the temperature unit? ")
degrees = int(input("What is the temperature to convert? "))

if temp_unit == "f":
    celsius_temp = (degrees - 32) / 1.8
    kelvin_temp = (degrees + 459.67) / 1.8
    print("Celsius: ", celsius_temp)
    print("kelvin: ", kelvin_temp)
elif temp_unit == "C":
    farenheit_temp = degrees * 1.8 + 32
    kelvin_temp = degrees + 273.15
    print("Fahrenheit: ", farenheit_temp)
    print("kelvin: ", kelvin_temp)
elif temp_unit == "k":
    celsius_temp = degrees - 273.15
    farenheit_temp = degrees * 1.8 - 459.67
    print("Celsius: ", celsius_temp)
    print("Fahrenheit: ", farenheit_temp)
else:
    print("We haven't implemented that unit yet!")
