import intro 
import main_ingredient
import rice_beans
import fillings
import confirm

cost_of_burrito = 5
ingredient = None
rice = 'No'
beans = 'No'

ingredient,cost_of_burrito = main_ingredient.ask_main_ingredient(cost_of_burrito)
#print(ingredient,cost_of_burrito)

cost_of_burrito, rice, beans = rice_beans.rice_beans(cost_of_burrito)
#print(cost_of_burrito,rice,beans)

burrito_fillings,cost_of_burrito = fillings.fillings(cost_of_burrito)
#print(burrito_fillings,cost_of_burrito)

confirm.user_confirm(cost_of_burrito,ingredient,rice,beans,burrito_fillings)

