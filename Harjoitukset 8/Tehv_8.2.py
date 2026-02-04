import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Tite360340',
         autocommit=True
         )




icao_code = input("Syötä lentokentän ICAO-koodi: ").upper()


cursor = yhteys.cursor()


sql = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(sql, (icao_code,))


tulos = cursor.fetchone()

if tulos:
    print(f"Airport Name: {tulos[0]}")
    print(f"Location: {tulos[1]}")
else:
    print("Lentoasema ei löytynyt. Tarkista ICAO-koodi.")


yhteys.close()