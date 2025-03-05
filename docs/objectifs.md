---
layout: default
nav_order: 2
title: Objectifs du Projet
---


# Objectifs du Projet

## 1. Objectif Principal et Spécifiques 
L'objectif principal du projet est de concevoir un robot bipède capable de marcher de manière autonome tout en maintenant son équilibre. Ce défi implique plusieurs aspects essentiels :

<div class="bubbles-container">
    <div class="bubble-wrapper">
        <div class="bubble">Développement de la Structure mécanique</div>
        <div class="arrow"></div>
        <div class="sub-objective">Conception d’une structure légère et robuste adaptée aux servomoteurs Dynamixel</div>
    </div>
    <div class="bubble-wrapper">
        <div class="bubble">Création d'un système de contrôle précis des articulations</div>
        <div class="arrow"></div>
        <div class="sub-objective">Développement d’un programme permettant un contrôle fluide des articulations</div>
    </div>
    <div class="bubble-wrapper">
        <div class="bubble">Stratégies de stabilisation et Algorithmes de marche</div>
        <div class="arrow"></div>
        <div class="sub-objective">Expérimentation de stratégies de stabilisation et génération d’algorithmes de marche efficaces</div>
    </div>
</div>

<div style="border-top: 2px solid #e0e0e0; margin: 30px 0;"></div>

## 2. Quels sont les enjeux et les objectifs à atteindre ?

#### D'un point de vue technique, 75h pour réaliser...

- **Coordination des mouvements :** Assurer la stabilité et l'équilibre pendant les déplacements.
- **Optimisation des trajectoires de marche :** Garantir la fluidité et l'efficacité des déplacements.
- **Compétences transversales :** Développer des compétences en gestion de projet, travail d’équipe et résolution de problèmes complexes.

<div style="border-top: 2px solid #e0e0e0; margin: 30px 0;"></div>

## 3. Quels sont les impacts attendus de ce projet ? 

#### D'un point de vue personnel...

- **Renforcer ses compétences techniques** tels que la mécanique, la programmation, et l'IA.
- **Développer des compétences transversales** : gestion de projet et la collaboration en équipe.
- Apporter des **solutions concrètes** pour des applications futures en robotique.

<div style="border-top: 2px solid #e0e0e0; margin: 30px 0;"></div>

## 4. Cahier des Charges
[**Cahier des charges "Robot Bipède"** - Cliquez ici pour y accéder](assets/pdf/CAHIER_DES_CHARGES.pdf)

<style>
/* Conteneur principal des bulles */
.bubbles-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px;
    margin-top: 20px;
}

/* Structure de chaque bulle */
.bubble-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

/* Style des bulles */
.bubble {
    width: 280px;
    height: 120px;
    padding: 15px;
    background-color: rgb(161, 16, 16);
    color: white;
    border-radius: 30px;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    text-align: center;
    opacity: 0;
    animation: fadeIn 1s forwards;
}

/* Apparition progressive des bulles */
.bubble:nth-child(1) { animation-delay: 0s; }
.bubble:nth-child(2) { animation-delay: 0.5s; }
.bubble:nth-child(3) { animation-delay: 1s; }

/* Flèche sous la bulle */
.arrow {
    width: 0;
    height: 0;
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-top: 15px solid gray;
    margin: 10px 0;
}

/* Texte des sous-objectifs */
.sub-objective {
    width: 280px;
    height: 80px;
    padding: 10px;
    background-color: #f0f0f0;
    color: #333;
    border-radius: 10px;
    text-align: center;
    font-size: 14px;
    font-weight: normal;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.15);
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Animation d'apparition */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Responsive Design */
@media screen and (max-width: 768px) {
    .bubbles-container {
        flex-direction: column;
        align-items: center;
    }
    .bubble, .sub-objective {
        width: 90%;
    }
}
</style>