import time

def chatbot():
    import main
def game():
    import game

def menu():
    while True:
        print("Welcome to the chatbot!")
        print("-----------------------")
        print()
        choice = int(input("""Please choose one of the options bellow :)
            Chatbot - 1
            Cool Game -  2
            Exit :( - 3
            
            """))


        if choice == 1:
            chatbot()
            break
        elif choice == 2:
            game()
            break
        elif choice == 3:
            print("BYEEE!")
            break
        else:
            print("You have to pick a number!")

menu()