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

# Mise à jour apt-get
print_step "Mise à jour apt-get..."
if apt-get update; then
    print_success "apt-get a été mis à jour avec succès."
else
    print_error "Erreur lors de la mise à jour apt-get."
    exit 1
fi

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

# Installation de nmap
print_step "Installation de nmap"
if apt-get install nmap; then
    print_success "nmap installé avec succès."
else
    print_error "Erreur lors de l'installation de nmap."
    exit 1
fi

# Installation de wkhtmltopdf
print_step "Installation de libjpeg-dev et zlib1g-dev..."
if apt-get install wkhtmltopdf; then
    print_success "wkhtmltopdf installé avec succès."
else
    print_error "Erreur lors de l'installation de wkhtmltopdf."
    exit 1
fi

# Installation de fping
print_step "Installation de fping..."
if apt-get install fping; then
    print_success "fping installé avec succès."
else
    print_error "Erreur lors de l'installation de fping."
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

# Création du venv
print_step "Mise en place du venv..."
if python3 -m venv .venv; then
    print_success "venv mis en place avec succès"
else
    print_error "Erreur lors de la mise en place du venv"
    exit 1
fi

# Activation du venv
print_step "Activation du venv..."
if source .venv/bin/activate; then
    print_success "venv activé avec succès"
else
    print_error "Erreur lors de la mise en place du venv"
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

# Installation des bibliothèques python
print_step "Installation en cours..."
if pip install -r requirements.txt; then
    print_success "Toutes les bibliothèques ont été installées avec succès"
else
    print_error "Erreur lors de l'installation des bibliothèques."
    exit 1
fi

print_info "Tous les paquets ont été installés avec succès."
