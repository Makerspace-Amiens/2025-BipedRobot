---
layout: default
nav_exclude: true
title: Contrainte et Sécurité
---

<style>
:root {
    --primary-color: #1c5083;
    --secondary-color: #0d2b4e;
    --accent-color: rgba(28, 80, 131, 0.15);
    --text-color: #2d3748;
    --light-bg: #f8fafc;
    --border-color: #e2e8f0;
    --angle-color: #1c5083;
    --speed-color: #dd6b20;
    --warning-color: #c53030;
    --code-bg: #f0f5ff;
}

body {
    font-family: 'Segoe UI', system-ui, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 2rem 0;
}

.intro-box {
    background-color: var(--accent-color);
    border-left: 4px solid var(--primary-color);
    padding: 1.25rem;
    border-radius: 0 8px 8px 0;
    margin: 1.5rem 0;
}

.table-container {
    overflow-x: auto;
    margin: 2rem 0;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    background: white;
    border: 1px solid var(--border-color);
}

h1 {
    color: var(--secondary-color);
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 0.5rem;
    margin-bottom: 1.5rem;
}

h2 {
    color: var(--primary-color);
    margin: 2rem 0 1rem 0;
    position: relative;
    padding-left: 1.2rem;
}

h2:before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.35em;
    height: 1em;
    width: 5px;
    background: linear-gradient(to bottom, var(--primary-color), var(--secondary-color));
    border-radius: 3px;
}

h3 {
    color: var(--secondary-color);
    margin: 1.5rem 0 0.8rem 0;
    font-weight: 600;
}

h4 {
    font-weight: 600;
    color: var(--secondary-color);
    margin: 1.5rem 0 0.8rem 0;
    padding-bottom: 0.3rem;
    border-bottom: 2px solid rgba(13, 43, 78, 0.1);
    display: inline-block;
}

.tg {
    border-collapse: collapse;
    width: 100%;
    font-size: 0.9rem;
    table-layout: fixed;
}

.tg thead {
    position: sticky;
    top: 0;
}

.tg th {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    padding: 12px 10px;
    font-weight: 600;
    text-align: left;
    border: none;
}

.tg th:first-child {
    border-top-left-radius: 8px;
}

.tg th:last-child {
    border-top-right-radius: 8px;
}

.tg td {
    padding: 10px 10px;
    border-bottom: 1px solid var(--border-color);
    vertical-align: middle;
    word-wrap: break-word;
}

.tg tr:nth-child(even) {
    background-color: var(--light-bg);
}

.tg tr:hover td {
    background-color: var(--accent-color);
}

.tg .angle {
    color: var(--angle-color);
    font-weight: 500;
    text-align: center;
}

.tg .speed {
    color: var(--speed-color);
    font-weight: 500;
    text-align: center;
}

.warning-box {
    background-color: rgba(197, 48, 48, 0.08);
    border-left: 4px solid var(--warning-color);
    padding: 1rem;
    border-radius: 0 8px 8px 0;
    margin: 1.5rem 0;
}

code {
    background-color: var(--code-bg);
    padding: 0.2em 0.4em;
    border-radius: 4px;
    font-family: 'SFMono-Regular', Consolas, monospace;
    font-size: 0.9em;
    color: #2d3748;
}

ol, ul {
    padding-left: 1.5rem;
    margin: 1rem 0;
}

li {
    margin-bottom: 0.5rem;
    position: relative;
}

/* Ajustement des largeurs de colonnes */
.tg th:nth-child(1), .tg td:nth-child(1) { width: 5%; }
.tg th:nth-child(2), .tg td:nth-child(2) { width: 20%; }
.tg th:nth-child(3), .tg td:nth-child(3) { width: 15%; }
.tg th:nth-child(4), .tg td:nth-child(4) { width: 12%; }
.tg th:nth-child(5), .tg td:nth-child(5) { width: 10%; }
.tg th:nth-child(6), .tg td:nth-child(6) { width: 10%; }
.tg th:nth-child(7), .tg td:nth-child(7) { width: 10%; }

@media (max-width: 768px) {
    .tg {
        font-size: 0.8rem;
    }
    .tg th, .tg td {
        padding: 8px 6px;
    }
}
</style>

# Contraintes et Sécurité

