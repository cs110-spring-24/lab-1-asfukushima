import random
cpu = random.randint(1, 3)

user = input("Enter rock paper or scissors: ")

if user == "rock":
	if cpu == 1: # cpu chose rock
		print("tie game.")
	elif cpu == 2: # cpu chose paper
		print("you lost.")
	else:
		print("you won.")

if user == "paper":
	if cpu == 1: # cpu chose rock
		print("you won.")
	elif cpu == 2: # cpu chose paper
		print("tie game.")
	else:
		print("you lost.")

if user == "scissors":
	if cpu == 1: # cpu chose rock
		print("you lost.")
	elif cpu == 2: # cpu chose paper
		print("you won.")
	else:
		print("tie game.")







