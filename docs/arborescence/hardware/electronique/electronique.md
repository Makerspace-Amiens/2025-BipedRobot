---
layout: default
nav_order: 2
title: Electronique et Capteurs
parent: Mécatronique et Systèmes
---

# Électronique et Capteurs

<hr>

<div style="background-color:rgba(225, 225, 225, 0.7); padding: 20px; text-align: justify;">
  Découvrez l'architecture électronique du robot, les composants clés et leurs fiches techniques détaillées. <strong>Explorez les cartes ci-dessous !</strong>
</div>

## Composants Clés
Cliquez sur une carte pour accéder à la fiche technique du composant.

<div class="cards-container">
  <!-- Carte 1 -->
  <div class="electronic-card">
    <h3>Servomoteurs Dynamixel AX-12</h3>
    <p><strong>Rôle :</strong> Les muscles du robot<br>
    • Font bouger les articulations<br>
    • Contrôlent précisément les mouvements<br>
    • Communiquent leur position</p>
    <div class="card-footer"><a href="{{site.baseurl}}/arborescence/hardware/electronique/dynamixel/dynamixel">Voir la fiche technique</a></div>
  </div>
    <!-- Carte 2 -->
  <div class="electronic-card">
    <h3>Microcontrôleur</h3>
    <p><strong>Rôle :</strong> Le cerveau du robot<br>
    • Reçoit et traite les informations<br>
    • Prend les décisions<br>
    • Commande les autres composants</p>
    <div class="card-footer"><a href="{{site.baseurl}}/arborescence/hardware/electronique/microcontroleur/microcontroleur">Voir la fiche technique</a></div>
  </div>
  
  <!-- Carte 3 -->
  <div class="electronic-card">
    <h3>Alimentation Secteur</h3>
    <p><strong>Rôle :</strong> Le cœur énergétique<br>
    • Fournit l'électricité à tout le système<br>
    • Convertit le courant secteur<br>
    • Protège contre les surtensions</p>
    <div class="card-footer"><a href="{{site.baseurl}}/arborescence/hardware/electronique/alimentation/alimentation">Voir la fiche technique</a></div>
  </div>
  
  <!-- Carte 4 -->
  <div class="electronic-card">
    <h3>Dynamixel Starter Kit</h3>
    <p><strong>Rôle :</strong> Boîte à outils des servos<br>
    • Interface de contrôle clé en main<br>
    • Permet de tester et configurer<br>
    • Facilite le développement</p>
    <div class="card-footer"><a href="{{site.baseurl}}/arborescence/hardware/electronique/dynamixel/starterkit">Voir la fiche technique</a></div>
  </div>
  
  <!-- Carte 5 -->
  <div class="electronic-card">
    <h3>Convertisseur DC/DC</h3>
    <p><strong>Rôle :</strong> Adaptateur de tension<br>
    • Ajuste la tension pour chaque composant<br>
    • Stabilise l'alimentation<br>
    • Optimise l'efficacité énergétique</p>
    <div class="card-footer"><a href="{{site.baseurl}}/arborescence/hardware/electronique/convertisseur/convertisseur">Voir la fiche technique</a></div>
  </div>
</div>

<style>
  :root {
    --primary: #1c5083;
    --secondary: #4a89dc;
    --text: #333;
    --light-gray: #f5f7fa;
  }

  .cards-container {
    display: grid;
    grid-template-columns: repeat(2, 2fr);
    gap: 25px;
    margin: 2rem 0;
    width: 100%;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
  }

  .card-link {
    text-decoration: none;
  }

  .electronic-card {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    border: 1px solid #e1e5eb;
    height: 100%;
  }

  .electronic-card h3 {
    color: var(--primary);
    margin: 0 0 1rem 0;
    font-size: 1.25rem;
    border-bottom: 2px solid var(--primary);
    padding-bottom: 0.5rem;
  }

  .electronic-card p {
    color: var(--text);
    margin: 0 0 1.5rem 0;
  }

  .card-footer {
    color: var(--primary);
    font-weight: 500;
    display: flex;
    align-items: center;
    font-size: 0.9rem;
  }

  .card-footer::before {
    content: "▶";
    margin-right: 8px;
    font-size: 0.8rem;
  }

  hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
}

  .electronic-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    border-color: var(--secondary);
  }

  /* Responsive pour mobile */
  @media (max-width: 768px) {
    .cards-container {
      grid-template-columns: 1fr !important;
      padding: 0 15px;
    }
  }
</style>
