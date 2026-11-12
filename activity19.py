#act19

import getpass

loginattempt = 0

username = "NEILLPOGI"
password = "NEILL1234"

while True:
    user = input("Username: --> ")
    passw = input("Password: --> ")

    if user == username and passw == password:
        print("Login Successfully...")
        print("Login Attempts: ", loginattempt)
        break
    else:
        print("Login Unsuccessfully...")
        loginattempt = loginattempt + 1