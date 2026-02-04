import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Tite360340',
         autocommit=True
         )




cursor = yhteys.cursor(dictionary=True)

icao = input("syötä ICAO-koodi (e.g., EFHK): ").upper()

kysely = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(kysely, (icao,))

tulos = cursor.fetchone()

if tulos:
    print(f"Airport: {tulos['name']}")
    print(f"Municipality: {tulos['municipality']}")
else:
    print("Tuloksia ei löytynyt.")

yhteys.close()