montant_initial = 10000  
taux_rendement_annuel = 5  

gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Gain annuel initial : {gain_annuel:.2f} euros")

montant_initial += 5000  
taux_rendement_annuel += 2  
gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Gain annuel après augmentation de capital : {gain_annuel:.2f} euros")

=ontant_initial -= montant_initial * 0.10  
taux_rendement_annuel -= 1  
gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Gain annuel après retrait : {gain_annuel:.2f} euros")
