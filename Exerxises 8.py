import mysql.connector

"""""
1. Write a program that asks the user to enter the ICAO code of an airport.
The program fetches and prints out the corresponding airport name and location (town)
from the airport database used on this course.
The ICAO codes are stored in the ident column of the airport table.
"""


db_connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="1234",
    autocommit=True
)

def find_airport(ICAO):
    sql = "SELECT name,municipality FROM airport WHERE ident='" + ICAO +"'"
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    query_result = db_cursor.fetchall()
    if db_cursor.rowcount > 0:
        for tbl_row in query_result:
            print(f"Airport name is {tbl_row[0]} and the location:{tbl_row[1]}")


ICAO = input("Give the ICAO code:")
find_airport(ICAO)
print("These employees have better salary than their bosses:")

"""""
2. Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that 
country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.
"""""
def find_airport_ordered(area_code):
    sql = "select name, type from airport where iso_country ='" + area_code + "' order by type desc;"
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    query_result = db_cursor.fetchall()
    if db_cursor.rowcount > 0:
        for tbl_row in query_result:
            print(f"Airport name: {tbl_row[0]}, type: {tbl_row[1]}")
area_code = input("Give the ICAO code:")
find_airport_ordered(area_code)