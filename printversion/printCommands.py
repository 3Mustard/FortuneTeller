import random
from printversion import tarotdict


def main_menu():
    print("Welcome to fortune teller.")
    print("-------------------------")
    print("Please select an option:")
    print("1. Tarot")
    user_selection = input("> ")  # stores the users selection

    if user_selection == "1":  # 1.Tarot option
        print("-------------------------")
        print("Please select how many cards you wish to draw.")
        print("1. Single card draw.")
        print("2. Three card draw (Past, Present, Future)")
        print("3. Card information")
        print("0. Main menu")
        user_tarot_selection = input("> ")
        if user_tarot_selection == "1":
            draw_one()
        if user_tarot_selection == "2":
                draw_three()
        if user_tarot_selection == "3":
                card_info()
        if user_tarot_selection == "0":
            main_menu()
        else:
            print("Please make a valid selection. Returning to the main menu.")
            main_menu()
    else:
        print("Please make a valid selection. Returning to the main menu.")
        main_menu()

def menu_prompt():
    print("Would you like to return to the main menu or see more information on a card?")
    print("1. More information\n0. Main menu")
    end_option = input("> ")
    if end_option == "1":
        card_info()
    if end_option == "0":
        main_menu()

#tarot option functions
#option 1. draw one  function
def draw_one():
    single_draw = random.randint(1,78)
    single_up_or_down = random.randint(1,2) #decides if card is face up or down. 1==face up && 2==face down
    print("-------------------------")
    print("You have drawn the " + tarotdict.tarot[single_draw] + " card.")#print card draw
    if single_up_or_down == 1: #determine if face up or down
        print("Your card is facing up and represents:")
        print(tarotdict.tarot_face_up[single_draw])
        print("-------------------------")
    else:
        print("Your card is facing down and represents:")
        print(tarotdict.tarot_face_down[single_draw])
        print("-------------------------")
    menu_prompt()

#option 2. draws three cards to represent the users past, present and future
def draw_three():
    #face up == 1 and face down == 2
    past_random = random.randint(1,78) #selects a card for past
    past_up_or_down = random.randint(1,2) #determines face up or down for past
    present_random = random.randint(1,78) #selects a card for present
    present_up_or_down = random.randint(1,2) #determines face up or down for present
    future_random = random.randint(1,78) #selects a card for future
    future_up_or_down = random.randint(1,2) #determines face up or down future
    
    print("-------------------------")#print past card
    print("Your past is the " + tarotdict.tarot[past_random] + " card.")
    if past_up_or_down == 1: #determines if the card is face up or down and prints appropriate response.
        print("Your card is facing up and represents:")
        print(tarotdict.tarot_face_up[past_random])
        print("-------------------------")
    else:
        print("Your card is facing down and represents:")
        print(tarotdict.tarot_face_down[past_random])
        print("-------------------------")
    
    if past_random == present_random: #checks if the past card is the same as the present card. If it is a new card is assigned to present.
        present_random = random.randint(1,78)
        print("Your present is the " + tarotdict.tarot[present_random] + " card.") #print present card
    if present_up_or_down == 1: #determines if the card is face up or down and prints the appropriate response.
        print("Your card is facing up and represents:")
        print(tarotdict.tarot_face_up[present_random])
        print("-------------------------")
    else:
        print("Your card is facing down and represents:")
        print(tarotdict.tarot_face_down[present_random])
        print("-------------------------")
    
    if past_random == future_random or present_random == future_random: #checks if the future card is the same as the past or present card. If it is a new card is assigned to future.
        future_random = random.randint(1,78)
        print("Your future is the " + tarotdict.tarot[future_random] + " card.") #print future card

    if future_up_or_down == 1: #determines if the card is face up or down and prints the appropriate response.
        print("Your card is facing up and represents:")
        print(tarotdict.tarot_face_up[future_random])
        print("-------------------------")
    else:
        print("Your card is facing down and represents:")
        print(tarotdict.tarot_face_down[future_random])
        print("-------------------------")
        #end of draw options
        print("Would you like to return to the main menu or see more information on a card?")
        print("1. More information\n0. Main menu")
        end_option = input("> ")

    if end_option == "1":
        card_info()
    if end_option == "0":
        main_menu()
        
#function for obtaining information on cards
def card_info():
    print("-------------------------")
    print("Which type of card would you like more information on?")
    print("1. Wands\n2. Cups\n3. Swords\n4. Pentacles\n5. Ace\n6. II\n7. III\n8. IV\n9. V\n10. VI\n11. VII\n12. VIII\n13. IX\n14. X\n15. Page\n16. Knight\n17. Queen\n18. King\n0. Return to main menu.")
    print("-------------------------")
    info_choice = input("> ")
    
    if info_choice == "0":
        main_menu()
    if info_choice == "1":
        print("Wands\n------\nElement: Fire\npassion, desire, will")
        more_information()
    if info_choice == "2":
        print("Cups\n------\nElement: Water\nemotions, feelings, relationships")
        more_information()
    if info_choice == "3":
        print("Swords\n------\nElement: Air\nlogic, ideas, intellect")
        more_information()
    if info_choice == "4":
        print("Pentacles\n------\nElement: Earth\nearthly, material, sensual")
        more_information()
    if info_choice == "5":
        print("Aces represent beginnings, potential and new initiatives")
        more_information()
    if info_choice == "6":
        print("II represents decisions, balance and partnership")
        more_information()
    if info_choice == "7":
        print("III represents growth, creativity and expression")
        more_information()
    if info_choice == "8":
        print("IV represents stability, application and formation")
        more_information()
    if info_choice == "9":
        print("V represents conflict, change and expansion")
        more_information()
    if info_choice == "10":
        print("VI represents cooperation, harmony and compassion")
        more_information()
    if info_choice == "11":
        print("VII represents spirituality, wisdom and exploration")
        more_information()
    if info_choice == "12":
        print("VIII represents action, change and regeneration")
        more_information()
    if info_choice == "13":
        print("IX represents fulfillment, idealism and inspiration")
        more_information()
    if info_choice == "14":
        print("X represents completion, finality and renewal")
        more_information()
    if info_choice == "15":
        print("Pages represent a new spark, they are are the holders of energy for their suit")
        more_information()
    if info_choice == "16":
        print("Knights represent a messanger, they bring the energy of their suit out into the world")
        more_information()
    if info_choice == "17":
        print("Queens represent a keeper or influencer, they master the energy of their suit and subtly bring them to others")
        more_information()
    if info_choice == "18":
        print("Kings represent the master and executor, they control and reign over their suit bringing power to action")
        more_information()
    else:
        print("Please enter a valid selection.")
        card_info()
        
def more_information():
    print("Would you like information on another card type? (y/n)")
    y_n = input("> ")
    if y_n == "y":
        card_info()
    if y_n == "n":
        main_menu()
    else:
        print("Please enter 'y' or 'n'" )
        more_information()