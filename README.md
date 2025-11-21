# Password
big job du 17/11/2025 au 21/11/2025

🔐 Gestionnaire de mots de passe avec vérification + hachage SHA‑256


Un programme Python permettant :

de demander un mot de passe,

de vérifier sa sécurité,

de le hacher avec SHA‑256,

de l’enregistrer dans un fichier JSON,

et de gérer plusieurs mots de passe enregistrés.


📋 Fonctionnalités


🔎 Vérification du mot de passe


Le programme demande à l'utilisateur de choisir un mot de passe, puis vérifie qu’il respecte toutes ces règles :


✔ Au moins 8 caractères

✔ Au moins 1 lettre majuscule

✔ Au moins 1 lettre minuscule

✔ Au moins 1 chiffre

✔ Au moins 1 caractère spécial parmi : ! @ # $ % ^ & *


Si le mot de passe ne respecte pas ces critères :

➡️ ❌ Un message d’erreur s'affiche

➡️ 🔁 L’utilisateur doit en saisir un nouveau

➡️ Jusqu’à avoir un mot de passe valide

🔐 Hachage du mot de passe (SHA‑256)


Une fois validé, le mot de passe est :

transformé en hachage SHA‑256 via hashlib

sauvegardé dans un fichier JSON


👉 Cela garantit que les mots de passe ne sont jamais stockés en clair.

📁 Gestion des mots de passe (JSON)


Le programme permet :


➕ d’ajouter un nouveau mot de passe (après vérification + hachage)

📄 d’afficher tous les mots de passe hachés enregistrés


🧠 Deux versions du programme


Tu as créé deux versions, fonctionnant pareil mais écrites différemment :


FichierDescriptionmain.py / password.py💠 Version n°1 : style 1, logique classique

main1.py / mots_de_passe.py💠 Version n°2 : même programme mais écrit différemment


Les deux :


vérifient le mot de passe

le hachent avec SHA‑256

stockent dans un JSON
