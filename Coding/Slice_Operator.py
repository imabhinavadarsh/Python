#write a program to convert the first character of the string to capital.

smaller_string = "abhinav"
print("without conversion : " + smaller_string)
upper_string = smaller_string[0].upper() + smaller_string[1 : ]
print("with conversion : " + upper_string)
