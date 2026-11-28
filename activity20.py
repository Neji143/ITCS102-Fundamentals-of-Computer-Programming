mcu_movies = []

isContinuing = True

while isContinuing:
    ans = input("Do you want to add a title of an mcu movie (y/n): ") == "y"
    if ans == True:
        title = input("Enter the title of an mcu movie: ")
        mcu_movies.append(title)
        print(mcu_movies)
      
    else:
        isContinuing = False
        print(mcu_movies)