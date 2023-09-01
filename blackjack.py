import random
from kort import Kortlek  # Importera Kortlek-klassen från kort.py
from hand import Hand    # Importera Hand-klassen från hand.pys

class BlackjackSpel:
    def __init__(self):
        self.kortlek = Kortlek()  # Skapa en ny kortlek från Kortlek-klassen
        self.spelare_hand = Hand()  # Skapa en tom hand för spelaren från Hand-klassen
        self.dealer_hand = Hand()   # Skapa en tom hand för dealern från Hand-klassen
        self.pengar = 0            # Spelarens totala pengar
        self.insats = 0            # Aktuell insats
        self.dealer_skämt = [      # Listan med dealerens skämtsamma kommentarer
            "Du borde byta karriär",
            "Lyckan var inte på din sida den här gången.",
            "Kanske prova ett annat spel?",
            "De säger att övning ger färdighet. Fortsätt öva!",
        ]
        self.dealer_arga_fraser = [  # Listan med dealerens arga kommentarer
            "Hur lyckades du med det? Du har en bra programmerings lärare Mahmud ellerhur?",
            "Du måste fuska...",
            "Det här kan inte vara sant!",
            "Otroligt!",
        ]

    def satsa_pengar(self):
        while True:
            try:
                self.insats = int(input("Hur mycket pengar vill du satsa från din kredit? "))
                if self.insats > self.pengar:
                    print("Du har inte tillräckligt med pengar.")
                else:
                    break
            except ValueError:
                print("Ogiltigt värde. Ange en heltalsmängd.")

    def dela_ut_inledande_kort(self):
        self.spelare_hand.rensa()  # Töm spelarens hand
        self.dealer_hand.rensa()   # Töm dealerens hand

        # Dela ut två kort till spelaren och två till dealern
        self.spelare_hand.lägg_till_kort(self.kortlek.dra_kort())
        self.dealer_hand.lägg_till_kort(self.kortlek.dra_kort())
        self.spelare_hand.lägg_till_kort(self.kortlek.dra_kort())
        self.dealer_hand.lägg_till_kort(self.kortlek.dra_kort())

    def spela(self):
        while True:
            self.pengar = 0
            while self.pengar <= 0:
                try:
                    self.pengar = int(input("Välkommen till Blackjack! Ange hur mycket pengar du vill börja med (Pengar som du lägger in i casinot): "))
                    if self.pengar <= 0:
                        print("Ange en positiv heltalsmängd. (Till exempel, 100)")
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
                            print("Grattis! Du vann :)")
                            self.pengar += self.insats * 2
                            print(random.choice(self.dealer_arga_fraser))
                        elif self.spelare_hand.få_värde() < self.dealer_hand.få_värde():
                            print("Dealern vinner :( ")
                            self.pengar -= self.insats
                        else:
                            print("Det blir lika (push). Ingen vinner eller förlorar.")
                        break

if __name__ == "__main__":
    spel = BlackjackSpel()
    spel.spela()
    print("Spelet är slut. Tack för att du spelade!")
