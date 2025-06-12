---
layout: default
nav_order: 1
title: Architecture Matérielle
parent: Mécatronique et Systèmes
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
</style>

# Architecture Matérielle

<div class="header-divider"></div>

## Conception mécanique en 3 phases

<h3 class="phase-title">Phase 1 : Prototype initial</h3>

<p><strong>Composition :</strong></p>
<ul class="feature-list">
    <li>Liaison bassin entre les deux jambes</li>
    <li>8 servomoteurs</li>
    <li>Hanche</li>
    <li>Cuisse</li>
    <li>Tibia</li>
    <li>Pied</li>
</ul>

<p><strong>Difficultés rencontrées :</strong></p>
<ul class="feature-list">
    <li>Frottements importants entre les pièces imprimées en 3D</li>
    <li>Jeu mécanique insuffisant pour assurer la fluidité des mouvements</li>
</ul>

<h3 class="phase-title">Phase 2 : Solution Robot Araignée</h3>
<p>Réutilisation du châssis du robot araignée de l'association Unimakers d'Unilasalle Amiens :</p>

<div class="img-container">
    <img src="{{site.baseurl}}/assets/img/meca/araignee.png" alt="Robot Araignée Unimakers" style="width: 50%;">
    <div class="img-caption">Robot Araignée Unimakers</div>
</div>

<p><strong>Avantages :</strong></p>
<ul class="feature-list">
    <li>Structure métallique robuste (6 pattes avec 3 servomoteurs chacune)</li>
    <li>Support idéal pour l'électronique embarquée</li>
    <li>Réutilisation de 2 pattes pour notre projet bipède</li>
    <li>Supports métalliques démontables offrant :</li>
    <ul class="feature-list">
        <li>Meilleure rigidité structurelle</li>
        <li>Précision articulaire accrue</li>
        <li>Maintenance facilitée</li>
    </ul>
</ul>

<h3 class="phase-title">Phase 3 : Modèle Final</h3>

<p><strong>Conception 3D sous Onshape :</strong></p>
<ul class="feature-list">
    <li><strong>Châssis central :</strong> Structure de cohésion avec surface plane pour l'électronique</li>
    <li><strong>2 pieds</strong> optimisés pour la stabilité</li>
</ul>

<p><strong>Architecture des jambes :</strong></p>
<ul class="feature-list">
    <li><strong>Hanche :</strong> Rotation latérale</li>
    <li><strong>Genou :</strong> Flexion/extension dans le plan sagittal</li>
    <li><strong>Cheville :</strong> Adaptation de l'angle du pied</li>
    <li><strong>Assemblage :</strong> Vis M2 et M3 pour l'interconnexion des segments</li>
</ul>

<div class="img-container">
    <img src="{{site.baseurl}}/assets/img/meca/articulations.png" alt="Schéma du robot final">
    <div class="img-caption">Architecture articulaire du robot bipède</div>
</div>
