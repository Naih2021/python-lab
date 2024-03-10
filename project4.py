zipcode = input("Enter your zipcode number: ")

if zipcode.isdigit() and len(zipcode) == 5:
    print("Your entry is valid")
else:
        print("please enter a valid entry")