ex_name  = "" 

n = str(input("What's the name of your ex? -->"))
ex_name = n + ", "

e = str(input("Who else? --> "))
ex_name += e + ", "

h = str(input("Who else? --> "))
ex_name += h + ","

print("Your exes name are {" , ex_name, "}")