caracteres_speciaux = "!@#$%^&*"

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

    # Vérifier la présence d'une minuscule
    for c in mot_de_passe:
        if c.islower():
            break
    else:
        print("Erreur : le mot de passe doit contenir au moins une minuscule.")
        continue

    # Vérifier la présence d'un chiffre
    for c in mot_de_passe:
        if c.isdigit():
            break
    else:
        print("Erreur : le mot de passe doit contenir au moins un chiffre.")
        continue

    # Vérifier la présence d'un caractère spécial
    for c in mot_de_passe:
        if c in caracteres_speciaux:
            break
    else:
        print(f"Erreur : le mot de passe doit contenir au moins un caractère spécial ({caracteres_speciaux}).")
        continue

    # Si toutes les conditions sont remplies
    print("Mot de passe valide !")
    break
