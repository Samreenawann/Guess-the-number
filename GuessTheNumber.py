import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a!=n):
    a = int(input("Enter a number: "))

    if(n>a):
        print("Try a Greater number: ")
        guesses +=1
    elif(n<a):
        print("Try a smaller number: ")
        guesses +=1

    
print(f"The actual number is {n} which you guess in {guesses} attempts")

