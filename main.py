from interface import Interface

class Models:
    def __init__(self, model: str, category: str, costumer_request: str=None): 
        # costumer_request gets None for an optional argument

        self.model = model
        # model = Personenwaagen, Rollstuhlwagen, Postwaagen etc.git

        # category = Industrie, Haushalt, Medizin etc.        
        self.category = category

        # add the optional part for that costumer requestgit 
        if not costumer_request:
            self.costumer_request = "No Entry"
        else:
            self.costumer_request = costumer_request


    def __str__(self):
        return f"Model: {self.model} - Category: {self.category} - Costumer Request: {self.costumer_request}"


    def get_info(self):
        return self.__str__()


if __name__ == "__main__":
    app = Interface()
    app.mainloop()