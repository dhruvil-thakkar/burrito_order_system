import random 
import text_colors

def user_confirm(cost,main_ingredient,rice,beans,fillings):
    order_no = random.randint(1,10000000)
    print(text_colors.OKCYAN+"\n#################################################")
    print("\nHere's how your Burrito is customized:\n")
    print("Main Ingredient =",main_ingredient)
    print("Rice =",rice)
    print("Beans =",beans)
    print("Fillings =",fillings)
    print("\nTotal cost of your Burrito is: ${}".format(cost))
    confirm = input(text_colors.FAIL+"\nConfirm your order? Enter Y or N: ")
    while confirm not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        confirm = input("Invalid Input. Please enter Y or N to confirm your oder: ")
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        print(text_colors.OKGREEN+"\nThank you for placing your order. Your order is confirmed. Your order number is:",order_no)
        print("\n")
    elif confirm.lower() == 'n' or confirm.lower() == 'no':
        print("\nYour order is cancelled. Please start over again!!\n")

#user_confirm()