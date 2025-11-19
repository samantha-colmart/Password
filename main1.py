import hashlib
import json
caracteres_speciaux = "!@#$%^&*"

while True:
    mot_de_passe = input("Veuillez entrer votre mot de passe : ")

    if len(mot_de_passe) < 8:
        print("Erreur : le mot de passe doit contenir au moins 8 caractères.")
        continue

    if not any(c.isupper() for c in mot_de_passe):
        print("Erreur : il faut au moins une majuscule.")
        continue

    if not any(c.islower() for c in mot_de_passe):
        print("Erreur : il faut au moins une minuscule.")
        continue

    if not any(c.isdigit() for c in mot_de_passe):
        print("Erreur : il faut au moins un chiffre.")
        continue

    if not any(c in caracteres_speciaux for c in mot_de_passe):
        print(f"Erreur : il faut au moins un caractère spécial ({caracteres_speciaux}).")
        continue

    print("Mot de passe valide !")
    break

hash_object = hashlib.sha256(mot_de_passe.encode())  
mot_de_passe_hash = hash_object.hexdigest()
try:
    with open("password.json", "r") as fichier:
        liste_hash = json.load(fichier)   # lire ce qu'il y a déjà

        if isinstance(liste_hash, str):
            liste_hash = [liste_hash]

except:
    liste_hash = []

liste_hash.append(mot_de_passe_hash)

with open('password.json', 'w') as fichier:
    json.dump(liste_hash, fichier, indent=4)

print("\nMot de passe haché (SHA-256) :")
print(mot_de_passe_hash)