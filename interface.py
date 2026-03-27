import customtkinter as ctk
from models import PostOfficeScale


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Trying out CTk for my models GUI")
        self.geometry("400x400")

        # Test Class
        self.scale = PostOfficeScale()

        self.label_model = ctk.CTkLabel(self, text=f"Modell: {self.scale.model_name}")
        self.label_model.pack(pady=10)

        self.label_category = ctk.CTkLabel(self, text=f"Kategorie: {self.scale.category}")
        self.label_category.pack(pady=10)
