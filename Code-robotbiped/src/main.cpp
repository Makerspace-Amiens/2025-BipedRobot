#include <iostream>
#include <string>
#include <map>
#include <limits> // Pour numeric_limits

class Moteur {
public:
    Moteur(std::string nom, int pin, double angle_min = 0.0, double angle_max = 180.0)
        : nom_(nom), pin_(pin), angle_(0.0), angle_min_(angle_min), angle_max_(angle_max) {
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

    bool definirAngle(double angle_cible) {
        if (angle_cible < angle_min_) {
            std::cerr << "Erreur: Angle cible pour " << nom_ << " (" << angle_cible << ") inferieur a la limite minimum (" << angle_min_ << "). Angle ramene a " << angle_min_ << "." << std::endl;
            angle_ = angle_min_;
            return false; // Indique que l'angle a ete contraint
        } else if (angle_cible > angle_max_) {
            std::cerr << "Erreur: Angle cible pour " << nom_ << " (" << angle_cible << ") superieur a la limite maximum (" << angle_max_ << "). Angle ramene a " << angle_max_ << "." << std::endl;
            angle_ = angle_max_;
            return false; // Indique que l'angle a ete contraint
        } else {
            angle_ = angle_cible;
            std::cout << "Moteur " << nom_ << ": Angle defini a " << angle_ << " degres." << std::endl;
            // Ici, tu ajouterais la logique pour envoyer la commande a la broche du servo
            return true; // Indique que l'angle a ete defini avec succes
        }
    }

    std::string getNom() const { return nom_; }
    int getPin() const { return pin_; }
    double getAngle() const { return angle_; }
    double getAngleMin() const { return angle_min_; }
    double getAngleMax() const { return angle_max_; }

private:
    std::string nom_;
    int pin_;
    double angle_;
    double angle_min_;
    double angle_max_;
};

class Capteur {
public:
    Capteur(std::string nom) : nom_(nom) {
        if (nom_.empty()) {
            throw std::invalid_argument("Le nom du capteur ne peut pas etre vide.");
        }
    }

    double lireDonnees() {
        // Ici, tu ajouterais la logique pour lire les donnees reelles du capteur
        double donnees = std::numeric_limits<double>::quiet_NaN(); // Represente une valeur "non un nombre" en cas d'echec de lecture
        std::cerr << "Avertissement: Lecture de donnees simulee pour le capteur " << nom_ << "." << std::endl;
        return donnees;
    }

    std::string getNom() const { return nom_; }

private:
    std::string nom_;
};

class RobotBipede {
public:
    RobotBipede(std::string nom) : nom_(nom) {
        if (nom_.empty()) {
            throw std::invalid_argument("Le nom du robot ne peut pas etre vide.");
        }
    }

    void ajouterMoteur(Moteur& moteur) {
        if (moteurs_.count(moteur.getNom())) {
            throw std::invalid_argument("Un moteur avec le nom '" + moteur.getNom() + "' existe deja.");
        }
        moteurs_[moteur.getNom()] = &moteur;
        std::cout << "Moteur " << moteur.getNom() << " ajoute." << std::endl;
    }

    void ajouterCapteur(Capteur& capteur) {
        if (capteurs_.count(capteur.getNom())) {
            throw std::invalid_argument("Un capteur avec le nom '" + capteur.getNom() + "' existe deja.");
        }
        capteurs_[capteur.getNom()] = &capteur;
        std::cout << "Capteur " << capteur.getNom() << " ajoute." << std::endl;
    }

    bool definirAngleMoteur(const std::string& nom_moteur, double angle) {
        if (moteurs_.count(nom_moteur)) {
            return moteurs_[nom_moteur]->definirAngle(angle);
        } else {
            std::cerr << "Erreur: Moteur " << nom_moteur << " non trouve." << std::endl;
            return false;
        }
    }

    std::map<std::string, double> lireCapteurs() const {
        std::cout << "Lecture des capteurs:" << std::endl;
        std::map<std::string, double> resultats;
        for (const auto& pair : capteurs_) {
            resultats[pair.first] = pair.second->lireDonnees();
        }
        return resultats;
    }

    std::string getNom() const { return nom_; }

private:
    std::string nom_;
    std::map<std::string, Moteur*> moteurs_;
    std::map<std::string, Capteur*> capteurs_;
};

int main() {
    try {
        // Creation des moteurs avec des limites d'angle
        // Hanche gauche
        Moteur hancheG_avant("HancheG_AvAr", 1, -30.0, 90.0);
        Moteur hancheG_cote("HancheG_GD", 2, -25.0, 25.0);
        Moteur hancheG_rot("HancheG_Rotation", 3, -45.0, 45.0);

        // Genou gauche
        Moteur genouG("GenouG", 4, 0.0, 130.0);

        // Hanche droite
        Moteur hancheD_avant("HancheD_AvAr", 5, -30.0, 90.0);
        Moteur hancheD_cote("HancheD_GD", 6, -25.0, 25.0);
        Moteur hancheD_rot("HancheD_Rotation", 7, -45.0, 45.0);

        // Genou droit
        Moteur genouD("GenouD", 8, 0.0, 130.0);

        // Creation du robot
        RobotBipede robot("Roby");

        // Ajout des moteurs au robot
        robot.ajouterMoteur(hancheG_avant);
        robot.ajouterMoteur(genouG);
        robot.ajouterMoteur(hancheD_avant);
        robot.ajouterMoteur(genouD);
        robot.ajouterMoteur(hancheG_cote);
        robot.ajouterMoteur(hancheG_rot);
        robot.ajouterMoteur(hancheD_cote);
        robot.ajouterMoteur(hancheD_rot);

        // Tentative de definition d'angles hors limites
        robot.definirAngleMoteur("HancheG_AvAr", -40.0);
        robot.definirAngleMoteur("GenouG", 140.0);
        robot.definirAngleMoteur("HancheD_AvAr", 100.0);
        robot.definirAngleMoteur("GenouD", -10.0);
        robot.definirAngleMoteur("HancheG_cote", 30.0);
        robot.definirAngleMoteur("HancheG_Rotation", -50.0);
        robot.definirAngleMoteur("HancheD_cote", -30.0);
        robot.definirAngleMoteur("HancheD_Rotation", 60.0);

        // Lecture des capteurs
        std::map<std::string, double> resultats_capteurs = robot.lireCapteurs();
        std::cout << "Resultats des capteurs:" << std::endl;
        for (const auto& pair : resultats_capteurs) {
            std::cout << pair.first << ": " << pair.second << std::endl;
        }

    } catch (const std::exception& e) {
        std::cerr << "Erreur: " << e.what() << std::endl;
        return 1; // Indique une erreur lors de l'execution
    }

    return 0; // Indique une execution reussie
}

