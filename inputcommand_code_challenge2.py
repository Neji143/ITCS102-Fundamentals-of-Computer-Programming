money = input("How much money do you want to deposit? ")
print("You deposited" + " " + money)
print()

total = int(money)
print("Since you deposited", total, "this is the breakdown of the money in different denominations")
print()
total = int(money)
#Money to deposit 
a = total//1000
total = total - a*1000
b = total//500
total = total - b*500
c = total//200
total = total -  c*200
d = total//100
total = total - d*100
e = total//50
total = total - e*50
f = total//20
total = total - f*20
g = total//10
total = total - g*10
h = total//5
total = total - h*5
i = total//1
total = total - i*1

print("There are ", a, ", 1000's")
print("There are ", b, ", 500's")
print("There are ", c, ", 200's")
print("There are ", d, ", 100's")
print("There are ", e, ", 50's")
print("There are ", f, ", 20's")
print("There are ", g, ", 10's")
print("There are ", h, ", 5's")
print("There are ", i, ", 1's")

