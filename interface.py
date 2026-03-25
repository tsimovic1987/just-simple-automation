import customtkinter as ctk
from models import Models


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Test: Meine Modelle Klasse in ctk einbinden")
        self.geometry("400x400")

        self.scale = Models("Rollstuhlwaage", "Haushalt")

        self.label_model = ctk.CTkLabel(self, text=f"Modell: {self.scale.model}")
        self.label_model.pack(pady=10)

        self.label_category = ctk.CTkLabel(self, text=f"Kategorie: {self.scale.category}")
        self.label_category.pack(pady=10)
