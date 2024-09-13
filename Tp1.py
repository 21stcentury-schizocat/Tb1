#Liam Rodriguez
#2024-09-13
#Nombre de mots dans un string

#Demander le string
Sentence = input(str("Écriver la phrase dont vous voulez conter les mots:"))

#Séparer le phrase
print(Sentence.split(" "))

#Conter le nombre de mots
print("Il y a")
print(len(Sentence.split(" ")))
print("mots dans la phrase.")

