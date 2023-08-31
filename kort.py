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
        return f"{self.rank} av {self.färg}" # Kort

    class kortlek:
        def__init__(self):
        return