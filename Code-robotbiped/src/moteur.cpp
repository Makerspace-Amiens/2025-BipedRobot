#include "moteur.h"
#include <iostream>

Moteur::Moteur(std::string nom, int pin, double angle_min, double angle_max)
    : nom_(nom), pin_(pin), angle_(0.0), angle_min_(angle_min), angle_max_(angle_max), servo_() {
    servo_.attach(pin_);
    if (nom_.empty()) {
        throw std::invalid_argument("Le nom du moteur ne peut pas etre vide.");
    }
    if (pin_ < 0) {
        throw std::invalid_argument("Le numero de la broche (pin) doit etre positif.");
    }
    if (angle_min_ >= angle_max_) {
        throw std::invalid_argument("La limite d'angle minimum doit etre inferieure a la limite maximum pour le moteur " + nom_);
    }
    std::cout << "Moteur " << nom_ << " (Pin " << pin_ << ") initialise. Limites: [" << angle_min_ << ", " << angle_max_ << "] degres." << std::endl;
}

bool Moteur::definirAngle(double angle_cible) {
    if (angle_cible < angle_min_) {
        std::cerr << "Erreur: Angle cible pour " << nom_ << " (" << angle_cible << ") inferieur a la limite minimum (" << angle_min_ << "). Angle ramene a " << angle_min_ << "." << std::endl;
        angle_ = angle_min_;
        servo_.writeMicroseconds(angleToPWM(angle_, angle_min_, angle_max_, 500, 2500));
        return false; // Indique que l'angle a ete contraint
    } else if (angle_cible > angle_max_) {
        std::cerr << "Erreur: Angle cible pour " << nom_ << " (" << angle_cible << ") superieur a la limite maximum (" << angle_max_ << "). Angle ramene a " << angle_max_ << "." << std::endl;
        angle_ = angle_max_;
        servo_.writeMicroseconds(angleToPWM(angle_, angle_min_, angle_max_, 500, 2500));
        return false; // Indique que l'angle a ete contraint
    } else {
        angle_ = angle_cible;
        std::cout << "Moteur " << nom_ << ": Angle defini a " << angle_ << " degres." << std::endl;
        servo_.writeMicroseconds(angleToPWM(angle_, angle_min_, angle_max_, 500, 2500));
        return true; // Indique que l'angle a ete defini avec succes
    }
}

std::string Moteur::getNom() const { return nom_; }
int Moteur::getPin() const { return pin_; }
double Moteur::getAngle() const { return angle_; }
double Moteur::getAngleMin() const { return angle_min_; }
double Moteur::getAngleMax() const { return angle_max_; }

int Moteur::angleToPWM(double angle_deg, double min_angle, double max_angle, int min_pwm, int max_pwm) {
    if (angle_deg < min_angle) angle_deg = min_angle;
    if (angle_deg > max_angle) angle_deg = max_angle;
    return static_cast<int>(min_pwm + (max_pwm - min_pwm) * (angle_deg - min_angle) / (max_angle - min_angle));
}