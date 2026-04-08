import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metropolia',
    autocommit=True
)

@app.route("/airport/<icao>")
def get_airport(icao):
    kursori = yhteys.cursor()

    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao,))

    row = kursori.fetchone()

    if row is None:
        return jsonify({"error": "Airport not found"}), 404

    return jsonify({
        "ICAO": icao,
        "Name": row[0],
        "Location": row[1]
    })

if __name__ == "__main__":
    app.run(debug=True)