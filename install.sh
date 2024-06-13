#!/bin/bash

# Couleurs et styles
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m' # Pas de couleur

# Fonction pour afficher les étapes
print_step() {
    echo -e "${BLUE}==> $1${NC}"
}

# Fonction pour afficher les succès
print_success() {
    echo -e "${GREEN}✔ $1${NC}"
}

# Fonction pour afficher les erreurs
print_error() {
    echo -e "${RED}✖ $1${NC}"
}

# Fonction pour afficher les informations
print_info() {
    echo -e "${YELLOW}$1${NC}"
}

# Installation de cmake
print_step "Installation de cmake..."
if apt-get install -y cmake; then
    print_success "cmake installé avec succès."
else
    print_error "Erreur lors de l'installation de cmake."
    exit 1
fi

# Installation de libjpeg-dev et zlib1g-dev
print_step "Installation de libjpeg-dev et zlib1g-dev..."
if apt-get install -y libjpeg-dev zlib1g-dev; then
    print_success "libjpeg-dev et zlib1g-dev installés avec succès."
else
    print_error "Erreur lors de l'installation de libjpeg-dev et zlib1g-dev."
    exit 1
fi

# Installation de python3.11-venv
print_step "Installation de python3.11-venv..."
if apt-get install -y python3.11-venv; then
    print_success "python3.11-venv installé avec succès."
else
    print_error "Erreur lors de l'installation de python3.11-venv."
    exit 1
fi

# Mise à jour de pip
print_step "Mise à jour de pip..."
if pip install --upgrade pip; then
    print_success "pip mis à jour avec succès."
else
    print_error "Erreur lors de la mise à jour de pip."
    exit 1
fi

print_info "Tous les paquets ont été installés avec succès."
