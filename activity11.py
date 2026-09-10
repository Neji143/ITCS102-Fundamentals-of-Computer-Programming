#IF ELSE - getpass

import getpass

username = "D_ROSE"
password = "MYGOATDERICKROSE"

d = input("Input USERNAME: ")
r = getpass.getpass("Input PASSWORD: ")

    
if d == username and r == password: 
	print("WELCOME MVP")

else: 
	print("YOU AINT D ROSE")