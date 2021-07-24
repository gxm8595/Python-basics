import random
print("Welcome Gamer :) ")
def game():
    Hello = ["Stone", "Paper","Scissor:"]
    computer = random.choice(Hello)
    gamer = input("Enter \n    --Stone,Paper or Scissor")
    if gamer =="Stone" and computer  == "Stone":
        print("Computer: Stone\n Game Tied\n")
    elif gamer =="Paper" and computer  == "Stone":
        print("Computer: Stone\n You win\n")
    elif gamer =="Scissor" and computer  == "Stone":
        print("Computer: Stone\n You Loose\n")
    elif gamer =="Stone" and computer  == "Paper":
        print("Computer:Paper\n You Loose\n")
    elif gamer =="Paper" and computer  == "Paper":
        print("Computer: Paper\n Game Tied")
    elif gamer =="Scissor" and computer  == "Paper":
        print("Computer: Paper \n You win")
    elif gamer =="Paper" and computer  == "Scissor":
        print("Computer: Scissor\n You Loose\n")
    elif gamer =="Stone" and computer  == "Scissor":
        print("Computer: Scissor\n You win\n")
    elif gamer =="Scissor" and computer  == "Scissor":
        print("Computer: Scissor\n Game Tied\n")
    else:
        print("Invalid input")
game()