import pandas as pd



class Modelle:
    def __init__(self, modell: str, kategorie: str, kundenwunsch: str=None, csv_speichern: bool): 
        # kundenwunsch bleibt None und somit in der Exception eine Option
        # modell und kategorie sind bindend und müssen für alle Modelle() gelten

        self.modell = modell
        # modell = Personenwaagen, Rollstuhlwagen, Postwaagen etc.

        # kategorie = Industrie, Haushalt, Medizin etc.        
        self.kategorie = kategorie

        # kundenwunsch = None, optional
        self.kundenwunsch = kundenwunsch
        
        # kein input = "Keine Angabe" - Noch nicht final
        if not kundenwunsch:
            self.kundenwunsch = "Keine Angabe"
        else:
            self.kundenwunsch = kundenwunsch


        # lets try: 

        if csv_speichern:
            self.csv_auslesen("auftraege.csv")

    # csv datei erstellen lassen, am besten bei jedem instanzieren der Klasse
    # Idee: Ein neues Modell wird erstellt und alle Daten kommen automatisch in eine csv datei

    def als_csv_speichern(self, csv_datei): # Testing
        import csv
        with open(csv_datei, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.modell, self.kategorie, self.kundenwunsch])


    def __str__(self):
        return f"Modell: {self.modell} - Kategorie: {self.kategorie} - Kundenwunsch: {self.kundenwunsch}"
    

    # csv umwandeln in ein pandas df. Weitere Verwendung offen..
    def csv_auslesen(csv_datei: str):
        df = pd.read_csv(csv_datei, encoding="utf-8")
        return df
    
    def kundenwunsch_anpassen():
        pass
    

postwaage = Modelle("postwaage", "industriewaage", "muss in rot sein")
print(postwaage)



kundenwunsch = input("Irgendwelche wünsche für ihre Personenwaage? ")


personenwaage = Modelle("Personenwaage", "Retail", kundenwunsch)
print(personenwaage)