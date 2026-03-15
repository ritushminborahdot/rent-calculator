rent = int(input("Enter your house/hostel rent: "))
food = int(input("Enter your total food bill amount: "))
electricity = int(input("Enter your electricity bill amount: "))
other_expenses = int(input("Enter your other expenses amount: "))
number_of_persons = int(input("Enter total number of persons: "))
output = (rent+food+electricity+other_expenses) // number_of_persons
print("Per person will pay: ", output)