class Hand:
    def __init__(self):
        self.kort = []  # En lista som håller de kort som utgör handen

    def lägg_till_kort(self, kort):
        self.kort.append(kort)  # Lägger till ett kort i handen

    def rensa(self):
        self.kort = []  # Tömmer handen genom att återställa kortlistans

    def få_värde(self):
        värde = sum(kort.värde for kort in self.kort)  # Beräknar det aktuella värdet av handen genom att summera kortens värden

        num_ess = sum(1 for kort in self.kort if kort.rank == "Ess")  # Räknar antalet Ess i handen
        while num_ess > 0 and värde + 10 <= 21:
            värde += 10  # Om det finns ett Ess i handen och värdet är mindre än eller lika med 21, räknas Ess som 11
            num_ess -= 1

        return värde  # Returnerar det totala värdet av handen, med beaktande av Ess som kan vara 11 eller 1
