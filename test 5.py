import mysql.connector
import geopy
from geopy.distance import geodesic
import random
import time
from time import sleep
import sys
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

def get_country():
    sql = "SELECT country.name FROM country, airport WHERE airport.iso_country = country.iso_country and country.continent like '%EU%' ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]
def get_heliport(country):
    sql = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country and country.name ='" + country + "' and airport.type like '%heliport' ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:
        print('This country does not exist, try again.')
        return None
    if cursor.rowcount > 0:
        for row in result:
            return row[0]
def get_location(heliport):  # returns long/lat of an airport
    location = []
    sql = "SELECT longitude_deg, latitude_deg FROM airport WHERE airport.ident ='" + heliport + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            location.append(int(row[1]))
            location.append(int(row[0]))
        return location
def get_continent(country):  # returns continent
    sql = "SELECT country.continent FROM country WHERE country.name ='" + country + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]
def get_weather():
    weather = []
    sql = "SELECT NAME FROM goal ORDER BY NAME DESC limit 5"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            weather.append(result)
            return weather


print(get_weather())

rounds = 1
score = 0
score1 = 0
score2 = 0
while round !=2:
    alive = True
    budget = 1000
    cost = 200

    current_country = get_country()
    current_continent = (get_continent(current_country))

    destination = None
    current_heliport = None
    recent_heliport = ""

    while alive:
        if budget <= 0:
            print("You are run out of money, You can not travel more. ")
            alive = False
            break
        while budget > 0 and alive:

            recent_country = current_country

            if recent_country != "":
                print(f"Your are currently in {recent_country} at {get_heliport(recent_country)} in {get_continent(recent_country)}. \nYour budget is {budget} & you have to travel 3 country in minimum cost\n Every time it will cost €200 to travel. ")
                recent_heliport = ""
                destination = input("Enter the country you want to travel: ")

                destination_heliport = get_heliport(destination)

                while destination_heliport is None:

                    destination = input("Enter the country you want to travel: ")
                    destination_heliport = get_heliport(destination)

                else:
                    print("Choose 1 rout from below:\n1. route one\n2. route two\n3. route three")
                    path = int(input("Enter the path you want to go: "))
                    random = random.randint(1,3)
                    print(random)
                    if path == 1:
                        if random == 1:
                            print("You caught by police because you do not have visa, now you have two option\n1.try to pay bribe\nor\n2.get ready to be deported  ")
                            option = int(input("What will you do? (1 or 2): "))
                            if option == 1:
                                print("Police release you for 100€......Enjoy your next flight")
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(100 + cost)
                                print(f"Welcome to the  {destination}, You traveled {distance:1f} kilometers and you paid {(cost+100)}")
                            else:
                                recent_heliport += current_heliport
                                destination_heliport = get_heliport(destination)
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(cost*2)
                                print(f"Welcome back to the {recent_country}, it cost you {int(cost*2)}")
                        else:
                            distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                            budget -=int(cost)
                            current_country = destination
                            print(f"You safely escaped from {recent_country}, You traveled {distance:.1f} kilometers and it cost you {cost}")

                    if path == 2:
                        if random == 3:
                            print("You caught by police because you do not have visa, now you have two option\n1.try to pay bribe\nor\n2.get ready to be deported  ")
                            option = int(input("What will you do? (1 or 2): "))
                            if option == 1:
                                print("Police release you for 100€......Enjoy your next flight")
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(100 + cost)
                                print(f"Welcome to the  {destination}, You traveled {distance:1f} kilometers and you paid {(cost + 100)}")
                            else:
                                recent_heliport += current_heliport
                                destination_heliport = get_heliport(destination)
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(cost*2)
                                print(f"Welcome back to the {recent_country}, it cost you {int(cost*2)}")


                        else:
                            distance = geodesic(get_location(current_heliport), get_location(destination_heliport))
                            budget -=int(cost)
                            current_country = destination
                            print(f"You safely escaped from {recent_country}, You traveled {distance:.1f} kilometers and it cost you {cost}")

                    if path == 3:
                        if random ==1:
                            distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                            current_country = destination
                            print(f"You safely escaped from {recent_country}, You traveled {distance:.1f} kilometers and it cost you {cost}")

                        if random == 2:
                            print("You caught by police because you do not have visa, now you have two option\n1.try to pay bribe\nor\n2.get ready to be deported  ")
                            option = int(input("What will you do? (1 or 2): "))
                            if option == 1:
                                print("Police release you for 100€......Enjoy your next flight")
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(100 + cost)
                                print(f"Welcome to the  {destination}, You traveled {distance:1f} kilometers and you paid {(cost + 100)}")
                            else:
                                recent_heliport += current_heliport
                                destination_heliport = get_heliport(destination)
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(cost*2)
                                print(f"Welcome back to the {recent_country}, it cost you {int(cost*2)}")

                        if random == 3:
                            distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                            budget -= int(cost*2)
                            current_country = destination
                            print(f"You safely escaped from {recent_country}, You traveled {distance:.1f} kilometers and it cost you {int(cost*2)}")

            else:

                current_heliport = get_heliport(current_country)
                print(f"You are currently in {current_country} at {current_heliport} in {get_continent(current_country)}.\n your current budget is {budget}. You have to travel 3 country")
                destination = input("Enter the country you wish to travel to: ")
                destination_heliport = get_heliport(destination)

                while destination_heliport is None:

                    destination = input("Enter the country you want to travel: ")
                    destination_heliport = get_heliport(destination)

                else:
                    random = random.randint(1,3)
                    print(f"2{random}")
                    if path == 1:
                        if random == 1:
                            print("You caught by police because you do not have visa, now you have two option\n1.try to pay bribe\nor\n2.get ready to be deported  ")
                            option = int(input("What will you do? (1 or 2): "))
                            if option == 1:
                                print("Police release you for 100€......Enjoy your next flight")
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(100 + cost)
                                print(f"Welcome to the  {destination}, You traveled {distance:1f} kilometers and you paid {(cost+100)}")
                            else:
                                recent_heliport += current_heliport
                                destination_heliport = get_heliport(destination)
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(cost*2)
                                print(f"Welcome back to the {recent_country}, it cost you {int(cost*2)}")
                        else:
                            distance = geodesic(get_location(current_heliport), get_location(destination_heliport))
                            budget -=int(cost)
                            current_country = destination
                            print(f"You safely escaped from {recent_country}, You traveled {distance:.1f} kilometers and it cost you {cost}")

                    if path == 2:
                        if random == 3:
                            print("You caught by police because you do not have visa, now you have two option\n1.try to pay bribe\nor\n2.get ready to be deported  ")
                            option = int(input("What will you do? (1 or 2): "))
                            if option == 1:
                                print("Police release you for 100€......Enjoy your next flight")
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(100 + cost)
                                print(f"Welcome to the  {destination}, You traveled {distance:1f} kilometers and you paid {(cost + 100)}")
                            else:
                                recent_heliport += current_heliport
                                destination_heliport = get_heliport(destination)
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(cost*2)
                                print(f"Welcome back to the {recent_country}, it cost you {int(cost*2)}")


                        else:
                            distance = geodesic(get_location(current_heliport), get_location(destination_heliport))
                            budget -=int(cost)
                            current_country = destination
                            print(f"You safely escaped from {recent_country}, You traveled {distance:.1f} kilometers and it cost you {cost}")

                    if path == 3:
                        if random ==1:
                            distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                            budget -= int(cost)
                            current_country = destination
                            print(f"You safely escaped from {recent_country}, You traveled {distance:.1f} kilometers and it cost you {cost}")

                        if random == 2:
                            print("You caught by police because you do not have visa, now you have two option\n1.try to pay bribe\nor\n2.get ready to be deported  ")
                            option = int(input("What will you do? (1 or 2): "))
                            if option == 1:
                                print("Police release you for 100€......Enjoy your next flight")
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(100 + cost)
                                print(f"Welcome to the  {destination}, You traveled {distance:1f} kilometers and you paid {(cost + 100)}")
                            else:
                                recent_heliport += current_heliport
                                destination_heliport = get_heliport(destination)
                                distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                                budget -= int(cost*2)
                                print(f"Welcome back to the {recent_country}, it cost you {int(cost*2)}")

                        if random == 3:
                            distance = geodesic(get_location(current_heliport),get_location(destination_heliport))
                            budget -= int(cost*2)
                            current_country = destination
                            print(f"You safely escaped from {recent_country}, You traveled {distance:.1f} kilometers and it cost you {int(cost*2)}")






















