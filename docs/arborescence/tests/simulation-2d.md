---
layout: default
nav_order: 1
title: Simulation 2D
parent: Tests et Validation
---

# Simulation 2D de la Marche

<hr>

<div class="card">
<div style="text-align:justify">
<strong>Objectifs :</strong> Visualiser la cinématique de marche du robot via une modélisation 2D simplifiée en Python pour tester les stratégies de marche et mieux appréhender les concepts liés à la locomotion robotique humanoïde.
</div>
</div>

<div style="position: relative; width: 100%; padding-bottom: 56.25%;">
  <iframe
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    src="https://www.youtube.com/embed/dlNgZRaJvbg"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen
  ></iframe>
</div>

## <span class="section-title">Basé sur la biomécanique humaine</span>

<div style="text-align:justify; margin-top:20px;">
Le robot est conçu pour reproduire la dynamique de la marche humaine à travers une simplification du système locomoteur. Les segments (cuisse, tibia, pied) sont modélisés par des traits articulés, et le mouvement suit un cycle périodique.
</div>

<h3 style="color:rgb(16, 49, 77)">• Cycle de Marche</h3>

<figure style="margin: 20px 0; text-align: center;">
  <img src="{{site.baseurl}}/assets/img/simulation-2d/cycle_marche.png"
       alt="Phases et sous-phases du cycle de marche selon Perry et al. (1992)"
       style="max-width: 100%; height: auto; border: 1px solid #eee; padding: 5px;">
  <figcaption style="margin-top: 10px; font-style: italic; text-align: left; max-width: 800px; margin-left: auto; margin-right: auto;">
    <p style="margin-bottom: 8px; text-align:center"><strong>Figure :</strong> Définition des phases et sous-phases du cycle de marche selon Perry et al. (1992).</p>
    <p style="margin: 5px 0; text-align:center;">Les rôles des articulations du genou et de la cheville sont indiqués pour chaque phase.</p>
  </figcaption>
</figure>

<div style="margin-top:25px">
  <h3 style="color:rgb(16, 49, 77)">• Descriptif détaillé de chaque pas</h3>
</div>

<ul style="margin-left: 20px; margin-top:20px;">
  <li><strong>Contact Initial (Initial Contact):</strong> Instant où le pied entre en contact avec le sol.</li>
  <li><strong>Réponse au Chargement (Loading Response):</strong> Transfert du poids sur la jambe d'appui.</li>
  <li><strong>Appui Medio-Plantaire (Mid Stance):</strong> Le corps progresse au-dessus du pied d'appui.</li>
  <li><strong>Appui Propulsif (Terminal Stance):</strong> Poussée vers l'avant initiée par la cheville.</li>
  <li><strong>Pré-Oscillation (Pre-Swing):</strong> Préparation au soulèvement du pied.</li>
  <li><strong>Oscillation Initiale (Initial Swing):</strong> Le pied quitte le sol et commence à avancer.</li>
  <li><strong>Oscillation Medio-Pied (Mid Swing):</strong> La jambe avance sous le corps.</li>
  <li><strong>Oscillation Terminale (Terminal Swing):</strong> Préparation à la prise de contact du pied.</li>
  <li><strong>Préparation au Contact (Swing Preparation):</strong> Phase de décélération de la jambe oscillante.</li>
  <li><strong>Placement du Pied (Foot Placement):</strong> Le pied se positionne pour le prochain contact.</li>
</ul>

<p style="text-align:justify;">La progression à travers ces phases est déterminée par le temps et la fréquence des pas.</p>

<div style="margin-top:25px">
  <h3 style="color:rgb(16, 49, 77)">• Paramètres du corps humain (Référence pour la simulation)</h3>
</div>

<p style="text-align:justify;">
  Les dimensions physiques du robot dans cette simulation sont basées sur les mesures d'un étudiant spécifique. Ces valeurs ont été utilisées comme référence pour définir les longueurs des segments (cuisse, tibia, pied) et la hauteur de la hanche du modèle virtuel, influençant directement la cinématique de la marche simulée. Il est important de noter que ces mesures sont spécifiques à cet individu et peuvent varier considérablement pour d'autres personnes.
</p>

