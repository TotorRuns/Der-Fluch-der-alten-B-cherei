class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung
    
    def __str__ (self):
        return self.name
    
