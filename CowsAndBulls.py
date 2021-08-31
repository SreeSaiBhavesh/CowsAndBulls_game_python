import random

def CowAndBulls():
    turns = int(input("Enter the number of attempts you want to take: "))
    digits = '123456789'
    size = 4
    num = ''.join(random.sample(digits,size))
    random_number = list(num)
    print("Guess a 4 - digit number: ")
    j=0
    while(turns!=0):
        data = int(input())
        UserInput = list(str(data))
        
        if len(UserInput) != size:
            print("Enter a valid 4-digit number, eg:1234")
                
        else:
            j+=1
            cow=0
            bull=0
            for i in range(len(UserInput)):
                if UserInput[i] == random_number[i]:
                    cow+=1
                                            
            if UserInput[0] == random_number[1] or UserInput[0] == random_number[2] or UserInput[0] == random_number[3]:
                bull+=1
            if UserInput[1] == random_number[0] or UserInput[1] == random_number[2] or UserInput[1] == random_number[3]:
                bull+=1
            if UserInput[2] == random_number[0] or UserInput[2] == random_number[1] or UserInput[2] == random_number[3]:
                bull+=1
            if UserInput[3] == random_number[1] or UserInput[3] == random_number[2] or UserInput[3] == random_number[0]:
                bull+=1

                                       
            if(cow==4):
                print("You won")
                print("You have found word in attempts: ",j)
                break
            elif cow==0 and bull==0:
                print("Bullshit")
                turns=turns-1
            elif cow!=0 or bull!=0:
                print("No of Cows:",cow)
                print("No of Bulls:",bull)
                turns=turns-1
                if(turns==0):
                    print("Sorry! you are unable to find the word")
                    print("Actual number is",num)

            
                  
name = input("Enter Your Name: ")
print("Welcome to the Cow and Bull game, Mr.",name)
print("..............................................")
print("Try to guess the correct number")
CowAndBulls()
