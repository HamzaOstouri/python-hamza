# -*- coding: utf-8 -*-
class CompteBancaire:
    def __init__(self, numeroCompte, nomPrenom, solde):
        self.numeroCompte = numeroCompte
        self.nomPrenom = nomPrenom
        self.solde = solde
    def Versement(self,Somme):
        self.solde = self.solde + Somme
    def Retrait(self, Somme):
        if(Somme > self.solde ):
            print("solde insuffisant")
        else:
            self.solde = self.solde - Somme


newCompte = CompteBancaire(12827878, "Robert Hamza", 2570)
print("le numero de compte est : ", newCompte.numeroCompte)
print("Nom du propriétaire : ",newCompte.nomPrenom)
print("Solde sans erreur :", newCompte.solde)
newCompte.Versement(5350)
print("Solde aprés :", newCompte.solde)
newCompte.Retrait(10000)