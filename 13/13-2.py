from flask import Flask, request
import mysql.connector
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight',
         user='root',
         password='5995',
         autocommit=True
         )

app = Flask(__name__)


@app.route('/kenttä/<ICAO>')
def kenttä(ICAO):
    sql = "SELECT name, municipality FROM airport"
    x = " WHERE ident='" + ICAO + "'"
    kursori = yhteys.cursor()
    nimi = "SELECT name FROM airport"
    nimi += x
    kursori.execute(nimi)
    nimi = kursori.fetchall()
    paikka = "SELECT municipality FROM airport"
    paikka += x
    kursori.execute(paikka)
    paikka = kursori.fetchall()

    vastaus={
        "ICAO": ICAO, 
        "Name": nimi,
        "Municipality": paikka
    }

    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)