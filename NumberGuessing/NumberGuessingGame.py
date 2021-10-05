import random   
input("First Choose your Range for Number guessing\nlike 1 to 20\nEnter To Start Game For Number Guess ")
lower_range =int(input("Enter Your Lower Range To Start Guessing Game: \n"))
upper_range =int(input("Enter Your Upper Range To Start Guessing Game: \n"))

ran_num = random.randint(lower_range,upper_range) 
#print(ran_num) To print Random Number For Debugging Purpose. 
'''
Random : import random for generate random number between Lower Range TO Upper Range
Input  : input Fucntion for take user input
Lower Range : Lower Range for randomly Generated Number
Upper Range : Upper Range For Randomly Generated Number
ran_num = Random Number Generated In Saved In ran_num Variable for Check With User Input
'''

num = int(input("Please Enter Your Guess Number :\n"))
while True:
	if num == ran_num:         # Checking User Input with Random Generated Number
		print("You Guess Right Number")
		break
	else:
		print("Your Guess Was Wrong")   # if ran_num was not same as User Input.
		break
print("The Real Number Was {}".format (ran_num))   # To Print The Random Generated Number . 
