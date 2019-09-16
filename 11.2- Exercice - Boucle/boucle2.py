# coding=utf-8
# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

for j in range(1, len(B)):
    cle = B[j]
    k = j - 1

    while k >= 0 and B[k] > cle:

        B[k+1] = B[k]
        k += -1
    B[k+1] = cle

print "Tableau B trié : ", B