<ul style="margin-left: 20px;">
  <li><strong>Longueur de la cuisse:</strong> 0.47 mètre (distance entre la hanche et le genou)</li>
  <li><strong>Longueur du tibia:</strong> 0.45 mètre (distance entre le genou et la cheville)</li>
  <li><strong>Longueur du pied:</strong> 0.25 mètre (distance de la cheville à l'extrémité du pied)</li>
  <li><strong>Hauteur de la hanche:</strong> 0.92 mètre (hauteur verticale du centre de la hanche par rapport au sol en position debout)</li>
</ul>

<p style="text-align:justify;">
  Ces paramètres servent de base pour les longueurs des segments définies dans la section "Contraintes Physiques".
</p>

<div style="margin-top:25px; margin-top:20px; margin-bottom:20px;">
  <h3 style="color:rgb(16, 49, 77)">• Contraintes Physiques</h3>
</div>

<div class="table-container">
  <table class="table">
    <thead>
      <tr>
        <th style="padding: 14px 16px; text-align: left; color: white; background-color:rgb(25, 61, 98); font-size: 0.85rem;"><strong>Contrainte</strong></th>
        <th style="padding: 14px 16px; text-align: left; color: white; background-color: rgb(25, 61, 98); font-size: 0.85rem;"><strong>Description</strong></th>
        <th style="padding: 14px 16px; text-align: left; color: white; background-color:rgb(25, 61, 98); font-size: 0.85rem;"><strong>Valeur (unité)</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Longueur des Segments</td>
        <td>Les longueurs de la cuisse, du tibia et du pied sont fixes.</td>
        <td>Cuisse: 0.47 m, Tibia: 0.45 m, Pied: 0.25 m</td>
      </tr>
      <tr>
        <td>Niveau du Sol</td>
        <td>Le contact avec le sol se produit à une hauteur verticale de 0 m.</td>
        <td>0 m</td>
      </tr>
      <tr>
        <td>Dégagement du Pied</td>
        <td>Le pied oscillant doit atteindre un dégagement vertical pour éviter de heurter le sol.</td>
        <td>0.12 m (amplitude maximale)</td>
      </tr>
      <tr>
        <td>Fréquence des Pas</td>
        <td>Le rythme de la marche est maintenu à une fréquence constante.</td>
        <td>1.1 Hz</td>
      </tr>
      <tr>
        <td>Longueur des Pas</td>
        <td>La distance parcourue à chaque pas est relativement constante.</td>
        <td>0.65 m</td>
      </tr>
      <tr>
        <td>Mouvement du Bassin</td>
        <td>Le mouvement du bassin (tangage, roulis, déplacement horizontal) suit des oscillations sinusoïdales avec des amplitudes définies.</td>
        <td>Tangage: 0.06 rad, Roulis: 0.03 rad, Déplacement horizontal: Amplitude spécifiée dans le code</td>
      </tr>
      <tr>
        <td>Contact au Sol</td>
        <td>Pendant les phases d'appui, le pied est contraint de rester au niveau du sol. La position horizontale du point de contact est mise à jour à chaque nouveau contact initial.</td>
        <td>Position horizontale variable, hauteur = 0 m</td>
      </tr>
      <tr>
        <td>Angles Articulaires</td>
        <td>Les angles des articulations de la hanche, du genou et de la cheville sont interpolés de manière lissée entre des valeurs prédéfinies pour chaque phase du cycle de marche.</td>
        <td>Variables en fonction de la phase</td>
      </tr>
    </tbody>
  </table>
</div>
<h3 style="color:rgb(16, 49, 77)">• Interpolation des Angles Articulaires</h3>
  <div class="section-content">
    <p>
      Pour générer un mouvement de marche fluide et coordonné, les angles des différentes articulations du robot (hanche, genou, cheville) évoluent continuellement au cours du cycle de marche. L'interpolation est une technique mathématique utilisée pour estimer des valeurs entre des points de données connus.
    </p>
    <div class="highlight-box">
      <p>
        <strong>Méthode :</strong> Nous utilisons une interpolation cubique lissée qui permet :
      </p>
      <ul>
        <li>Des transitions douces en position, vitesse et accélération</li>
        <li>Une représentation mathématique par polynômes de degré trois</li>
        <li>Un ajustement précis via les conditions aux limites</li>
      </ul>
    </div>
      <ul>
        <li><strong>Continuité du mouvement:</strong> Évite les changements brusques de posture irréalistes</li>
        <li><strong>Facilité de contrôle:</strong>Trajectoires lisses pour les actionneurs du robot</li>
        <li><strong>Flexibilité d'ajustement:</strong> Modification facile des angles clés pour différentes démarches</li>
      </ul>
  <div>
  <h3 style="color:rgb(16, 49, 77)">• Modélisation du Mouvement du Bassin</h3>
  <div class="section-content">
    <p>
      Le mouvement du bassin joue un rôle clé dans la marche humaine, contribuant à l'équilibre et à la fluidité du mouvement. Notre modélisation 2D intègre :
    </p>
      <ul>
        <li><strong>Tangage (Pelvic Tilt):</strong> Inclinaison avant/arrière autour d'un axe transversal</li>
        <li><strong>Déplacement Vertical (Pelvic Height):</strong>Variation de hauteur pendant le cycle de marche (influence sur la hauteur des hanches)</li>
        <li><strong>Roulis (Pelvic Rotation):</strong>Rotation verticale favorisant l'avancée de la hanche</li>
        <li><strong>Déplacement Horizontal (Pelvic Sway):</strong> Mouvement latéral du bassin</li>
      </ul>
    <div class="technical-note">
      <p>
        <strong>Note technique :</strong> Ces mouvements sont modélisés par des fonctions sinusoïdales paramétrables (amplitude, fréquence, phase) permettant de simuler différentes caractéristiques de marche. Les amplitudes pour le tangage, le roulis et le déplacement horizontal sont définies dans le code.
      </p>
    </div>
  </div>
<h3 style="color:rgb(16, 49, 77)">• Gestion du Contact au Sol et de l'Oscillation</h3>
  <div class="phase-container">
    <div class="phase-card contact-phase">
      <h4>Contact au Sol</h4>
      <ul class="phase-details">
        <li>Pied maintenu à z = 0 (niveau du sol)</li>
        <li>Position horizontale évolutive avec la progression</li>
        <li>Détection précise des transitions entre phases</li>
        <li>Prévention de la pénétration dans le sol</li>
      </ul>
    </div>
    <div class="phase-card swing-phase">
      <h4>Phase d'Oscillation</h4>
      <ul class="phase-details">
        <li>Décalage vertical du pied basé sur une fonction parabolique pour le dégagement</li>
        <li>Hauteur de dégagement maximale de 0.12 m</li>
        <li>La trajectoire vise à assurer un dégagement suffisant pour éviter les collisions</li>
        <li>Le placement précis du pied pour le prochain contact est géré</li>
      </ul>
    </div>
  </div>

  <div class="transition-note">
    <p>
      <strong>Transition :</strong> Le passage entre phases est déterminé par la progression dans le cycle (pourcentage) ou par des critères spécifiques (temps écoulé).
    </p>
  </div>

<div style="background-color: #f5f7fa; padding: 1em 1.2em; border-radius: 6px; margin-top: 1.5em; border-left: 3px solid #4a6ea9;">
    <div style="font-size: 14px; color: #555; margin-bottom: 6px;">
        <strong>Si vous voulez accéder directement au code :</strong> 
    </div>
    <div style="font-size: 14px;">
        <a href="{{site.baseurl}}/assets/img/simulation-2d/V2_2_0.marche.py" style="color: #2a6496; text-decoration: none; font-weight: 500;">
            Télécharger le code (fichier Python)
        </a>
    </div>
</div>

<style>

:root {
  --primary-color: rgb(28, 80, 131);
  --secondary-color: rgb(28, 80, 131);
  --accent-color: rgb(28, 80, 131);
}

hr {
  border: none;
  height: 2px;
  background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
  margin: 1.5rem 0;
}

.card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}

