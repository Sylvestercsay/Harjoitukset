import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Tite360340',
         autocommit=True
         )






cursor = yhteys.cursor(dictionary=True)

def hae_tiedot(icao):

    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    tulos = cursor.fetchone()
    if tulos:
        return (tulos['latitude_deg'], tulos['longitude_deg'])
    return None

icao1 = input("Syötä ensim ICAO-koodi: ").upper()
icao2 = input("Syötä toinen ICAO-koodi: ").upper()

coords1 = hae_tiedot(icao1)
coords2 = hae_tiedot(icao2)

if coords1 and coords2:
    distance = geodesic(coords1, coords2).kilometers

    print(f"\nDistance between {icao1} and {icao2}:")
    print(f"{distance:.2f} kilometers")
else:
    if not coords1:
        print(f"Virhettä: {icao1} ei löytynyt tietokannasta.")
    if not coords2:
        print(f"virhettä: {icao2} ei löytynyt tietokannasta.")

yhteys.close()