from models import Models, PostOfficeScale

class PartsList:
    def __init__(self, model_obj: Models):
        
        self.model = model_obj
        self.parts: dict = {
            f"Load cell ({self.model.max_weight_g  / 1000} kg)": 1,     # example load cell
            "Sechskantschraube M5": 5,                                  # example bolts
            "Rubber": 2                                                 # example rubber
        }
        