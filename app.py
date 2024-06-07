#write hello world to the console
#crea una lista de opciones con las que el usuaruo puede interactuar para escoger 'paper','scissors','rock'
#el usuario escoge una opcion
#la computadora escoge una opcion
#se compara la opcion del usuario y la de la computadora para determinar quien gana
#se imprime el resultado

import random
jugando = True
while jugando:
    puntuación = 0
    choices = ['paper', 'scissors', 'rock']
    user_choice = input('Choose between paper, scissors and rock: ').lower()
    computer_choice = random.choice(choices)
    #Ahora necesito que verifiques si el usuario escogió o no una opción valida, si dio una opción no valida, hazle saber que no es valida y pidele que escoja de nuevo
    while user_choice not in choices:
        print('Invalid choice')
        user_choice = input('Choose between paper, scissors and rock: ').lower()
    #Haz algo que se vea más agradable a la vista, como 'opcion jugador ' vs. 'opcion computadora'
    print('User chose:', user_choice)
    print('Computer chose:', computer_choice)
    #Ahora necesito que compares las opciones del usuario y la computadora para determinar quién ganó
    if user_choice == computer_choice:
        print('It\'s a tie!')
        puntuación += 1
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('You win!')
            puntuación += 1
        else:
            print('You lose!')
            puntuación -= 1
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print('You win!')
            puntuación += 1
        else:
            print('You lose!')
            puntuación -= 1
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print('You win!')
            puntuación += 1
        else:
            print('You lose!')
            puntuación -= 1
    #Ahora necesito que me muestres la puntuación actual del usuario
    print('Your score:', puntuación)
    #Ahora necesito que le preguntes al usuario si quiere seguir jugando o no
    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again == 'no':
        jugando = False
    
