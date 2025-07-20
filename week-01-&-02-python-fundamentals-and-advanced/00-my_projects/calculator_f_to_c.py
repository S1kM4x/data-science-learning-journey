
print("Welcome to the °F ↔ °C temperature converter")
print("Choose an option: 1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius")

option = input("Enter option (1 or 2): ")

if option == "1":
    temp_c = float(input("Enter temperature in Celsius: "))
    result = temp_c * 9/5 + 32
    print(f"{temp_c} °C is equal to {result:.2f} °F")

elif option == "2":
    temp_f = float(input("Enter temperature in Fahrenheit: "))
    result = (temp_f - 32) * 5/9
    print(f"{temp_f} °F is equal to {result:.2f} °C")

else:
    print("Invalid option.")


