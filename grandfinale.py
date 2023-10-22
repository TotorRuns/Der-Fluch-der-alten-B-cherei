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

os.system('cls')

cprint(figlet_format('Kapitel 5: Das Finale'))

time.sleep(2)

print(playerName + ": Ich denke, ich habe es. Der Fluch, das verfluchte Buch, all diese Hinweise... es ist alles miteinander verbunden.")
time.sleep(2)

print(char4	+ ": Was muessen wir tun?")
time.sleep(2)
print(playerName + ": Wir muessen das Buch schließen. Aber es ist ein Risiko.")
time.sleep(2)
print(char1 + ": Ich werde es tun. Ich weiß, dass Gustav das gewollt haette.")
time.sleep(2)
print (playerName + ": Okay Frankiska, dann lass ich dich mal das Buch schließen. Aber sei vorsichtig.")
time.sleep(2)
print ("Franziska schließt das Buch und es scheint, als ob der Fluch gebrochen ist. Die Athmosphaere kehrt zur Normalitaet zurueck.")
time.sleep(2)
os.system("cls")
cprint(figlet_format('ENDE...?'))
time.sleep(5)
os.system('cls')
print ("Wir haben den Fluch gebrochen, aber wir haben noch eine Sache zu klaeren.")

while True:
    choice = input("Wer hat Gustav umgebracht? ")
    if choice == "Ludwig":
        break
    else:
        print("Ich bin mir sicher, dass es der nicht war.")

time.sleep(2)
print(playerName + ": Ludwig ich weiß, dass du es warst. Du musst dich stellen.\n Ich habe Beweise gefunden, die dich als Taeter entlarven. Du hast aucf mich nervoes gewirkt, als ich dich auf die Kaputte Brille und auf das Medallion angesprochen habe.")
time.sleep(2)
print(char2 + " : Was? Das ist absurd! Ich habe nichts damit zu tun!")
time.sleep(2)
print(playerName + ": Oh doch, Ludwig. Ich habe deinen Zettel gefunden, in dem du deine Plaene niedergeschrieben hast. Du wolltest Gustav loswerden, um an das wertvolle Buch zu gelangen.")
time.sleep(2)
print(char2 + ": Das ist eine Luege! Ihr koennt mir nichts beweisen!")
time.sleep(2)
print (playerName + ": Oh doch, Ludwig. Hier ist auch die Giftflasche, die du zum Toeten von Gustav verwendet hast.")
time.sleep(2)
print(char3 + "Verdammt! Ich gebe es zu! Ich habe Gustav ermordet, um an das Buch, welches Antonia jetzt hat, zu gelangen. Ich war verzweifelt und dachte, der Fluch wuerde mich reich machen. Aber ich bereue es zutiefst.")
time.sleep(2)
print ("Die Polizei wird gerufen und Ludwig wird verhaftet. Die Geschichte endet mit einem Gefuehl der Erleichterung und der Gerechtigkeit.")

cprint(figlet_format("ENDE"))
os.system('pause')