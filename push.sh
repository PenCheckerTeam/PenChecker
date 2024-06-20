#!/bin/bash

# Demande à l'utilisateur d'entrer le message de commit
echo "Intitulé du commit :"
read user_input

# Vérifie que le message de commit n'est pas vide
if [ -z "$user_input" ]; then
    echo "Le message de commit ne peut pas être vide."
    exit 1
fi

# Demande à l'utilisateur d'entrer le tag à créer
echo "Tag à créer :"
read tag_input

# Vérifie que le tag n'est pas vide
if [ -z "$tag_input" ]; then
    echo "Le tag ne peut pas être vide."
    exit 1
fi

# Ajoute les fichiers spécifiés à la staging area
git add *.py install.sh requirements.txt push.sh

# Vérifie si la commande git add a réussi
if [ $? -ne 0 ]; then
    echo "Erreur lors de l'ajout des fichiers."
    exit 1
fi

# Commit les modifications avec le message de l'utilisateur
git commit -m "$user_input"

# Vérifie si la commande git commit a réussi
if [ $? -ne 0 ]; then
    echo "Erreur lors du commit."
    exit 1
fi

# Push les modifications sur la branche main
git push origin main

# Vérifie si la commande git push a réussi
if [ $? -ne 0 ]; then
    echo "Erreur lors du push."
    exit 1
fi

# Crée un tag avec l'entrée de l'utilisateur
git tag $tag_input

# Vérifie si la commande git tag a réussi
if [ $? -ne 0 ]; then
    echo "Erreur lors de la création du tag."
    exit 1
fi

# Push le tag vers le repository distant
git push origin $tag_input

# Vérifie si la commande git push du tag a réussi
if [ $? -ne 0 ]; then
    echo "Erreur lors du push du tag."
    exit 1
fi

echo "Modifications et tag poussés avec succès."
