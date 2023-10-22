import gegenstand
import sys
from colorama import init
import os
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
import time
encoding ='utf-8'
with open("names.txt", "r") as f:
    playerName = f.readline().strip()
    char1 = f.readline().strip()
    char2 = f.readline().strip()
    char3 = f.readline().strip()
    char4 = f.readline().strip()
    opfer = f.readline().strip()

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

time.sleep(2)
print (playerName + ": Ein alter Artikel ueber die Schließung der Bibliothek?")
time.sleep(2)
print (char2 + ": Das war eine schwere Zeit. Viele Buecher wurden vermisst, einschließlich... das verfluchte Buch.")
time.sleep(2)
print("Du hast nun die Moeglichkeit dich umzusehen. Du kannst SUCHEN und SPRECHEN.")

def suchen():
    print("Du hast Antonias Tagebucheintrag gefunden.")
    exec(open("antoniastagebuch.py").read())

while True:
    choice = input("Deine Wahl: ").lower()

    if choice == "suchen":
        suchen()
        break
    elif choice == "sprechen":
        # Hier sollte dein Code für "SPRECHEN" hinkommen.
        print(playerName + ": Also wurde die Bibliothek nur wegen dem Fluch geschlossen? Oder gab es andere Gruende?")
