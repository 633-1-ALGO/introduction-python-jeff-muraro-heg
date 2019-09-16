nb_articles = 13
prix_ht = 42.75

tva = 0.077
prix_ttc = (nb_articles * prix_ht) + (nb_articles * prix_ht * tva)
print("Le prix TTC est de ", prix_ttc, " chf.")
