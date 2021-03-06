# Burrito Program Intro
import clear
import text_colors
clear.clear()

def get_name():
    print(text_colors.OKCYAN + " __      __       .__                                  __            ")
    print("/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____        ")
    print("\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \       ")
    print(" \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )      ")
    print("  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/       ")
    print("       \/       \/          \/            \/     \/                      ")
    print("  __  .__             ___.                       .__  __                 ")
    print("_/  |_|  |__   ____   \_ |__  __ ________________|__|/  |__ ____         ")
    print("\   __\  |  \_/ __ \   | __ \|  |  \_  __ \_  __ \  \   __ /  _ \        ")
    print(" |  | |   Y  \  ___/   | \_\ \  |  /|  | \/|  | \/  ||  | (  <_> )       ")
    print(" |__| |___|  /\___  >  |___  /____/ |__|   |__|  |__||__|  \____/        ")
    print("           \/     \/       \/                                            ")
    print("                 .___               __          __   .__                 ")
    print("  ___________  __| _/___________  _/  |______  |  | _|__| ____    ____   ")
    print(" /  _ \_  __ \/ __ |/ __ \_  __ \ \   __\__  \ |  |/ /  |/    \  / ___\  ")
    print("(  <_> )  | \/ /_/ \  ___/|  | \/  |  |  / __ \|    <|  |   |  \/ /_/  > ")
    print(" \____/|__|  \____ |\___  >__|     |__| (____  /__|_ \__|___|  /\___  /  ")
    print("                  \/    \/                   \/     \/       \//_____/   ")
    print("                      .__    .__             ._.                         ")
    print(" _____ _____    ____ |  |__ |__| ____   ____| |                          ")
    print("/     \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ |                          ")
    print("|  Y Y  \/ __ \\  \___|   Y  \  |   |  \  ___/\|                         ")
    print("|__|_|  (____  /\___  >___|  /__|___|  /\___  >_                         ")
    print("      \/     \/     \/     \/        \/     \/\/  \n                     ")
    print(text_colors.ENDC +"     Welcome to the burrito order taking machine!")
    print("     We are so glad you are here.")
    global name
    name = input("     What is your name? ")
    print("\n     Welcome " + name + ". You must be hungry. Lets get some delicious Burritos"+"!\n")
    return name

get_name()
