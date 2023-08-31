import random

class Kort:
    def __init__(self, färg, rank):
        self.färg = färg
        self.rank = rank
        if rank in ['Knekt', 'Dam', 'Kung']:
            self.värde = 10
        elif rank == 'Ess':
            self.värde = 11
        else:
            self.värde = int(rank)

    def __str__(self):
        return f"{self.rank} av {self.färg}"

class Kortlek:
    def __init__(self):
        färger = ["Hjärter", "Ruter", "Klöver", "Spader"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dam", "Kung", "Ess"]
        self.kort = [Kort(färg, rank) for färg in färger for rank in ranks]
        random.shuffle(self.kort)

    def dra_kort(self):
        return self.kort.pop()
