from flask import Flask, Blueprint, request, Response, render_template, Markup
import calendar, datetime, time
from datetime import date
import random

app = Flask(__name__)

@app.route('/oppija/<name>', methods=['GET'])
def app_name(name):
    kurssit = ["Docker", "Jenkins", "Vagrant"]
    verkkokurssit = ["GIT", "Linux", "RESTful API"]
    tyoviikko = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
    kuukauded = ["Tammikuulle", "Helmikuulle", "Maalliskuulle", "Huhtikuulle", "Toukokuulle", "Kesäkuulle", "Heinäkuulle", "Elokuulle", "Syyskuulle", "Marraskuulle", "Joulukuulle"]
    tanaan = date.today()
    vuo = int(tanaan.strftime("%Y"))
    kuu = tanaan.strftime("%m")

    if kuu.startswith("0"):
        kuu = int(kuu[1])
    else:
        kuu = int(kuu)

    kal = calendar.monthcalendar(vuo, kuu)
    
    #Muodostetaan lukujärjestyksen HTML-taulukon
    lukuhtml = "<table><tr><th>pvm</th><th>vkpv</th><th>Aihe</th></tr>"
    for viikko in kal:
        i = 0
        for paiva in viikko:
            if paiva > 0:
                sattu = random.randrange(len(kurssit))
                aihe = kurssit[sattu]
                if i <= 4:
                    lukuhtml = lukuhtml + "<tr><td>" + str(paiva) + "</td><td>" + tyoviikko[i] + "</td><td>" + aihe + "</td><td><button type = \"button\" onclick = \"alert('TUUT!')\">EN TUU</button></td></tr>" 
                    # print(str(paiva) + " >> " + tyoviikko[i] + " >> " + aihe)
                # else:
                #     print(str(paiva) + " >> " + tyoviikko[i] + " >> " + "---")
            i = i + 1

    lukuhtml = Markup(lukuhtml + "</table>")

    # Muodostataan verkkokurssien HTML-taulukon
    verkkohtml = "<table><tr><th> # </th><th>Nimi</th><th>Aloittamatta</th><th>Kesken</th><th>Valmis</th></tr>"
    i = 0
    for kurssi in verkkokurssit:
        verkkohtml = verkkohtml + "<tr><td>" + str(i+1) + "</td><td>" + kurssi + "</td><td>" + "<td><input type=\"radio\" name=\"verkkovaihe\" value=\"aloittamatta\"></td><td><input type=\"radio\" name=\"verkkovaihe\" value=\"kesken\"></td><td><input type=\"radio\" name=\"verkkovaihe\" value=\"valmis\"></td></tr>"
        i = i + 1

    verkkohtml = Markup(verkkohtml + "</table><br><button type = \"button\" onclick = \"alert('Tee enemmän!!')\">Submit</button>")

    return render_template('cal.html', name = name.title(), kuukauded=kuukauded[kuu-1], lukuhtml=lukuhtml, verkkohtml=verkkohtml)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)