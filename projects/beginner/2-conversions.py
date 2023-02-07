choice = input(
    "Pick F to convert from Fahrenheit to Celsius or C to convert from Celsius to Fahrenheit: "
)
if choice == "F":
    tempf = float(input("Enter a temperature in Fahrenheit: "))
    tempc = (tempf - 32) / 1.8
    print("The temp is " + tempc + " degrees Celsius.")
elif choice == "C":
    tempc = float(input("Enter a temperature in Celsius: "))
    tempf = (tempc * 1.8) + 32
    print("The temp is " + tempf + " degrees Celsius.")