<div class="intro-box">
Garantir l'intégrité des composants mécaniques et électroniques du robot bipède en limitant les valeurs critiques (angle, vitesse, température) via le logiciel de contrôle moteur.
</div>

## Paramètres des servomoteurs

Chaque servomoteur possède des limites définies manuellement selon sa position mécanique dans le robot. Ces limites permettent de restreindre :

1. **L'amplitude angulaire** - ex: `min_angle`, `max_angle`
2. **La vitesse maximale autorisée** - ex: `max_speed`

<div class="table-container">
<table class="tg">
  <thead>
    <tr>
      <th>#</th>
      <th>Servomoteur</th>
      <th>Position</th>
      <th>Axe</th>
      <th>Min</th>
      <th>Max</th>
      <th>Vitesse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Genou gauche</td>
      <td>Articulation</td>
      <td>Pitch</td>
      <td class="angle">0°</td>
      <td class="angle">90°</td>
      <td class="speed">60°/s</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Genou droit</td>
      <td>Articulation</td>
      <td>Pitch</td>
      <td class="angle">0°</td>
      <td class="angle">90°</td>
      <td class="speed">60°/s</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Hanche G. Pitch</td>
      <td>Bassin</td>
      <td>Av/Ar</td>
      <td class="angle">-45°</td>
      <td class="angle">+45°</td>
      <td class="speed">50°/s</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Hanche G. Roll</td>
      <td>Bassin</td>
      <td>Latéral</td>
      <td class="angle">-20°</td>
      <td class="angle">+20°</td>
      <td class="speed">40°/s</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Hanche G. Yaw</td>
      <td>Bassin</td>
      <td>Rotation</td>
      <td class="angle">-25°</td>
      <td class="angle">+25°</td>
      <td class="speed">40°/s</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Hanche D. Pitch</td>
      <td>Bassin</td>
      <td>Av/Ar</td>
      <td class="angle">-45°</td>
      <td class="angle">+45°</td>
      <td class="speed">50°/s</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Hanche D. Roll</td>
      <td>Bassin</td>
      <td>Latéral</td>
      <td class="angle">-20°</td>
      <td class="angle">+20°</td>
      <td class="speed">40°/s</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Hanche D. Yaw</td>
      <td>Bassin</td>
      <td>Rotation</td>
      <td class="angle">-25°</td>
      <td class="angle">+25°</td>
      <td class="speed">40°/s</td>
    </tr>
  </tbody>
</table>
</div>

### Conversion Angle – Dynamixel

Les servomoteurs Dynamixel utilisent une unité interne codée sur 10 bits (0-1023), représentant une plage de 0° à 300°. Deux fonctions assurent la conversion :

- `angle_to_dxl(angle_deg)` : convertit un angle en degrés vers une position Dynamixel
- `dxl_to_angle(position)` : convertit une position Dynamixel en degrés

Ces conversions sont indispensables pour garantir la cohérence des mouvements avec les limites imposées.

### Envoi de commande sécurisé

Avant l'envoi d'une commande à un moteur, une vérification est systématiquement effectuée :

1. Contrôle que la cible est dans l'intervalle autorisé (`min_angle` ≤ angle ≤ `max_angle`)
2. Contrôle que la vitesse reste dans les limites (`speed` ≤ `max_speed`)
3. Conversion en unité Dynamixel
4. Envoi via `write_word` avec gestion des erreurs

<div class="warning-box">
Toute violation déclenche une exception ou un arrêt d'urgence pour éviter tout dommage matériel.
</div>

## Protection du robot – Arrêt d'urgence

### Surveillance thermique

La température interne des servomoteurs est régulièrement surveillée à l'aide de la commande `read_byte`. Le seuil critique est fixé à **70°C**. En cas de dépassement :

- Message d'erreur affiché immédiatement
- Coupure de couple via `Torque Enable = 0`
- Enregistrement d'un log détaillé pour analyse

### Activation de l'arrêt d'urgence

L'arrêt d'urgence peut être déclenché :

- **Automatiquement** (température, erreur critique, dépassement de limite)
- **Manuellement** (bouton physique ou commande logicielle)

### Comportement de la fonction `emergency_shutdown()`

1. Désactivation immédiate du couple sur tous les moteurs
2. Blocage de l'exécution du programme
3. Affichage du statut d'urgence
4. Enregistrement des paramètres critiques