import text_colors
# Fillings

#print("     Now it is time to select fillings.")

users_list = '''
     1: Extra beans, add $.50
     2: Chorizo, add $1.00
     3: Onion
     4: Peppers
     5: Salsa
     6: Green chile salsa, add $0.25
     7: Cheese
     8: Extra cheese, add $.050
     9: Potatoes, add $1.00
'''

#print(users_list)

'''
fillings = {
    1: "Extra beans",
    2: "Chorizo",
    3: "Onion",
    4: "Peppers",
    5: "Salsa",
    6: "Green chile salsa",
    7: "Cheese",
    8: "Extra cheese",
    9: "Potatoes"
}
'''

def fillings(cost):
    selections = []
    print(text_colors.WARNING + "\nNow lets add some Fillings to your Burrito!!! We will select from the following options: ")
    print(users_list)
    add_beans = input("Do you want to add beans for additional $0.50? Enter Y or N: ")
    beans = 'No'
    while add_beans.lower() not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        add_beans = input("Invalid Input. Do you want to add beans for additional $0.50? Please enter Y or N: ")
    if add_beans.lower() == 'y' or add_beans.lower() == 'yes':
        cost+=0.50
        selections.append("beans")

    add_Chorizo = input("Do you want to add chorizo for additional $1.00? Enter Y or N: ")
    Chorizo = 'No'
    while add_Chorizo.lower() not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        add_Chorizo = input("Invalid Input. Do you want to add chorizo for additional $1.00? Please enter Y or N: ")
    if add_Chorizo.lower() == 'y' or add_Chorizo.lower() == 'yes':
        cost+=1.00
        Chorizo = 'Yes'
        selections.append("Chorizo")

    add_Green = input("Do you want to add green chile salsa for additional $0.25? Enter Y or N: ")
    beans = 'No'
    while add_Green.lower() not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        add_Green = input("Invalid Input. Do you want to add green chile salsa for additional $0.25? Please enter Y or N: ")
    if add_Green.lower() == 'y' or add_Green.lower() == 'yes':
        cost+=0.25
        Green = 'Yes'
        selections.append("Chile Salsa")

    add_cheese = input("Do you want to add cheese for free? Enter Y or N: ")
    cheese = 'No'
    while add_cheese.lower() not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        add_cheese = input("Invalid Input. Do you want to add cheese for free? Please enter Y or N: ")
    if add_cheese.lower() == 'y' or add_cheese.lower() == 'yes':
        cheese = 'Yes'
        selections.append("Chese")

    add_cheesex = input("Do you want to add extra cheese for additional $0.50? Enter Y or N: ")
    cheesex = 'No'
    while add_cheesex.lower() not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        add_cheese = input("Invalid Input. Do you want to add extra cheese for additional $0.50? Please enter Y or N: ")
    if add_cheesex.lower() == 'y' or add_cheesex.lower() == 'yes':
        cost+=0.50
        cheesex = 'Yes'
        selections.append("Extra Cheese")

    add_Potatoes = input("Do you want to add potatoes for additional $1.00? Enter Y or N: ")
    Potatoes = 'No'
    while add_Potatoes.lower() not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        add_Potatoes = input("Invalid Input. Do you want to add potatoes for additional $1.00? Please enter Y or N: ")
    if add_Potatoes.lower() == 'y' or add_Potatoes.lower() == 'yes':
        cost+=1.00
        Potatoes = 'Yes'
        selections.append("Potatoes")

    add_Onion = input("Do you want to add onion for free? Enter Y or N: ")
    Onion = 'No'
    while add_Onion.lower() not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        add_Onion = input("Invalid Input. Do you want to add onion for free? Please enter Y or N: ")
    if add_Onion.lower() == 'y' or add_Onion.lower() == 'yes':
        Onion = 'Yes'
        selections.append("Onion")

    add_Peppers = input("Do you want to add peppers for free? Enter Y or N: ")
    Peppers = 'No'
    while add_Peppers.lower() not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        add_Peppers = input("Invalid Input. Do you want to add peppers for free? Please enter Y or N: ")
    if add_Peppers.lower() == 'y' or add_Peppers.lower() == 'yes':
        Peppers = 'Yes'
        selections.append("Peppers")

    add_Salsa = input("Do you want to add salsa for free? Enter Y or N: ")
    Salsa = 'No'
    while add_Peppers.lower() not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        add_Salsa = input("Invalid Input. Do you want to add salsa for free? Please enter Y or N: ")
    if add_Salsa.lower() == 'y' or add_Salsa.lower() == 'yes':
        Salsa = 'Yes'
        selections.append("Salsa")

    #print(selections)
    return selections,cost

#fillings()
