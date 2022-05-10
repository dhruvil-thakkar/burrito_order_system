#this is an example of the switch used
#Decalaration of the variables used
FIRST_INGREDIENT_SELECTED = False
FIRST_INGREDIENT_NAME = ""
FIRST_SELECTION = 0
TOTAL_PRICE = 5

def FIRST_ING (FIRST_SELECTION,TOTAL_PRICE): 
    if int(FIRST_SELECTION) == 1:
        FIRST_INGREDIENT_NAME = "Ground beef"
        FIRST_INGREDIENT_SELECTED = True
        return FIRST_INGREDIENT_NAME,TOTAL_PRICE

    elif int(FIRST_SELECTION) == 2:
        FIRST_INGREDIENT_NAME = "Carne asada"
        FIRST_INGREDIENT_SELECTED = True
        TOTAL_PRICE += 1
        return FIRST_INGREDIENT_NAME,TOTAL_PRICE       

    elif int(FIRST_SELECTION) == 3:
        FIRST_INGREDIENT_NAME = "Carne adovada"
        FIRST_INGREDIENT_SELECTED = True
        TOTAL_PRICE = TOTAL_PRICE+1
        return FIRST_INGREDIENT_NAME,TOTAL_PRICE

    elif int(FIRST_SELECTION) == 4:
        FIRST_INGREDIENT_NAME = "Scrambled eggs"
        FIRST_INGREDIENT_SELECTED = True
        return FIRST_INGREDIENT_NAME,TOTAL_PRICE  

    elif int(FIRST_SELECTION) == 5:
        FIRST_INGREDIENT_NAME = "Chicken"
        FIRST_INGREDIENT_SELECTED = True
        return FIRST_INGREDIENT_NAME,TOTAL_PRICE 

    elif int(FIRST_SELECTION) == 6:
        FIRST_INGREDIENT_NAME = "Sofritas"
        FIRST_INGREDIENT_SELECTED = True
        return FIRST_INGREDIENT_NAME,TOTAL_PRICE

def ask_main_ingredient(TOTAL_PRICE):
    while FIRST_INGREDIENT_SELECTED == False:
        print ("Please select one of the fillowing ingredients by typing the number")
        print ("1 - Ground beef")
        print ("2 - Carne asada (add $1.00)")
        print ("3 - Carne adovada (add $1.00)")
        print ("4 - Scrambled eggs")
        print ("5 - Chicken")
        print ("6 - Sofritas")
        FIRST_SELECTION = input("Type the number from 1 to 6:>  ")
        while True:
            try:
                int(FIRST_SELECTION)
                if int(FIRST_SELECTION) in [1,2,3,4,5,6]:
                    FIRST_INGREDIENT_NAME,TOTAL_PRICE=FIRST_ING(FIRST_SELECTION,TOTAL_PRICE)
            except ValueError:
                FIRST_SELECTION = input("Invalid Input. Type the number from 1 to 6:>  ")
        #FIRST_INGREDIENT_NAME,TOTAL_PRICE=FIRST_ING(FIRST_SELECTION,TOTAL_PRICE)
        try:
            int(FIRST_SELECTION)
        except ValueError:
            print("Please enter a valid number")
            continue
        if int(FIRST_SELECTION) in [1,2,3,4,5,6]:
            print("In if")
            break
        else:
            continue

    print("you choose "+FIRST_INGREDIENT_NAME+" whith the cost of "+str(TOTAL_PRICE))
    print(FIRST_INGREDIENT_NAME,TOTAL_PRICE)
    
    
#print (FIRST_INGREDIENT_SELECTED)

ask_main_ingredient(TOTAL_PRICE)