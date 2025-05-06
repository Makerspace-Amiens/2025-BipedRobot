#include "robotbipede.h"
#include <iostream>
#include <cmath>
#include <iomanip>

RobotBipede::RobotBipede(std::string nom) : nom_(nom), contact_x_right(0.0), contact_x_left(0.0) {
    if (nom_.empty()) {
        throw std::invalid_argument("Le nom du robot ne peut pas etre vide.");
    }
    l_thigh = 0.47;
    l_shank = 0.45;
    l_foot = 0.25;
    h_hip = 0.92;
    ground_level = 0.0;
    step_frequency = 1.1;
    cycle_time = 1.0 / step_frequency;
    swing_phase_ratio = 0.4;
    double_support_ratio = 0.15;
    step_length = 0.65;
    gait_cycle = step_length * 2;
    foot_clearance = 0.12;
    pelvic_tilt_amplitude = 0.06;
    pelvic_rotation_amplitude = 0.08;
    pelvic_sway_amplitude = 0.04;
    horizontal_speed = step_length * step_frequency;
    global_x_position = 0.0;
}

void RobotBipede::ajouterMoteur(Moteur& moteur) {
    if (moteurs_.count(moteur.getNom())) {
        throw std::invalid_argument("Un moteur avec le nom '" + moteur.getNom() + "' existe deja.");
    }
    moteurs_[moteur.getNom()] = &moteur;
    std::cout << "Moteur " << moteur.getNom() << " ajoute." << std::endl;
}

void RobotBipede::ajouterCapteur(Capteur& capteur) {
    if (capteurs_.count(capteur.getNom())) {
        throw std::invalid_argument("Un capteur avec le nom '" + capteur.getNom() + "' existe deja.");
    }
    capteurs_[capteur.getNom()] = &capteur;
    std::cout << "Capteur " << capteur.getNom() << " ajoute." << std::endl;
}

bool RobotBipede::definirAngleMoteur(const std::string& nom_moteur, double angle) {
    if (moteurs_.count(nom_moteur)) {
        return moteurs_[nom_moteur]->definirAngle(angle);
    } else {
        std::cerr << "Erreur: Moteur " << nom_moteur << " non trouve." << std::endl;
        return false;
    }
}

std::map<std::string, double> RobotBipede::lireCapteurs() const {
    std::cout << "Lecture des capteurs:" << std::endl;
    std::map<std::string, double> resultats;
    for (const auto& pair : capteurs_) {
        resultats[pair.first] = pair.second->lireDonnees();
    }
    return resultats;
}

std::string RobotBipede::getNom() const { return nom_; }

std::pair<std::string, double> RobotBipede::getGaitPhaseProgress(double t, const std::string& leg) const {
    double phase_normalized = std::fmod(t, cycle_time) / cycle_time;
    double offset = (leg == "left") ? 0.5 : 0.0;
    double adjusted_phase = std::fmod(phase_normalized + offset, 1.0);

    if (adjusted_phase < 0.05) {
        return {"initial_contact", adjusted_phase / 0.05};
    } else if (adjusted_phase < 0.12) {
        return {"loading_response", (adjusted_phase - 0.05) / 0.07};
    } else if (adjusted_phase < 0.30) {
        return {"mid_stance", (adjusted_phase - 0.12) / 0.18};
    } else if (adjusted_phase < 0.45) {
        return {"terminal_stance", (adjusted_phase - 0.30) / 0.15};
    } else if (adjusted_phase < 0.55) {
        return {"pre_swing", (adjusted_phase - 0.45) / 0.10};
    } else if (adjusted_phase < 0.65) {
        return {"initial_swing", (adjusted_phase - 0.55) / 0.10};
    } else if (adjusted_phase < 0.80) {
        return {"mid_swing", (adjusted_phase - 0.65) / 0.15};
    } else if (adjusted_phase < 0.92) {
        return {"terminal_swing", (adjusted_phase - 0.80) / 0.12};
    } else if (adjusted_phase < 0.97) {
        return {"swing_preparation", (adjusted_phase - 0.92) / 0.05};
    } else {
        return {"foot_placement", (adjusted_phase - 0.97) / 0.03};
    }
}

