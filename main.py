# in future i'll use english comments on my files!

import pandas as pd
import csv

class Modelle:
    def __init__(self, modell: str, kategorie: str, kundenwunsch: str=None, csv_speichern: bool=None): 
        # kundenwunsch bleibt None und somit in der Exception eine Option
        # modell und kategorie sind bindend und müssen für alle Modelle() gelten

        self.modell = modell
        # modell = Personenwaagen, Rollstuhlwagen, Postwaagen etc.

        # kategorie = Industrie, Haushalt, Medizin etc.        
        self.kategorie = kategorie

        # kein input = "Keine Angabe" - Noch nicht final
        if not kundenwunsch:
            self.kundenwunsch = "Keine Angabe"
        else:
            self.kundenwunsch = kundenwunsch

        if csv_speichern:
            self.als_csv_speichern("auftraege.csv")

    def als_csv_speichern(self, csv_datei): 
        with open(csv_datei, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([self.modell, self.kategorie, self.kundenwunsch])

    def __str__(self):
        return f"Modell: {self.modell} - Kategorie: {self.kategorie} - Kundenwunsch: {self.kundenwunsch}"

    @staticmethod
    def csv_auslesen(csv_datei: str):
        df = pd.read_csv(csv_datei, encoding="utf-8")
        return df
    
    def kundenwunsch_anpassen(self):
        pass

    def get_info(self):
        return self.__str__()
