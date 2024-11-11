nom = "PC"
prix = 2000
quantité = 4
prix = prix * 1.10

print("{n} - {p}€ stock : {q}".format(n=nom, p=prix, q=quantité))

x = int(input("Combien de produits voulez-vous acheter ? "))

if x <= quantité:
    quantité -= x

    print("Nouvelle quantité en stock : {q}".format(q=quantité))

else:
    print("Quantité insuffisante en stock.")
