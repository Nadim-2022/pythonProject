"""One talent is 20 pounds.
One pound is 32 lots.
One lot is 13.3 grams."""


t = float(input( "Enter a mass in talents ?"))
p = float(input("Enter a mass in Pounds ?"))
l = float(input("Enter a mass in lots ?"))
talent = float(t)*20*32*13.3
pound = float(p)*32*13.3
lot = float(l)*13.3
wight = int(talent+pound+lot)//1000
g = int(wight)
g%=1000
print(f"The weight in modern units:  " + str(wight))
print(g)

