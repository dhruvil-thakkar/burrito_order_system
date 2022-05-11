import text_colors

def rice_beans(cost):
    print(text_colors.OKGREEN+"\nNow we will select if you want to add Rice or Beans. Adding Rice or Cilantro Rice will be additional $0.25. You can add Beans for free")
    add_rice = input("\nDo you want to add Rice for additional $0.25? Enter Y or N: ")
    rice = 'No'
    while add_rice.lower() not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        add_rice = input("Invalid Input. Do you want to add Rice for additional $0.25? Please enter Y or N: ")
    if add_rice.lower() == 'y' or add_rice.lower() == 'yes':
        cost+=0.25
        rice = 'Yes'
    add_beans = input("Do you want to add Beans for free? Enter Y or N: ")
    beans = 'No'
    while add_beans.lower() not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:   
        add_beans = input("Invalid Input. Do you want to add beans for free? Please enter Y or N: ")
    if add_beans.lower() == 'y' or add_beans.lower() == 'yes':
        beans = 'Yes'
    #print(cost,rice,beans)
    print("\nYou have selected {0} for Rice and {1} for Beans. Your current cost is ${2}".format(rice,beans,cost))
    return cost, rice, beans

#rice_beans()
