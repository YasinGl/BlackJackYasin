import random

class Kort:
    def __init__(self, färg, rank):
        self.färg = färg  # Färgen på kortet (t.ex. Hjärter, Ruter, Klöver, Spader))
        self.rank = rank  # Ranken på kortet (t.ex. 2, 3, Ess, Knekt, Dam, Kung)
        if rank in ['Knekt', 'Dam', 'Kung']:
            self.värde = 10  # Värdet för Knekt, Dam och Kung är 10 i Blackjack
        elif rank == 'Ess':
            self.värde = 11  # Ess kan vara värt 11 i vissa situationer, annars 1
        else:
            self.värde = int(rank)  # Värdet är samma som ranken för övriga kort

    def __str__(self):
        return f"{self.rank} av {self.färg}"  # Returnerar en läsbar strängrepresentation av kortet

class Kortlek:
    def __init__(self):
        färger = ["Hjärter", "Ruter", "Klöver", "Spader"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dam", "Kung", "Ess"]
        self.kort = [Kort(färg, rank) for färg in färger for rank in ranks]  # Skapar en kortlek genom att kombinera färger och ranks
        random.shuffle(self.kort)  # Blandar kortleken slumpmässigt

    def dra_kort(self):
        return self.kort.pop()  # Drar ett kort från kortleken och tar bort det från leken
