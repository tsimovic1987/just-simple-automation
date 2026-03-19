import pandas as pd



class Modelle:
    def __init__(self, modell: str, kategorie: str, kundenwunsch: str=None): 
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



    def __str__(self):
        return f"Modell: {self.modell} - Kategorie: {self.kategorie} - Kundenwunsch: {self.kundenwunsch}"
    

    # csv ist für Zukunft geplant, aber nicht sicher ob es am final benötigt wird
    def csv_auslesen(csv_datei: str):
        df = pd.read_csv(csv_datei, encoding="utf-8")
        return df # nur als Platzhalter gedacht!
    
    def kundenwunsch_anpassen():
        pass
    

postwaage = Modelle("postwaage", "industriewaage", "muss in rot sein")
print(postwaage)



kundenwunsch = input("Irgendwelche wünsche für ihre Personenwaage? ")


personenwaage = Modelle("Personenwaage", "Retail", kundenwunsch)
print(personenwaage)