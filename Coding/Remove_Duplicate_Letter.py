def rev_dup():
    try:
        user_str = input("Enter the string: ").strip() #Writing the risky code in try block and used.strip() to remvover extra spaces

        if not user_str:
            print("String cannot be empty") #Check the Validation
            return

        set_str = set(user_str)
        print(f"After removing duplicate characters: {set_str}")

    except ValueError as e :
        print(f"Error: {e}") #Handling code in this except block

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    rev_dup() #Calling my fuction 
