class Models:
    def __init__(self, model: str, category: str, max_weight_g: int=50000, accuracy: int=10): 
        """
        Initialize a new scale. By default, we assume a maximum weight of 50kg and increments
        of 10g. It is best to always store weights internally in the smallest unit (grams)
        to avoid rounding errors.

        More coming soon!
        """

        self.model = model                  # Scale model
        self.category = category            # Scale mategory (industry, household, etc.)
        self.max_weight_g = max_weight_g    # The limit until ERR
        self.accuracy = accuracy            # coming soon!





    def __str__(self):
        return f"Model: {self.model} - Category: {self.category}"


    def get_info(self):
        return self.__str__()