double RobotBipede::smoothInterp(double p, const std::vector<double>& vals) const {
    if (p <= 0) return vals[0];
    if (p >= 1) return vals[1];
    return vals[0] + (vals[1] - vals[0]) * (3 * std::pow(p, 2) - 2 * std::pow(p, 3));
}

std::tuple<double, double, double> RobotBipede::getJointAngles(const std::string& phase_name, double phase_progress, const std::string& leg) const {
    static const std::map<std::string, std::map<std::string, std::vector<double>>> angle_params = {
        {"initial_contact", {{"thigh", {-0.1, -0.3}}, {"shank", {0.05, 0.2}}, {"foot", {-0.2, 0.1}}}},
        {"loading_response", {{"thigh", {-0.3, 0.1}}, {"shank", {0.2, -0.2}}, {"foot", {0.1, 0.2}}}},
        {"mid_stance", {{"thigh", {0.1, 0.4}}, {"shank", {-0.2, -0.4}}, {"foot", {0.2, 0.3}}}},
        {"terminal_stance", {{"thigh", {0.4, 0.2}}, {"shank", {-0.4, 0.2}}, {"foot", {0.3, 0.6}}}},
        {"pre_swing", {{"thigh", {0.2, -0.5}}, {"shank", {0.2, 0.0}}, {"foot", {0.6, -0.8}}}},
        {"initial_swing", {{"thigh", {-0.5, -0.2}}, {"shank", {0.0, -0.6}}, {"foot", {-0.8, 0.2}}}},
        {"mid_swing", {{"thigh", {-0.2, 0.2}}, {"shank", {-0.6, 0.0}}, {"foot", {0.2, -0.2}}}},
        {"terminal_swing", {{"thigh", {0.2, -0.1}}, {"shank", {0.0, 0.1}}, {"foot", {-0.2, -0.4}}}},
        {"swing_preparation", {{"thigh", {-0.1, -0.15}}, {"shank", {0.1, 0.15}}, {"foot", {-0.4, -0.3}}}},
        {"foot_placement", {{"thigh", {-0.15, -0.1}}, {"shank", {0.15, 0.05}}, {"foot", {-0.3, -0.2}}}}
    };

    const auto& params = angle_params.at(phase_name);
    double thigh_angle = smoothInterp(phase_progress, params.at("thigh"));
    double shank_angle = smoothInterp(phase_progress, params.at("shank"));
    double foot_angle = smoothInterp(phase_progress, params.at("foot"));
    return std::make_tuple(thigh_angle, shank_angle, foot_angle);
}

std::tuple<double, double, double, double, double, double, double, double, double, double>
RobotBipede::getJointPositions(double time,const std::string& leg) {
        double offset_x = (leg == "left") ? step_length : 0.0;
        double sign = (leg == "left") ? 1.0 : -1.0;
    
        auto [phase_name, phase_progress] = getGaitPhaseProgress(time, leg);
        auto [thigh_angle, shank_angle, foot_angle] = getJointAngles(phase_name, phase_progress, leg);
    
        // Kinematics (simplified - assumes a planar robot)
        double hip_x = global_x_position + offset_x;
        double hip_y = ground_level + h_hip;
    
        double knee_x = hip_x + l_thigh * std::sin(thigh_angle);
        double knee_y = hip_y - l_thigh * std::cos(thigh_angle);
    
        double ankle_x = knee_x + l_shank * std::sin(thigh_angle + shank_angle);
        double ankle_y = knee_y - l_shank * std::cos(thigh_angle + shank_angle);
    
        double foot_tip_x = ankle_x + l_foot * std::sin(thigh_angle + shank_angle + foot_angle);
        double foot_tip_y = ankle_y - l_foot * std::cos(thigh_angle + shank_angle + foot_angle);
    
        double foot_start_x = ankle_x;
        double foot_start_y = ankle_y;
        double foot_end_x = foot_tip_x;
        double foot_end_y = foot_tip_y;
    
        return std::make_tuple(hip_x, hip_y, knee_x, knee_y, ankle_x, ankle_y, foot_start_x, foot_start_y, foot_end_x, foot_end_y);
    }