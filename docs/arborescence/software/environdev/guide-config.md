---
layout: default
nav_exclude: true
title: Configuration Arduino - Seeeduino Xiao BLE
---

# Configuration Arduino - Seeeduino Xiao BLE

<hr>

<style>
:root {
    --primary-color: #1c5083;
    --secondary-color: #143c64;
    --accent-color: rgba(28, 80, 131, 0.1);
    --text-color: #333;
    --light-bg: #f8f9fa;
    --border-color: #ddd;
}

h2{
    color:var(--primary-color);
}

/* Typographie améliorée */
.content-wrapper {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}


/* Séparateur moderne */
hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
}

/* Encart d'introduction */
.intro-box {
    background-color: var(--light-bg);
    text-align:justify;
    padding: 1.25rem;
    margin: 1.5rem 0;
    border-radius: 0 4px 4px 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.url-copy-container {
  display: flex;
  align-items: center;
  margin: 1rem 0;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.url-display {
  flex-grow: 1;
  padding: 0.75rem 1rem;
  background-color: #f5f7fa;
  font-family: 'SF Mono', 'Roboto Mono', monospace;
  font-size: 0.9rem;
  color: #2d3748;
  overflow-x: auto;
  white-space: nowrap;
  border: 1px solid #e2e8f0;
  border-right: none;
  border-radius: 6px 0 0 6px;
}

.copy-button {
  position: relative;
  padding: 0.75rem 1.25rem;
  background-color: #4299e1;
  color: white;
  border: none;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  border-radius: 0 6px 6px 0;
}

.copy-button:hover {
  background-color: #3182ce;
}

.copy-icon {
  font-size: 1.1rem;
}

.copied-confirm {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #48bb78;
  opacity: 0;
  transition: opacity 0.2s ease;
  border-radius: 0 6px 6px 0;
}

.copy-button.copied .copy-text,
.copy-button.copied .copy-icon {
  opacity: 0;
}

.copy-button.copied .copied-confirm {
  opacity: 1;
}

/* Style des algorithmes */
.module-algorithms {
    margin-top: 0.75rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
}

.algorithm-link {
    display: inline-block;
    background-color: var(--accent-color);
    color: var(--primary-color);
    padding: 0.3rem 0.6rem;
    border-radius: 4px;
    text-decoration: none;
    transition: all 0.2s ease;
    border: 1px solid rgba(28, 80, 131, 0.2);
    font-size: 0.8rem;
    font-weight: 500;
}

.algorithm-link:hover {
    background-color: var(--primary-color);
    color: white;
    transform: translateY(-1px);
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

/* Tableau amélioré */
.table-container {
    overflow-x: auto;
    margin: 2rem 0;
    border-radius: 6px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.tg {
    border-collapse: collapse;
    border-spacing: 0;
    width: 100%;
    margin: 0 auto;
}

.tg td {
    border: 1px solid var(--border-color);
    padding: 12px 15px;
    font-size: 0.9rem;
    line-height: 1.5;
}

.tg th {
    border: 1px solid var(--border-color);
    background-color: var(--primary-color);
    color: white;
    padding: 14px 15px;
    font-weight: 600;
    text-align: left;
}

.tg tr:nth-child(even) {
    background-color: var(--light-bg);
}

.tg tr:hover {
    background-color: rgba(28, 80, 131, 0.05);
}

/* Section centrée */
.section-header {
    text-align: center;
    margin: 2rem 0;
    position: relative;
    color: var(--primary-color);
}

.section-header:after {
    content: "";
    display: block;
    width: 120px;
    height: 3px;
    background: var(--primary-color);
    margin: 1rem auto 0;
}

/* Responsive */
@media (max-width: 768px) {
    .tg td, .tg th {
        padding: 8px 10px;
        font-size: 0.85rem;
    }
}
</style>

<script>

function copyToClipboard(elementId) {
  const element = document.getElementById(elementId);
  const text = element.textContent.trim();
  navigator.clipboard.writeText(text);
  
  const button = element.nextElementSibling;
  button.classList.add('copied');
  
  setTimeout(() => {
    button.classList.remove('copied');
  }, 2000);
}
</script>

<div style="text-align:justify; background-color:rgba(168, 168, 168, 0.16);">
<p>Ce guide vous explique comment configurer l'IDE Arduino pour pouvoir programmer notre carte Seeeduino Xiao BLE (nRF52840). Cliquez sur le lien suivant pour accéder à la documentation du constructeur : <a href="https://wiki.seeedstudio.com/XIAO_BLE/"> Seeedstudio Xiao BLE </a></p>
</div >

## **Étape 1 : Installation de l'IDE Arduino**

<img src="{{site.baseurl}}/assets/img/logos/arduino.png" style="display: block; margin: 50px auto 50px auto; max-width: 150px; height: auto;">

<div style="text-align:justify;">
L’Arduino IDE est un environnement de développement gratuit et open-source conçu pour programmer facilement des cartes électroniques Arduino.  Si ce n'est pas déjà fait, téléchargez et installez la dernière version de l'IDE Arduino depuis le site officiel : 
<a href="https://www.arduino.cc/en/software"> Site Officiel Arduino </a>. Suivez les instructions d'installation pour votre système d'exploitation.
</div>

## **Étape 2 : Ajout de l'URL de Gestion des Cartes Seeeduino**

L'IDE Arduino nécessite une URL supplémentaire pour pouvoir télécharger les informations et les pilotes nécessaires pour les cartes Seeeduino. Veuillez suivre les étapes suivantes : 

1.  Ouvrez l'IDE Arduino.
2.  Cliquez sur `Fichier` dans la barre de menu, puis sélectionnez `Préférences`.
3.  Dans la fenêtre "Préférences", repérez le champ "URLs de gestion des cartes supplémentaires".
4.  Ajoutez l'URL suivante à ce champ :

<div class="url-copy-container">
  <div class="url-display" id="seeed-link">
    https://files.seeedstudio.com/arduino/package_seeeduino_boards_index.json
  </div>
  <button class="copy-button" onclick="copyToClipboard('seeed-link')">
    <span class="copy-icon">⎘</span>
    <span class="copy-text">Copier</span>
    <span class="copied-confirm">Copié !</span>
  </button>
</div>


Cliquez sur `OK` pour valider et enregistrer les modifications

## **Étape 3 : Installation du Package de la Carte Seeeduino nRF52**

Maintenant, nous pouvons télécharger et installer le support pour la Seeeduino Xiao BLE. 

<div style="display: flex; align-items: flex-start; gap: 20px;">
  <img src="{{site.baseurl}}/assets/img/arduino-config/boardmanager.png" alt="Board Manager" style="height: 500px;">
  
  <div style="max-width: 500px;">
    <ol>
      <li style="margin-bottom: 20px;">Dans l'IDE Arduino, allez dans <code>Tools</code> > <code>Board</code> > <code>Board Manager</code>. Vous allez tomber sur l'interface présente à gauche.</li>
      <li style="margin-bottom: 20px;">Tapez dans la barre de recherche <code>seeeduino nrf</code> et choisissez le package encadré en bleu </li>
    </ol>
  </div>
</div>

## **Étape 4 : Sélection de la Carte Seeeduino Xiao BLE**

Vous devez maintenant indiquer à l'IDE Arduino que vous travaillez avec une Seeeduino Xiao BLE.

1.  Allez dans le menu `Tools`, puis `Boards`.
2.  Recherchez dans la liste et sélectionnez l'entrée correspondant à votre carte. Elle devrait s'appeler `Seeeduino XIAO nRF52840 Sense`.

## **Étape 5 : Connexion de la Carte et Sélection du Port Série**

<div style="text-align: justify; max-width: 800px;">

  <p>
    Connectez votre carte Seeeduino Xiao BLE à votre ordinateur à l'aide d'un câble USB. L'IDE Arduino communique avec votre carte via le port série USB. Vous devez sélectionner le bon port.
  </p>

  <ol style="margin-left: 1em; margin-bottom: 1em;">
    <li>Allez dans le menu <code>Tools</code>, puis <code>Port</code>.</li>
    <li>Une liste des ports série disponibles s'affiche. Identifiez le port qui correspond à votre Seeeduino Xiao BLE. Sur Windows, il apparaît souvent avec un nom comme <code>COMx</code> (où x est un numéro). Si vous n'êtes pas sûr, essayez de débrancher et de rebrancher la carte pour voir quel port disparaît et réapparaît.</li>
    <li>Cliquez sur le port correspondant à votre Seeeduino Xiao nRF52840 Sense pour le sélectionner.</li>
  </ol>

  <p>
    Votre environnement de développement Arduino est maintenant configuré pour travailler avec la Seeeduino Xiao BLE (nRF52840). Vous pouvez commencer à écrire et à téléverser du code sur votre carte.
  </p>

</div>
