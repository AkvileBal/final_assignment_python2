import sqlite3

conn = sqlite3.connect("saldainiai.db")
c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS saldainiu_sarasas (pavadinimas text, tipas text, kaina_uz_kg float, perkamas_kiekis integer, kaina float)""")

    c.execute("INSERT INTO saldainiu_sarasas VALUES ('Migle', 'sokoladiniai', 8.5, 4, 0)")
    c.execute("INSERT INTO saldainiu_sarasas VALUES ('Ananasiniai', 'vafliniai', 9, 5, 0)")
    c.execute("INSERT INTO saldainiu_sarasas VALUES ('Fortuna', 'vafliniai', 5, 1, 0)")
    c.execute("INSERT INTO saldainiu_sarasas VALUES ('Obelele', 'marmeladiniai', 3.5, 3, 0)")
    c.execute("INSERT INTO saldainiu_sarasas VALUES ('Vilnius', 'sokoladiniai', 10.7, 2, 0)")
    c.execute("INSERT INTO saldainiu_sarasas VALUES ('Sostine', 'sokoladiniai', 15.2, 6, 0)")
    c.execute("INSERT INTO saldainiu_sarasas VALUES ('Aguona', 'sokoladiniai', 7.6, 9, 0)")
    c.execute("INSERT INTO saldainiu_sarasas VALUES ('Pupa', 'sokoladiniai', 6.7, 6, 0)")
    c.execute("INSERT INTO saldainiu_sarasas VALUES ('Nomeda', 'vafliniai', 4.6, 10, 0)")
    c.execute("INSERT INTO saldainiu_sarasas VALUES ('Vezelis', 'karamele', 2.9, 3, 0)")

    c.execute("UPDATE saldainiu_sarasas SET kaina=kaina_uz_kg*perkamas_kiekis WHERE pavadinimas='Migle'")
    c.execute("UPDATE saldainiu_sarasas SET kaina=kaina_uz_kg*perkamas_kiekis WHERE pavadinimas='Ananasiniai'")
    c.execute("UPDATE saldainiu_sarasas SET kaina=kaina_uz_kg*perkamas_kiekis WHERE pavadinimas='Fortuna'")
    c.execute("UPDATE saldainiu_sarasas SET kaina=kaina_uz_kg*perkamas_kiekis WHERE pavadinimas='Obelele'")
    c.execute("UPDATE saldainiu_sarasas SET kaina=kaina_uz_kg*perkamas_kiekis WHERE pavadinimas='Vilnius'")
    c.execute("UPDATE saldainiu_sarasas SET kaina=kaina_uz_kg*perkamas_kiekis WHERE pavadinimas='Sostine'")
    c.execute("UPDATE saldainiu_sarasas SET kaina=kaina_uz_kg*perkamas_kiekis WHERE pavadinimas='Aguona'")
    c.execute("UPDATE saldainiu_sarasas SET kaina=kaina_uz_kg*perkamas_kiekis WHERE pavadinimas='Pupa'")
    c.execute("UPDATE saldainiu_sarasas SET kaina=kaina_uz_kg*perkamas_kiekis WHERE pavadinimas='Nomeda'")
    c.execute("UPDATE saldainiu_sarasas SET kaina=kaina_uz_kg*perkamas_kiekis WHERE pavadinimas='Vezelis'")

    print('Sokoladiniai saldainiai, kurių kg kainuoja daugiau nei 5 eur:')
    sarasas=c.execute("SELECT * From saldainiu_sarasas WHERE tipas ='sokoladiniai' and kaina > 5")
    for i in sarasas:
            print(i)

    pavadinimas1=input('Iveskite saldainiu pavadinima ir spauskite enter: ')
    tipas1=input('Iveskite saldainiu tipa ir spauskite enter: ')
    kaina_uz_kg1=float(input('Iveskite saldainiu kaina už kg ir spauskite enter: '))
    perkamas_kiekis1=int(input('Iveskite saldainiu perkama kieki ir spauskite enter: '))
    kaina1=kaina_uz_kg1*perkamas_kiekis1
    
    c.execute(f"INSERT INTO saldainiu_sarasas VALUES ('{pavadinimas1}', '{tipas1}', {kaina_uz_kg1}, {perkamas_kiekis1}, {kaina1})")
    c.execute(f"DELETE from saldainiu_sarasas WHERE pavadinimas='{pavadinimas1}'")   

duomenys = c.execute("SELECT * From saldainiu_sarasas").fetchall()
duomenys1=list(duomenys)
print(duomenys1)

with open('saldainiu_sarasas.csv', 'w') as failas: 
    failas.write(duomenys1)

import pandas as pd
from matplotlib import pyplot as plt

from csv import reader, writer
with open('saldainiu_sarasas.csv', 'w', newline='') as failas:
    csv_writer=writer(failas)
    csv_writer.writerow(['pavadinimas', 'tipas', 'kaina_uz_kg', 'perkamas_kiekis', 'kaina'])
    csv_writer.writerows(duomenys1)

sarasas = pd.read_csv('saldainiu_sarasas.csv')
print(sarasas)
sokolad = sarasas[sarasas.tipas == 'sokoladiniai']
vafl = sarasas[sarasas.tipas == 'vafliniai']

plt.plot(sokolad.kaina_uz_kg, sokolad.pavadinimas)
plt.plot(vafl.kaina, vafl.pavadinimas)
plt.legend(['Sokoladiniai', 'Vafliniai'])
plt.title("Saldainiu asortimentas ir kaina už kilograma")
plt.xlabel('Kilogramo kaina')
plt.ylabel('Saldainiu pavadinimas')
plt.show()    

from numpy import block
import seaborn as sns
sns.set_style("dark")
sns.barplot(data=sarasas, x="kaina", y="pavadinimas")
plt.title("Pirkimai")
plt.xlabel('Krepselio kaina')
plt.ylabel('Saldainiu pavadinimas')
plt.show()