import hashlib
import json
import os

caracteres_speciaux = "!@#$%^&*"
FICHIER = "mots_de_passe.json"

def charger_mots_de_passe():
    if not os.path.exists(FICHIER):
        return []
    with open(FICHIER, "r") as f:
        return json.load(f)
    
def sauvegarder_mots_de_passe(liste):
    with open (FICHIER, "w") as f:
        return json.dump(liste, f, indent=4)

while True:
    mot_de_passe = input("Veuillez entrer votre mot de passe : ")

    if len(mot_de_passe) < 8:
        print("Erreur : le mot de passe doit contenir au moins 8 caractères.")
        continue

    for c in mot_de_passe:
        if c.isupper():
            break
    else:
        print("Erreur : le mot de passe doit contenir au moins une majuscule.")
        continue

    for c in mot_de_passe:
        if c.islower():
            break
    else:
        print("Erreur : le mot de passe doit contenir au moins une minuscule.")
        continue

    for c in mot_de_passe:
        if c.isdigit():
            break
    else:
        print("Erreur : le mot de passe doit contenir au moins un chiffre.")
        continue

    for c in mot_de_passe:
        if c in caracteres_speciaux:
            break
    else:
        print(f"Erreur : le mot de passe doit contenir au moins un caractère spécial ({caracteres_speciaux}).")
        continue

    print("Mot de passe valide !")
    break

hash_object = hashlib.sha256(mot_de_passe.encode())  
mot_de_passe_hash = hash_object.hexdigest()

print("\nMot de passe haché (SHA-256) :")
print(mot_de_passe_hash)

mots = charger_mots_de_passe()
mots.append(mot_de_passe_hash)
sauvegarder_mots_de_passe(mots)

print("\nMot de passe haché enregistré dans le fichier JSON !")