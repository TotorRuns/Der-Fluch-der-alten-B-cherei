import gegenstand
import sys
from colorama import init
import os
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
encoding ='utf-8'
import time
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
print (playerName + ": Was hat Antonia geschrieben?")
time.sleep(2)
print (char4 + ": *mit Traenen in den Augen* Ich wokkte nur meine Schwester zurueck. Ich dachte das Buch koennte mir helfen.")
time.sleep(2)
print ("Du suchst in einen von Franziskas Buechern und findest eine handgeschriebene Notiz von ihr.")
time.sleep(2)
print (playerName + ": Franziska wusste von den Fluch!")
time.sleep(2)
print (char1 + ": Ja, ich habe es gewusst. Aber ich dachte, es waere nur ein Maerchen.")
time.sleep(2)
print ("Du durchsuchst das Tagebuch von Viktor, welches du per Zufall auf einen Tisch gefunden hast. Neben einen Eintrag von Viktor findest du einen Zettel mit Ludwigs Handschrift.")
time.sleep(2)
print (playerName + ": Was ist hier drin?")
time.sleep(2)
print (char3 + ": Ja, ich wollte das Buch stehlen. Ich brauchte das Geld. Aber ich habe " + opfer + " nicht umgebracht.")
time.sleep(2)

exec(open("grandfinale.py").read())