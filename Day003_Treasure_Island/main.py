print('''
 _                                                         
| |                                                          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                      | |    
                                                      |_|    
''')

print("Welcome to Treasure Island.")
print("Your Mission is to find the treasure")
choice_1 = input('You´re at a crossroad, where do you want to go Type "left" or "right". \n>>').lower()

if choice_1 == "left":
    choice_2 = input('You´ve come to a lake and see an Island in the middle of the lake' \
'Type "wait" to wait for a boat. Type "swim" to swim across. \n>> ').lower()

    if choice_2 == "wait":
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. A red one, one is blue and the other one is green. Which color do you choose? \n>>").lower()
        if choice_3 == "red":
            print("It`s a room full of fire. Game Over :(")
        elif choice_3 == "blue":
            print("You found the Treasure. You Win!")
        elif choice_3 == "green":
            print("You got attacked by Scorpions. Game Over :(")
    else:
        print("You got attacked by an angry trout. Game Over :(")


else:
    print("Uh oh. Wrong direction and you fell in to a hole. Game Over :( ")
