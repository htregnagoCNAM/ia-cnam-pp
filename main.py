from src.poo import CompteBancaire

compteBancaire = CompteBancaire("Hugo", 500)
compteBancaire.afficher_solde()

print("Je dépose 100€")
compteBancaire.deposer(100)
compteBancaire.afficher_solde()

print("Je retire 200€")
compteBancaire.retirer(200)
compteBancaire.afficher_solde()

print("Je retire 400€")
compteBancaire.retirer(400)
compteBancaire.afficher_solde()

print("Je tente de retirer trop")
compteBancaire.retirer(1)
compteBancaire.afficher_solde()