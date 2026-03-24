import customtkinter as ctk
from main import Modelle


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # interface einstellungen:
        self.title("Test: Meine Modelle Klasse in ctk einbinden")
        self.geometry("400x400")
        
        kundenwunsch = input("Sie wünschen? ")

        self.waage_ = Modelle("Rollstuhlwaage", "Haushalt", kundenwunsch)

        # just to fill the empty CTk window with some labelss and a button

        self.label_modell = ctk.CTkLabel(self, text=f"Modell: {self.waage_.modell}")
        self.label_modell.pack(pady=10)

        self.label_kategorie = ctk.CTkLabel(self, text=f"Kategorie: {self.waage_.kategorie}")
        self.label_kategorie.pack(pady=10)
        
        self.button = ctk.CTkButton(self, text="Info zeigen", command=self.show_details)
        self.button.pack(pady=10)

    def show_details(self):
        # Zugriff auf die Methode des instanziierten Objekts
        print(self.waage_.get_info())
