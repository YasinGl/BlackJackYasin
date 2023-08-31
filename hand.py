class Hand:
    def __init__(self):
        self.kort = []

    def lägg_till_kort(self, kort):
        self.kort.append(kort)

    def rensa(self):
        self.kort = []

    def få_värde(self):
        värde = sum(kort.värde for kort in self.kort)
        num_ess = sum(1 for kort in self.kort if kort.rank == "Ess")
        while num_ess > 0 and värde + 10 <= 21:
            värde += 10
            num_ess -= 1
        return värde
