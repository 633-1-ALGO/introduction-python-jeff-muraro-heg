# coding=utf-8
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

print(texte)
print "Le nombre d'occurence du mot 'exemple' est : ", texte.count("exemple")
texte = texte.replace('est', 'représente')
print(texte[::-1])
