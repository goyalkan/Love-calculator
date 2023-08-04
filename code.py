print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name11 = name1.lower()
name22 = name2.lower()

T  = int(name11.count("t") + name22.count("t"))
R = int(name11.count("r") + name22.count("r"))
U = int(name11.count("u")+ name22.count("u"))
E = int(name11.count("e") + name22.count("e"))

L = int(name11.count("l")+ name22.count("l"))
O = int(name11.count("o")+ name22.count("o"))
V = int(name11.count("v") + name22.count("v"))
E = int(name11.count("e") + name22.count("e"))

true = int(T+R+U+E)
love = int(L+O+V+E)

yes = str(true)
Love = str(love)

score = (yes + Love)

if int(score)<10 or int(score)>90:
    print(f"Your score is {score} , you go together like coke and mentos.")
elif  40<int(score)<50:
    print(f"Your score is {score} , you are alright together.")

else:
    print(f"Your score is {score}.")





