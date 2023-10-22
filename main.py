import sys
import gegenstand
import os

from colorama import init
import time
import locale
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
char1 = "Franziska"
char2 = "Ludwig"
char3 = "Viktor"
char4 = "Antonia"
opfer = "Gustav"

fotographie = gegenstand.Gegenstand("Fotographie von " + char2 +  "und " + char3, "Ein altes Foto, auf dem die beiden lachend in der Bücherei stehen. Es deutet auf eine tiefe Freundschaft oder mögliche Verbindung zwischen ihnen hin.")
verfluchtes_Buch = gegenstand.Gegenstand("Verfluchtes Buch", "Ist mit den Worten KLAATU BARADA NIKTO beschriftet.")
medallion = gegenstand.Gegenstand("Mysteriöses Medallion","Ein Medaillon, das ein Bild von Viktor und einer unbekannten Frau zeigt. Auf der Rückseite steht 'Für immer Dein.'")
brief = gegenstand.Gegenstand("Brief von Gustav an Franziska", "Ein unversendeter Liebesbrief, in dem Gustav seine Gefühle für Franziska offenbart.")
gift = gegenstand.Gegenstand("Giftfläschchen", "Ein kleines Fläschchen mit einem unbekannten Gift. Ein Geruch, der darauf hindeutet, dass es kürzlich geöffnet wurde.")
brille_kaputt = gegenstand.Gegenstand("Gebrochene Brille", "Eine zerbrochene Brille, die Ludwig gehört. Es gibt Anzeichen eines Kampfes.")
taschentuch = gegenstand.Gegenstand("Viktors Taschenbuch", "Enthält Notizen über das verfluchte Buch und wie man seinen Fluch nutzt.")
zeitungsartikel = gegenstand.Gegenstand("Zeitungsartikel", "Ein alter Artikel, der die Schließung der Bücherei und das Verschwinden eines wertvollen Buches dokumentiert.")
tagebucheintrag = gegenstand.Gegenstand("Tageeinbucheintrag von Antonia", "Sie schreibt über ihre Besessenheit von dem verfluchten Fluch und wie sie glaubt, dass es ihr helfen könnte, ihre kürzliche verstorbene Schwester zurückzufinden.")
notizen = gegenstand.Gegenstand("Handgeschriebene Notizen von Franziska", "Sie hat Recherchen über das verfluchte Buch durchgeführt und warnt davor, seine Worte auszusprechen.")

encoding ='utf-8'


print("Disclaimer: Alle Aehnlichkeiten zu TV-Serien bzw. Spielen sind ungewollt")

cprint(figlet_format('Der Fluch der alten Bibliothek!'))


playerName = input("Wie soll der Detektiv heißen? ")

with open("names.txt", "w") as f:
        f.write(playerName + "\n")
        f.write(char1 + "\n")
        f.write(char2 + "\n")
        f.write(char3 + "\n")
        f.write(char4 + "\n")
        f.write(opfer + "\n")
       

os.system('cls')

cprint(figlet_format('Kapitel 1: Ankunft in der Bücherei'))
time.sleep(2)

print ("Wir sind in einer alten Bibliothek. " + char1 + ", " + char2 + " und " + char3 + " sind auch da und wissen noch nicht was alles passiert.")
time.sleep(2)
print (playerName +": Diese Buecherei ist beeindruckend! Wo fange ich nur an?")
time.sleep(2)
print (char1 + ": Hier sind so viele seltene Buecher. Wie koennten Monate damit verbringen, alles durchzugehen.")
time.sleep(2)
print("Du hast nun die Moeglichkeit dich umzusehen. Du kannst SUCHEN und SPRECHEN.")


def suchen():
    print("Du findest ein Foto von " + opfer + " und " + char2)
    exec(open('gustavundludwig.py').read())

while True:
    choice = input("Deine Wahl: ")
    if choice == "SUCHEN" or choice == "suchen":
        suchen()
        break
    elif choice == "SPRECHEN" or choice == "sprechen":
        print(char2 + ": Ich war hier frueher Bibliothekar")




#print("Hallo " + playerName)