.section-title {
  color: var(--primary-color);
  border-bottom: 2px solid var(--accent-color);
  padding-bottom: 0.5rem;
  margin-top: 2rem;
  margin-bottom: 1rem;
}

.subsection {
  margin: 1.5rem 0;
  padding-left: 1rem;
  border-left: 3px solid var(--accent-color);
}

.content-section {
  margin: 2rem 0;
  font-family: 'Segoe UI', Roboto, sans-serif;
}

.section-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  padding: 1.5rem;
  margin-bottom: 2rem;
  border-left: 4px solid #1c5083;
  transition: transform 0.3s ease;
}

.section-card:hover {
  transform: translateY(-3px);
}

.section-title {
  color: #1c5083;
  font-size: 1.4rem;
  margin-bottom: 1.2rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #63a4ff;
  display: flex;
  align-items: center;
}

.icon-spacing {
  margin-right: 10px;
  color: #3a7cb9;
}

.highlight-box {
  background: #f8fafc;
  border-radius: 8px;
  padding: 1rem;
  margin: 1.2rem 0;
  border-left: 3px solid #63a4ff;
}

.styled-list {
  padding-left: 1.5rem;
  list-style-type: none;
}

.movement-types {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin: 1.5rem 0;
}

.movement-type {
  flex: 1;
  min-width: 200px;
  background: #f8fafc;
  padding: 1rem;
  border-radius: 8px;
}

.movement-icon {
  margin-right: 8px;
}

.phase-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.phase-card {
  flex: 1;
  min-width: 250px;
  padding: 1.2rem;
  border-radius: 8px;
}

.contact-phase {
  background: #f0f7ff;
  border-left: 4px solid #1c5083;
}

.swing-phase {
  background: #fff0f7;
  border-left: 4px solid #c93d72;
}

.phase-details {
  list-style-type: none;
  padding-left: 0;
}

.phase-details li {
  margin-bottom: 0.6rem;
  padding-left: 1.5rem;
  position: relative;
}