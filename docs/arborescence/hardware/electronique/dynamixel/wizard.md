---
layout: default
nav_exclude: true
title: Dynamixel Wizard 2.0
---

<style>
:root {
    --primary-color: #1c5083;
    --secondary-color: #3a7cb9;
    --accent-color: #5fa8f3;
    --light-bg: #f8fafc;
    --border-color: #e2e8f0;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
}

.card {
    background: white;
    border-radius: 12px;
    border: 1px solid black; 
    box-shadow: 0 2px 10px rgba(17, 17, 17, 0.1);
    padding: 20px;
    margin: 20px 0;
}


.img-container {
    text-align: center;
    margin: 30px 0;
}

.img-container img {
    max-width: 200px;
    height: auto;
}

.requirements-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
    margin: 20px 0;
}

.requirement-item {
    background: var(--light-bg);
    padding: 15px;
    border-radius: 5px;
    border-left: 4px solid var(--accent-color);
}

.step {
    margin-bottom: 25px;
    padding-bottom: 15px;
    border-bottom: 1px dashed var(--border-color);
}

.step-number {
    display: inline-block;
    background: var(--primary-color);
    color: white;
    width: 15px;
    height: 15px;
    text-align: center;
    border-radius: 50%;
    margin-right: 10px;
    line-height: 25px;
}
</style>

# Guide Complet Dynamixel Wizard 2.0

<hr>

<div style="background-color:rgba(225, 225, 225, 0.7); padding: 20px; text-align: justify;">
  Dynamixel Wizard est un logiciel de configuration et de diagnostic développé par ROBOTIS pour ses servomoteurs intelligents Dynamixel. Il permet de paramétrer, tester et dépanner facilement des moteurs Dynamixel via une interface intuitive.
</div>

<div class="img-container">
    <img src="{{ site.baseurl }}/assets/img/electronique/wizard.logo.png" alt="Dynamixel Wizard Logo">
</div>

## Pourquoi utiliser Dynamixel Wizard ?

<div>
    <ul>
        <li>Visualisation en temps réel des paramètres du servomoteurs (vitesse, position, température, etc.)</li>
        <li>Modification facile des ID, des limites de position, de la vitesse, du mode de fonctionnement, etc.</li>
        <li>Utile pour un premier paramétrage ou un dépannage rapide avant programmation</li>
    </ul>
</div>

## Installation du Software Dynamixel Wizard 2.0

<div class="card">
    <div class="download-section">
        <div style="margin-bottom: 15px;">
            <p style="margin-bottom: 10px; font-weight: 500;">Télécharger le logiciel :</p>
            <a href="https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/" class="download-btn" style="display: inline-block; background: var(--accent-color); color: white; padding: 10px 8px; border-radius: 6px; text-decoration: none;
            font-weight: bold;box-shadow: 0 2px 5px rgba(0,0,0,0.1); transition: all 0.3s ease;">
               <span style="display: inline-block; margin-right: 8px;">↓</span> Dynamixel Wizard 2.0
            </a>
        </div>
        <div>
            <p style="margin: 0 0 8px 0; font-size: 0.95em; font-weight: 500;">Versions disponibles : Il faudra suivre ensuite les instructions spécifiques à ton OS. </p>
            <ul style="margin: 0; padding-left: 20px; font-size: 0.9em;">
                <li style="margin-bottom: 5px;">Windows</li>
                <li style="margin-bottom: 5px;">macOS </li>
                <li style="margin-bottom: 5px;">Linux</li>
            </ul>
        </div>
    </div>  
    <p><strong>Installation des drivers nécessaires : Driver FT4222H</strong><br>
    <p style="text-align: justify;">Pour bien réussir à connecter nos servomoteurs sur Dynamixel Wizard 2.0, il est impératif de télécharger les librairies D2XX Drivers et LibFT4222</p>
        <a href="https://ftdichip.com/drivers/" style="color: var(--accent-color);">Cliquez ici pour accéder au site de téléchargement</a></p>
        <img src="{{ site.baseurl }}/assets/img/electronique/ft422h_library.png" alt="Driver à installer" style="margin-top: 15px; margin-bottom: 8px; width: 85%;">
    <div class="alert" style="background: #fff3cd; padding: 10px; border-left: 4px solid #ffc107; margin: 15px 0;">
        <strong>Important :</strong> Redémarrer son ordinateur après avoir installé les deux drivers nécessaires
    </div>
</div>

