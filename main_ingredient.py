#this is an example of the switch used



#Decalaration of the variables used
FIRST_INGREDIENT_SELECTED = False
FIRST_INGREDIENT_NAME = ""
FIRST_SELECTION = 0

TOTAL_PRICE = 5


if int(FIRST_SELECTION) == 1:
    FIRST_INGREDIENT_NAME = "Ground beef"
    FIRST_INGREDIENT_SELECTED = True
    
if int(FIRST_SELECTION) == 2:
    FIRST_INGREDIENT_NAME = "Carne asada"
    FIRST_INGREDIENT_SELECTED = True
    TOTAL_PRICE = TOTAL_PRICE + 1
if int(FIRST_SELECTION) == 3:
    FIRST_INGREDIENT_NAME = "Carne adovada"
    FIRST_INGREDIENT_SELECTED = True
    TOTAL_PRICE = TOTAL_PRICE + 1
if int(FIRST_SELECTION) == 4:
    FIRST_INGREDIENT_NAME = "Scrambled eggs"
    FIRST_INGREDIENT_SELECTED = True
    
if int(FIRST_SELECTION) == 5:
    FIRST_INGREDIENT_NAME = "Chicken"
    FIRST_INGREDIENT_SELECTED = True
    
if int(FIRST_SELECTION) == 6:
    FIRST_INGREDIENT_NAME = "Sofritas"
    FIRST_INGREDIENT_SELECTED = True
    

def int_check (FIRST_SELECTION):
    try:
        int(FIRST_SELECTION)
        it_is = True
    except ValueError:
        it_is = False

while FIRST_INGREDIENT_SELECTED == False :
    
    print ("Please select one of the fillowing ingredients by typing the number")
    print ("1 - Ground beef")
    print ("2 - Carne asada (add $1.00)")
    print ("3 - Carne adovada (add $1.00)")
    print ("4 - Scrambled eggs")
    print ("5 - Chicken")
    print ("6 - Sofritas")
    FIRST_SELECTION = input("Type the number from 1 to 6:>  ")
    try:
        int(FIRST_SELECTION)
    except ValueError:
        print("Please enter a valid number")
        continue
    if int(FIRST_SELECTION):
        break
