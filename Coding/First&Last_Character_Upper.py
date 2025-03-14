#Write a program to convert the first and last character as uppercase 

input_string = input("Enter your string : ")
print(input_string[0].upper() + input_string[1 : len(input_string) - 1] + input_string[-1].upper())
