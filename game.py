number = 20
number_of_guesses = 1
play_again = True
# 𝟬 𝟭 𝟮 𝟯 𝟰 𝟱 𝟲 𝟳 𝟴 𝟵 -- here is numbers you can copy and paste in line 7
#and update your code
while play_again:
    print("You can try 𝟱 times:")
    while number_of_guesses <= 5:
        guess_number = int(input("Guess the number: "))
        
        if guess_number < number:
            print("You entered a smaller number. Please input a greater number.\n")
        elif guess_number > number:
            print("You entered a greater number. Please input a smaller number.\n")
        else:
            print("Congratulations!! you win 😇 \n")
            print("Number of guesses it took:", number_of_guesses)
            print("Your score is", 6 - number_of_guesses, "out of 5 😎")
            break
        print("Number of guesses left:", 5 - number_of_guesses)
        number_of_guesses += 1

    if number_of_guesses > 5:
        print("Opps!! Game Over 😢")

    play_again=input("Once again? (y/n): ").lower()
    if play_again == "y":

     number_of_guesses = 1 

    elif play_again == "n":
         print("Thank you for playing! 🙂 ")
         break

    else:
       print("""You should type either 'y' or 'n'.Okay, see you next time..🙂""")
       break
    
    # -- another way
    #play_again = input("Once again? (y/n): ")
    #if play_again == "y":
     #number_of_guesses = 1

    #-- another way
    #play_again=input("Once again? (y/n): ").lower() == "y"
    #number_of_guesses = 1

#print("Thank you for playing!")
