#include "capteur.h"
#include <iostream>
#include <limits> // Pour numeric_limits

Capteur::Capteur(std::string nom) : nom_(nom) {
    if (nom_.empty()) {
        throw std::invalid_argument("Le nom du capteur ne peut pas etre vide.");
    }
}

double Capteur::lireDonnees() {
    // Ici, tu ajouterais la logique pour lire les donnees reelles du capteur
    double donnees = std::numeric_limits<double>::quiet_NaN(); // Represente une valeur "non un nombre" en cas d'echec de lecture
    std::cerr << "Avertissement: Lecture de donnees simulee pour le capteur " << nom_ << "." << std::endl;
    return donnees;
}

std::string Capteur::getNom() const { return nom_; }