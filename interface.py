import customtkinter as ctk
from main import Models


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # interface einstellungen:
        self.title("Test: Meine Modelle Klasse in ctk einbinden")
        self.geometry("400x400")
        
        kundenwunsch = input("Special Order? ")

        self.scale = Models("Rollstuhlwaage", "Haushalt", kundenwunsch)

        # just to fill the empty CTk window with some labelss and a button

        self.label_model = ctk.CTkLabel(self, text=f"Modell: {self.scale.model}")
        self.label_model.pack(pady=10)

        self.label_category = ctk.CTkLabel(self, text=f"Kategorie: {self.scale.category}")
        self.label_category.pack(pady=10)
        
        self.button = ctk.CTkButton(self, text="Info zeigen", command=self.show_details)
        self.button.pack(pady=10)

    def show_details(self):
        # Zugriff auf die Methode des instanziierten Objekts
        print(self.scale.get_info())
