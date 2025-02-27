from traceback import print_tb


class CompteBancaire:
    def __init__(self, titulaire = "Titulaire", solde = 0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if self.solde - montant < 0:
            raise ValueError("Erreur : solde insuffisant")
        else:
            self.solde -= montant

    def afficher_solde(self):
        print(f"Le solde du compte de {self.titulaire} est de {self.solde}€")