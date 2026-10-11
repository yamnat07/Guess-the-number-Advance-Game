import random
from datetime import datetime
def difficulty():
    print("~"*28)
    print("WELCOME TO GUESS THE NUMBER")
    print("~"*28)
    print("Do you have enough guts to guess my secret number?")
    print("If YES! Then Good Luck\n")
    while True:
        print("="*20)
        print("Choose Difficulty")
        print("="*20)
        print("1.Easy(Numbers From 1 to 50)")
        print("2.Normal(Numbers From 1 to 100)")
        print("3.Hardcore(Numbers From 1 to 500)")
        print("4.Professional(Numbers From 1 to 1000)\n")
        print("Enter your choice in [1,2,3,4] only!")
        diff=input("Enter the difficulty:")
        if diff=="1":
            print("You have chosen Easy Difficulty!")
            return 50
        elif diff=="2":
            print("You have chosen Normal Difficulty!")
            return 100
        elif diff=="3":
            print("You have chosen Hardcore Difficulty!")
            return 500
        elif diff=="4":
            print("You have chosen Professional Difficulty!")
            return 1000
        else:
            print("Enter a valid number as a choice!")
con_num=difficulty()
secret_num=random.randint(1,con_num)
attempts=0
def guess_it(con_num,secret_num):
    print("="*20)
    print("GUESS THE NUMBER")
    print("="*20)
    print("I have chosen a number, can you guess it?")
    global attempts
    while True:   
        try:
            your_guess=int(input("Enter your Guess: "))
            if your_guess<1 or your_guess>con_num:
                print(f"Enter a number from 1 to {con_num}.")
                continue       
            if your_guess>secret_num:
                print("Too High! Try a smaller number.")
                attempts+=1
            elif your_guess<secret_num:
                print("Too Low! Try a higher number.")
                attempts+=1
            else:
                attempts+=1
                print("Congratulations!!! You Guessed the right number.")
                print(f"Correct number:{secret_num}")
                print("===RESULTS===")
                print(f"Total Attempts:{attempts}")
                break
        except ValueError:
            print("Enter a number.")

def save(con_num):
    global attempts
    while True:
        print("~"*20)
        print("===SAVING===")
        print("~"*20)
        print("1.Save Your Score.")
        print("2.Don`t Save.")
        permi=input("Enter your choice:")
        if permi.strip()=="1":
            now=datetime.now()
            date=now.strftime("%d-%m-%Y")
            time=now.strftime("%I:%M:%S %p")
            name=input("Enter Player name: ")
            A=attempts
            if con_num==50:
                Diff="Easy"
                with open("scores.txt","a") as file:
                    file.write(f"Date:{date}\nTime:{time}\nPlayer Name:{name}\nAttempts:{A}\nDifficulty:{Diff}\n\n")
                    print("Saving Complete.")
                    break
            elif con_num==100:
                Diff="Normal"
                with open("scores.txt","a") as file:
                    file.write(f"Date:{date}\nTime:{time}\nPlayer Name:{name}\nAttempts:{A}\nDifficulty:{Diff}\n\n")
                    print("Saving Complete.")
                    break
            elif con_num==500:
                Diff="Hardcore"
                with open("scores.txt","a") as file:
                    file.write(f"Date:{date}\nTime:{time}\nPlayer Name:{name}\nAttempts:{A}\nDifficulty:{Diff}\n\n")
                    print("Saving Complete.")
                    break
            elif con_num==1000:
                Diff="Professional"
                with open("scores.txt","a") as file:
                    file.write(f"Date:{date}\nTime:{time}\nPlayer Name:{name}\nAttempts:{A}\nDifficulty:{Diff}\n\n")
                    print("Saving Complete.")
                    break
        elif permi.strip()=="2":
            print("Thanks for playing!")
            break
        else:
            print("Please enter a number as stated above!")  

    
def main():
    con_num
    guess_it(con_num,secret_num)
    save(con_num)
    global attempts
    attempts=0
    while True:
        print("1.Play again/Beat your score.")
        print("2.Exit.")
        try:
            choice=int(input("Enter your choice: "))
            if choice==1:
                con_num2=difficulty()
                secret_num2=random.randint(1,con_num2)
                guess_it(con_num2,secret_num2)
                save(con_num2)
                attempts=0                        
            elif choice==2:
                print("Thanks For Playing!Hope you beat your score next time.")
                break
            else:
                print("Enter a valid choice!!!!")
        except ValueError:
            print("Enter a valid number!!")
main()