---
layout: default
nav_order: 2
title: 1er Prototype Mécanique 
parent: Tests et Validation
---

<style>
:root {
    --primary-color: #1c5083;
    --secondary-color: #0d2b4e;
    --accent-color: rgba(28, 80, 131, 0.15);
    --text-color: #2d3748;
    --light-bg: #f8fafc;
    --border-color: #e2e8f0;
}

.header-divider {
    border: none;
    height: 3px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
    border-radius: 3px;
}

.phase-title {
    color: var(--primary-color);
    font-weight: 600;
    margin-bottom: 0.8rem;
}

.img-container {
    text-align: center;
    margin: 1.5rem 0;
}

.img-container img {
    max-width: 100%;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.img-caption {
    font-style: italic;
    color: var(--secondary-color);
    margin-top: 0.5rem;
    font-size: 0.9em;
}

ul.feature-list {
    padding-left: 1.2rem;
}

ul.feature-list li {
    margin-bottom: 0.5rem;
    position: relative;
    list-style-type: none;
}

ul.feature-list li:before {
    content: "•";
    color: var(--primary-color);
    font-weight: bold;
    display: inline-block;
    width: 1em;
    margin-left: -1em;
}

.specs-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
}

.specs-table th {
    background-color: var(--accent-color);
    padding: 0.75rem;
    text-align: left;
}

.specs-table td {
    padding: 0.75rem;
    border-bottom: 1px solid var(--border-color);
}
</style>

# Premier Prototype Mécanique

<div class="header-divider"></div>

## 1. Présentation Générale

<p><strong>Caractéristiques principales :</strong></p>
<ul class="feature-list">
    <li>4 parties mécaniques principales</li>
    <li>6 servomoteurs Dynamixel AX-12A</li>
    <li>Structure légère en aluminium/composite</li>
</ul>

<div class="img-container">
    <img src="{{site.baseurl}}/assets/img/meca/proto.jpg" alt="Vue d'ensemble du prototype">
    <div class="img-caption">Premier prototype mécanique du robot bipède</div>
</div>

## 2. Composition Mécanique

<h3 class="phase-title">Structure Générale</h3>

<table class="specs-table">
    <thead>
        <tr>
            <th>Composant</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Partie supérieure</strong> (bassin)</td>
            <td>Support de la structure et fixation des jambes</td>
        </tr>
        <tr>
            <td><strong>Cuisse</strong> (x2)</td>
            <td>Transmission mouvement hanche-genou</td>
        </tr>
        <tr>
            <td><strong>Tibia</strong> (x2)</td>
            <td>Transmission mouvement genou-pied</td>
        </tr>
        <tr>
            <td><strong>Pied</strong> (x2)</td>
            <td>Support au sol (fixe dans ce prototype)</td>
        </tr>
    </tbody>
</table>

<h3 class="phase-title">Détails des composants</h3>

<p><strong>Partie Supérieure (Bassin)</strong></p>
<div class="img-container">
    <img src="{{site.baseurl}}/assets/img/meca/partie_superieur.jpg" alt="Partie supérieure">
    <div class="img-caption">Structure centrale de fixation</div>
</div>
<ul class="feature-list">
    <li><strong>Rôle :</strong> Structure centrale de fixation</li>
    <li><strong>Matériau :</strong> Aluminium/composite léger</li>
    <li><strong>Composants :</strong> Fixation des 2 servomoteurs de hanche</li>
</ul>

<p><strong>Cuisse</strong></p>
<div class="img-container">
    <img src="{{site.baseurl}}/assets/img/meca/thumbnail_cuisse.jpg" alt="Cuisse">
    <div class="img-caption">Segment cuisse avec servomoteur</div>
</div>
<ul class="feature-list">
    <li>1 servomoteur Dynamixel AX-12A par cuisse</li>
    <li>Liaison hanche-genou</li>
</ul>

## 3. Servomoteurs Dynamixel AX-12A

<p><strong>Spécifications techniques :</strong></p>
<ul class="feature-list">
    <li>Quantité totale : 6 unités</li>
    <li>Contrôle : Bus série TTL (Daisy-chain)</li>
    <li>Couple max : ~15 kg.cm (à 12V)</li>
    <li>Angle de rotation : 300°</li>
</ul>

<table class="specs-table">
    <thead>
        <tr>
            <th>Position</th>
            <th>Quantité</th>
            <th>Fonction</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Hanche gauche</td>
            <td>1</td>
            <td>Rotation horizontale jambe gauche</td>
        </tr>
        <tr>
            <td>Hanche droite</td>
            <td>1</td>
            <td>Rotation horizontale jambe droite</td>
        </tr>
        <tr>
            <td>Genou gauche</td>
            <td>1</td>
            <td>Flexion/extension cuisse-tibia</td>
        </tr>
        <tr>
            <td>Genou droit</td>
            <td>1</td>
            <td>Flexion/extension cuisse-tibia</td>
        </tr>
        <tr>
            <td>Cheville gauche</td>
            <td>1</td>
            <td>Mouvement tibia-pied (optionnel)</td>
        </tr>
        <tr>
            <td>Cheville droite</td>
            <td>1</td>
            <td>Mouvement tibia-pied (optionnel)</td>
        </tr>
    </tbody>
</table>

## 4. Remarques Techniques

<ul class="feature-list">
    <li> Pas de système de stabilisation active (IMU/gyroscope) dans cette version</li>
    <li>Alimentation et contrôleur non visibles (documentation électronique séparée)</li>
    <li>Pieds à axe fixe pour simplifier l'équilibrage passif</li>
    <li>Prototype conçu pour validation mécanique de base</li>
</ul>