## Matériel Nécessaire
<div class="requirements-simple" style="margin: 20px 0;">
  <ul style="list-style: none; padding: 0; line-height: 1.6; font-size: 0.95em;">
    <li style="padding: 8px 0; border-bottom: 1px solid #eee; display: flex; margin-left:20px;">
      <span style="display: inline-block; width: 120px; font-weight: bold;">Alimentation :</span>
      <span>12V stabilisé pour AX-12</span>
    </li>
    <li style="padding: 8px 0; border-bottom: 1px solid #eee; display: flex; margin-left:20px;">
      <span style="display: inline-block; width: 120px; font-weight: bold;">Servomoteur :</span>
      <span>Dynamixel compatible</span>
    </li>
    <li style="padding: 8px 0; border-bottom: 1px solid #eee; display: flex;  margin-left:20px;">
      <span style="display: inline-block; width: 120px; font-weight: bold;">Câble USB :</span>
      <span>Pour connecter le U2D2</span>
    </li>
    <li style="padding: 8px 0; border-bottom: 1px solid #eee; display: flex; margin-left:20px;">
      <span style="display: inline-block; width: 120px; font-weight: bold;">U2D2 :</span>
      <span>Convertisseur USB/TTL</span>
    </li>
    <li style="padding: 8px 0; display: flex; margin-left:20px;">
      <span style="display: inline-block; width: 120px; font-weight: bold;">PC :</span>
      <span>Pour exécuter le logiciel</span>
    </li>
  </ul>
</div>

## Connexion et Détection

<div style="background: #f8fafc; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
    <p style="text-align: justify; margin: 0;">Cette partie explique les branchements et la détection des servomoteurs. Le constructeur fournit un tutoriel complet que nous vous recommandons vivement de suivre :</p>
    <a href="https://www.youtube.com/watch?v=JRRZW_l1V-U" style="display: inline-block; margin: 10px 0 15px 0;color: var(--accent-color); font-weight: 500;">Tutoriel vidéo officiel - Configuration Dynamixel Wizard 2.0</a>
</div>

<h3 style="color: var(--primary-color); margin-top: 30px; margin-left:30px; margin-bottom:10px">Procédure de connexion</h3>

<div style="counter-reset: step-counter; margin-top: 20px; margin-left:40px;">
    <div style="position: relative; padding-left: 40px; margin-bottom: 20px;">
        <div style="position: absolute; left: 0; width: 28px; height: 28px; background: var(--primary-color); color: white;border-radius: 50%; text-align: center; line-height: 28px; font-size: 0.9em;">1
        </div>
        <div>Branchez les servomoteurs en série (TTL IN → TTL OUT)</div>
    </div>
    <div style="position: relative; padding-left: 40px; margin-bottom: 20px;">
        <div style="position: absolute; left: 0; width: 28px; height: 28px; background: var(--primary-color); color: white;border-radius: 50%; text-align: center; line-height: 28px; font-size: 0.9em;">2
    </div>
        <div>Connectez l'ensemble au convertisseur U2D2 relié à votre PC</div>
    </div>
    <div style="position: relative; padding-left: 40px; margin-bottom: 20px;">
        <div style="position: absolute; left: 0; width: 28px; height: 28px; background: var(--primary-color); color: white;border-radius: 50%; text-align: center; line-height: 28px; font-size: 0.9em;">3
        </div>
            <div>Lancez le logiciel Dynamixel Wizard 2.0</div>
    </div>
    <div style="position: relative; padding-left: 40px; margin-bottom: 20px;">
        <div style="position: absolute; left: 0; width: 28px; height: 28px; background: var(--primary-color); color: white;border-radius: 50%; text-align: center; line-height: 28px; font-size: 0.9em;">4
        </div>
            <div>Dans les menus :
                <ul style="margin-top: 8px; margin-bottom: 0; padding-left: 20px;">
                    <li>Allez dans <strong>Option > Port</strong></li>
                    <li>Sélectionnez le port COM approprié (à vérifier dans le Gestionnaire de périphériques)</li>
                </ul>
            </div>
        </div>
    <div style="position: relative; padding-left: 40px;">
        <div style="position: absolute; left: 0; width: 28px; height: 28px; background: var(--primary-color); color: white;border-radius: 50%; text-align: center; line-height: 28px; font-size: 0.9em;">5
        </div>
            <div>Cliquez sur <strong>"Scan"</strong> pour détecter tous les servomoteurs connectés</div>
        </div>
</div><br>

  <!-- Ajoutez ceci dans le <head> de votre HTML -->
  <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap" rel="stylesheet">

## Comment savoir que les servomoteurs fonctionnent correctement ? 

<hr>

<p style="text-align:justify; line-height: 1.6;"> Pour vérifier le bon fonctionnement des servomoteurs Dynamixel AX-12, une méthodologie rigoureuse s'impose. Ces moteurs intelligents nécessitent des tests à plusieurs niveaux : électronique, mécanique et logiciel. Nous avons alors crée une liste de critère afin de vérifier leur bon fonctionnement. Voici la checklist complète des critères à valider pour certifier leur état opérationnel :
</p>

