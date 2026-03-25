from interface import Interface

class Models:
    def __init__(self, model: str, category: str): 
        self.model = model
        self.category = category


    def __str__(self):
        return f"Model: {self.model} - Category: {self.category}"


    def get_info(self):
        return self.__str__()


if __name__ == "__main__":
    app = Interface()
    app.mainloop()