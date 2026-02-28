# FILE NAME - convert_C_to_F_02.py

# NAME: Elizabeth Mautz
# DATE: February 28, 2026
# BRIEF DESCRIPTION: ask user convert C to F or F to C
# user is then prompted to enter a temperature
# converted temperature is output



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Temperature Converter =====")
print()
print("  1. Convert from Celsius to Fahrenheit")
print("  2. Convert from Fahrenheit to Celsius")
print()
choice = int(input("Please choose from the above menu: "))

if choice == 1:
    temperature = int(input("Enter a temperature to convert: "))
    converted = temperature * 9/5 + 32
    print()
    print(f"{temperature:.1f} degrees Celsius is {converted} degrees Fahrenheit.")
else:
    temperature = int(input("Enter a temperature to convert: "))
    converted = (temperature - 32 ) * 5/9
    print()
    print(f"{temperature:.1f} degrees Fahrenheit is {converted} degrees Celsius.")










########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
I learned to make sure you're testing your code constantly. If I hadn't done that, I wouldn't
have put the specific decimal place that the input temeperature needs to go to.






'''