<p style="text-align:justify; font-size: 13px; background-color:rgba(225, 225, 225, 0.7); "><strong>Conseil technique :</strong> Pour une validation complète, exécutez ces tests à température ambiante (20-25°C) après 5 minutes de mise en service. Les servomoteurs doivent passer tous les critères sans exception pour être considérés comme pleinement opérationnels.</p>

<div style="max-width: 800px; margin: 20px auto; font-family: Arial, sans-serif; overflow-x: auto;">
  <h2 style="text-align: left; color: #1c5083; font-size: 20px; margin-bottom:0px">
    <em>Fiche de test – Servomoteur AX-12 n°XX</em>
  </h2>
  <table style="width: 100%; margin-top: 20px; border-collapse: collapse;">
    <thead>
      <tr style="color: white;">
  <th style=" padding: 12px; text-align: center; background-color: rgb(4, 39, 73); border: 1px solid #ddd; font-family: 'Lato', sans-serif; font-weight: 400;letter-spacing: 0.5px;">
    <strong>Critère</strong>
  </th>
  <th style=" padding: 12px; text-align: center; background-color: rgb(4, 39, 73); border: 1px solid #ddd; font-family: 'Lato', sans-serif; font-weight: 400;letter-spacing: 0.5px;">
    <strong>Observation</strong>
  </th>
  <th style=" padding: 12px; text-align: center; background-color: rgb(4, 39, 73); border: 1px solid #ddd; font-family: 'Lato', sans-serif; font-weight: 400;letter-spacing: 0.5px;">
    <strong>Validé ?</strong>
  </th>
</tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">ID détecté dans Wizard</td>
        <td style="padding: 10px; border: 1px solid #ddd;">Le moteur est-il détecté lors du scan ?</td>
        <td style="padding: 10px; text-align: center; color: #2e7d32; font-weight: bold; border: 1px solid #ddd;">OK</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">ID unique</td>
        <td style="padding: 10px; border: 1px solid #ddd;">Pas de conflit d'ID sur le bus ?</td>
        <td style="padding: 10px; text-align: center; color: #2e7d32; font-weight: bold; border: 1px solid #ddd;">OK</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">Tension correcte</td>
        <td style="padding: 10px; border: 1px solid #ddd;">Tension stable entre 9V et 12V ?</td>
        <td style="padding: 10px; text-align: center; color: #2e7d32; font-weight: bold; border: 1px solid #ddd;">OK</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">Température normale</td>
        <td style="padding: 10px; border: 1px solid #ddd;">Température &lt; 70°C ?</td>
        <td style="padding: 10px; text-align: center; color: #2e7d32; font-weight: bold; border: 1px solid #ddd;">OK</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">Charge moteur à l'arrêt</td>
        <td style="padding: 10px; border: 1px solid #ddd;">Pas de couple ou résistance excessive à l'arrêt ?</td>
        <td style="padding: 10px; text-align: center; color: #2e7d32; font-weight: bold; border: 1px solid #ddd;">OK</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">Contrôle manuel</td>
        <td style="padding: 10px; border: 1px solid #ddd;">Moteur réagit bien aux commandes manuelles ?</td>
        <td style="padding: 10px; text-align: center; color: #2e7d32; font-weight: bold; border: 1px solid #ddd;">OK</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">Position détectée</td>
        <td style="padding: 10px; border: 1px solid #ddd;">Retour de position correct ?</td>
        <td style="padding: 10px; text-align: center; color: #2e7d32; font-weight: bold; border: 1px solid #ddd;">OK</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">Mode correct</td>
        <td style="padding: 10px; border: 1px solid #ddd;">Mode bien configuré (ex : Joint Mode pour test de position) ?</td>
        <td style="padding: 10px; text-align: center; color: #2e7d32; font-weight: bold; border: 1px solid #ddd;">OK</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">Bruits anormaux</td>
        <td style="padding: 10px; border: 1px solid #ddd;">Pas de grésillements, bruits ou vibrations étranges ?</td>
        <td style="padding: 10px; text-align: center; color: #2e7d32; font-weight: bold; border: 1px solid #ddd;">OK</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">Réactivité</td>
        <td style="padding: 10px; border: 1px solid #ddd;">Mouvements fluides et rapides ?</td>
        <td style="padding: 10px; text-align: center; color: #2e7d32; font-weight: bold; border: 1px solid #ddd;">OK</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">Firmware</td>
        <td style="padding: 10px; border: 1px solid #ddd;">Version correcte / à jour ?</td>
        <td style="padding: 10px; text-align: center; color: #2e7d32; font-weight: bold; border: 1px solid #ddd;">OK</td>
      </tr>
    </tbody>
  </table>
</div>



