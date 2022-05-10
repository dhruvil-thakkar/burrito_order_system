import random 
def user_confirm(cost=5,main_ingredient='Avacado',rice='No',beans='No',fillings=[None]):
    order_no = random.randint(1,10000000)
    print("\nHere's how your Burrito is customized:")
    print("Main Ingredient =",main_ingredient)
    print("Rice =",rice)
    print("Beans =",beans)
    print("Fillings =",fillings)
    print("\nTotal cost of your Burrito is:",cost)
    confirm = input("Confirm your order? Enter Y or N: ")
    while confirm not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
        confirm = input("Invalid Input. Please enter Y or N to confirm your oder: ")
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        print("Thank you for placing your order. Your order is confirmed. Your order number is:",order_no)
    elif confirm.lower() == 'n' or confirm.lower() == 'no':
        print("Your order is cancelled. Please start over again!!")

user_confirm()