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

class BlackjackSpel:
    def __init__(self):
        self.kortlek = Kortlek()
        self.spelare_hand = Hand()
        self.dealer_hand = Hand()
        self.pengar = 0
        self.insats = 0
        self.dealer_skämt = [
            "Du borde byta karriär",
            "Lyckan var inte på din sida den här gången.",
            "Kanske prova ett annat spel?",
            "De säger att övning ger färdighet. Fortsätt öva!",
        ]
        self.dealer_arga_fraser = [
            "Hur lyckades du med det? Du har en bra programmerings lärare Mahmud ellerhur?",
            "Du måste fuska...",
            "Det här kan inte vara sant!",
            "Otroligt!",
        ]

    def satsa_pengar(self):
        while True:
            try:
                self.insats = int(input("Hur mycket pengar vill du satsa? "))
                if self.insats > self.pengar:
                    print("Du har inte tillräckligt med pengar.")
                else:
                    break
            except ValueError:
                print("Ogiltigt värde. Ange en heltalsmängd.")

    def dela_ut_inledande_kort(self):
        self.spelare_hand.rensa()
        self.dealer_hand.rensa()

        self.spelare_hand.lägg_till_kort(self.kortlek.dra_kort())
        self.dealer_hand.lägg_till_kort(self.kortlek.dra_kort())  # För att du ska kunna se dealerna första kort i blackjack.
        self.spelare_hand.lägg_till_kort(self.kortlek.dra_kort())
        self.dealer_hand.lägg_till_kort(self.kortlek.dra_kort())

    def spela(self):
        while True:
            self.pengar = 0
            while self.pengar <= 0:
                try:
                    self.pengar = int(input("Välkommen till Blackjack! Ange hur mycket pengar du vill börja med: "))
                    if self.pengar <= 0:
                        print("Ange en positiv heltalsmängd.")
                except ValueError:
                    print("Ogiltigt värde. Ange en positiv heltalsmängd.")

            while self.pengar > 0:
                print("Pengar:", self.pengar)
                self.satsa_pengar()

                self.spelare_hand.rensa()
                self.dealer_hand.rensa()

                self.dela_ut_inledande_kort()

                if self.spelare_hand.få_värde() == 21:
                    print("Blackjack! Du vann automatiskt.")
                    self.pengar += self.insats * 2
                    print(random.choice(self.dealer_arga_fraser))
                    continue

                print("Dealerns första kort:", self.dealer_hand.kort[0])
                while True:
                    print("Din hand:", ", ".join(str(kort) for kort in self.spelare_hand.kort))
                    print("Ditt totala värde:", self.spelare_hand.få_värde())
                    åtgärd = input("Vill du ta kort eller stanna? ").lower()

                    if åtgärd == "ta kort":
                        self.spelare_hand.lägg_till_kort(self.kortlek.dra_kort())
                        if self.spelare_hand.få_värde() > 21:
                            print("Överskridning! Du förlorade.")
                            self.pengar -= self.insats
                            print(random.choice(self.dealer_skämt))
                            break
                    elif åtgärd == "stanna":
                        while self.dealer_hand.få_värde() < 17:
                            self.dealer_hand.lägg_till_kort(self.kortlek.dra_kort())
                        print("Dealerns totala värde:", self.dealer_hand.få_värde())

                        if self.dealer_hand.få_värde() > 21:
                            print("Dealern överskred. Du vann!")
                            self.pengar += self.insats * 2
                            print(random.choice(self.dealer_arga_fraser))
                        elif self.spelare_hand.få_värde() > self.dealer_hand.få_värde():
                            print("Grattis! Du vann.")
                            self.pengar += self.insats * 2
                            print(random.choice(self.dealer_arga_fraser))
                        elif self.spelare_hand.få_värde() < self.dealer_hand.få_värde():
                            print("Dealern vinner.")
                            self.pengar -= self.insats
                        else:
                            print("Det blir lika (push). Ingen vinner eller förlorar.")
                        break

if __name__ == "__main__":
    spel = BlackjackSpel()
    spel.spela()
    print("Spelet är slut. Tack för att du spelade!")

