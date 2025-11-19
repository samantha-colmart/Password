import json

donnees = {
    "nom": "Stéphane ROBERT",
    "age": 29,
    "adresse": {
        "rue": "456 avenue des Champs",
        "ville": "Lyon",
        "code_postal": "69001"
    },
    "hobbies": ["photographie", "voyage", "musique"]
}
# Enregistrement des données JSON dans un fichier
with open('password.json', 'w') as fichier:
    json.dump(donnees, fichier, indent=4)