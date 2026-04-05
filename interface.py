import customtkinter as ctk
from models import PostOfficeScale


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Scale GUI")
        self.geometry("400x400")
        self.scale = PostOfficeScale()

        self.tabview = ctk.CTkTabview(self, width=350, height=300)
        self.tabview.pack(padx=20, pady=20, expand=True, fill="both")

        self.tabview.add("Scales")
        self.tabview.add("Settings")

        self.tabview.set("Scales")
        
        self.label_details = ctk.CTkLabel(self.tabview.tab("Scales"), text="Scale Information:")
        self.label_details.pack(pady=20)
        
        self.label_settings = ctk.CTkLabel(self.tabview.tab("Settings"), text="System Settings:")
        self.label_settings.pack(pady=20)


if __name__ == "__main__":
    app = Interface()
    app.mainloop()
