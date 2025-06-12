---
layout: default
nav_order: 3
title: Architecture Logicielle
parent: Logiciel
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

.white-square-shadow {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.34);
    margin: 50px auto;
    max-width: 80%;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
}

h2, h3 {
    color: var(--primary-color);
    margin-top: 1.5rem;
}

/* Styles améliorés pour les icônes */
.icons-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
    margin: 30px auto;
    max-width: 90%;
}

.icon-item {
    background-color: var(--primary-color);
    color: white;
    width: 150px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    text-align: center;
    cursor: pointer;
}

.icon-item:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    background-color: rgb(30, 33, 106);
}

.icon-item a {
    font-size: 18px;
    text-decoration: none;
    color: white;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.icon-item a:hover {
    text-decoration: underline;
}

/* Styles modaux améliorés */
.modal {
    opacity: 0;
    visibility: hidden;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(5, 25, 79, 0.53);
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: opacity 0.3s ease, visibility 0.3s ease;
  }

.modal.show {
    opacity: 1;
    visibility: visible;
}

.modal-content {
    background-color: rgba(250, 245, 245, 0.92);
    padding: 30px;
    border-radius: 8px;
    max-width: 800px;
    width: 90%;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.8);
    transition: transform 0.3s ease;
}

.modal.show .modal-content {
    transform: translate(-50%, -50%) scale(1);
}

.close {
    font-size: 28px;
    font-weight: bold;
    position: absolute;
    top: 10px;
    right: 20px;
    color: #aaa;
    cursor: pointer;
}

.close:hover, .close:focus {
    color: black;
}
</style>

# Architecture Logicielle

<hr>

<div style="font-size: 1.25rem; font-weight: 300; text-align: justify;">
    Cette section présente l'architecture logicielle mise en place pour répondre aux exigences et aux contraintes du projet.
</div>

## Logigramme de fonctionnement

<div class="icons-container">
    <div class="icon-item">
        <a href="javascript:void(0);" onclick="openModal('modal-initialisation')">Initialisation</a>
    </div>
    <div class="icon-item">
        <a href="javascript:void(0);" onclick="openModal('modal-lecture-data')">Lecture des données</a>
    </div>    
    <div class="icon-item">
        <a href="javascript:void(0);" onclick="openModal('modal-equilibre')">Gestion de l'équilibre</a>
    </div>
    <div class="icon-item">
        <a href="javascript:void(0);" onclick="openModal('modal-marche')">Cycle de Marche</a>
    </div>     
</div>

<div class="white-square-shadow">
    <div class="diagram">
        <img src="{{site.baseurl}}/assets/ArchitectureLogicielle.drawio.png" alt="Logigramme de l'architecture logicielle">
    </div>
</div>

<!-- Modals -->
<div id="modal-initialisation" class="modal">
  <div class="modal-content">
    <span class="close" onclick="closeModal('modal-initialisation')">&times;</span>
    <h2>INITIALISATION</h2>
    <p>
      L'initialisation prépare les servomoteurs et la connexion série pour garantir le bon fonctionnement du robot.
    </p>
    <hr>
    <h3>Étapes :</h3>
    <ul>
      <li><strong>Connexion série</strong></li>
      <li>
        <strong>Configuration des servomoteurs</strong>
        <p>Pour chaque moteur dans <code>DXL_IDS</code> :</p>
        <ul>
          <li>Activation du couple : <code>TORQUE_ENABLE = 1</code></li>
          <li>Vitesse par défaut : <code>DEFAULT_MOVING_SPEED = 300</code></li>
          <li>LED allumée : <code>LED_ON = 1</code></li>
          <li>Lecture de la tension pour vérifier l'alimentation</li>
        </ul>
        <p>
          En cas d’erreur (communication, surcharge, etc.), le processus s’arrête et un message d’erreur s’affiche.
        </p>
      </li>
      <li>
        <strong>Position initiale</strong>
        <p>
          Les moteurs amènent le robot à une position de repos définie par <code>INITIAL_POSITIONS</code>, en 1,5 seconde.
        </p>
      </li>
    </ul>
    </div>
</div>

<div id="modal-lecture-data" class="modal">
  <div class="modal-content">
    <span class="close" onclick="closeModal('modal-lecture-data')">&times;</span>
    <h2>LECTURE DES DONNÉES</h2>
    <p>
      La lecture des données des servomoteurs permet de surveiller l’état du robot, d’analyser son comportement et d’assurer un diagnostic en temps réel.
    </p>
    <hr>
    <h3>Données surveillées :</h3>
    <ul>
      <li>
        <strong>Position actuelle</strong>
        <p>
          Lecture via <code>ADDR_PRESENT_POSITION</code> avec <code>packetHandler.read2ByteTxRx</code> :
        </p>
        <ul>
          <li>Vérifier que les positions cibles sont atteintes</li>
          <li>Asservir les mouvements avec retour</li>
          <li>Détecter les blocages ou erreurs de déplacement</li>
        </ul>
      </li>
      <li>
        <strong>Tension d'alimentation</strong>
        <p>
          Lecture via <code>ADDR_PRESENT_VOLTAGE</code>, transformée en volts (division par 10) :
        </p>
        <ul>
          <li>Surveiller l’état de la batterie</li>
          <li>Détecter une alimentation insuffisante (&lt; 9V)</li>
          <li>Prévenir les dommages aux moteurs</li>
        </ul>
      </li>
      <li>
        <strong>Vitesse actuelle</strong>
        <p>
          Accessible via <code>ADDR_PRESENT_SPEED</code> :
        </p>
        <ul>
          <li>Analyser les performances des moteurs</li>
          <li>Identifier les blocages mécaniques (vitesse nulle)</li>
        </ul>
      </li>
    </ul>
  </div>
</div>

<div id="modal-equilibre" class="modal">
    <div class="modal-content">
        <span class="close" onclick="closeModal('modal-equilibre')">&times;</span>
        <h2>Gestion de l'équilibre</h2>
        <hr>
        <p style="text-align: justify">
            La gestion de l'équilibre est cruciale pour la stabilité d'un robot bipède, idéalement via des capteurs IMU et des algorithmes de Point de Moment Nul (ZMP) pour des ajustements en temps réel. Cependant, des défis d'intégration avec un microcontrôleur IMU ont limité cette capacité dans notre projet, nous amenant à nous reposer sur des mouvements pré-calculés pour la stabilité.
        </p>
    </div>
</div>

<div id="modal-marche" class="modal">
  <div class="modal-content">
    <span class="close" onclick="closeModal('modal-marche')">&times;</span>
    <h2>CYCLE DE MARCHE</h2>
    <p>
      Le cycle de marche correspond à une séquence de mouvements prédéfinis permettant au robot bipède d’avancer. Il ne s’agit pas d’une marche adaptative, mais d’un enchaînement de positions fixes simulant les étapes d’un pas.
    </p>
    <hr>
    <h3>Fonctionnement :</h3>
    <ul>
      <li>
        <strong>Séquence de pas :</strong> le script <code>perform_walk_steps()</code> exécute plusieurs phases :
        <ul>
          <li><em>Levée de jambe :</em> une jambe est soulevée et avancée.</li>
          <li><em>Pose et transfert de poids :</em> le robot transfère son poids sur cette jambe.</li>
        </ul>
      </li>
      <li>
        <strong>Durées contrôlées :</strong> chaque phase utilise des durées définies (<code>DUR_STEP_PHASE</code>, <code>DUR_PLANT</code>) pour ajuster vitesse et fluidité.
      </li>
      <li>
        <strong>Synchronisation :</strong> les commandes sont envoyées en parallèle aux servomoteurs avec <code>GroupSyncWrite</code> pour des mouvements coordonnés.
      </li>
      <li>
        <strong>Retour au repos :</strong> après les pas, le robot revient à sa position initiale.
      </li>
      <li>
        <strong>Arrêt d'urgence :</strong> le programme interrompt immédiatement la marche si la touche ESPACE est pressée (<code>emergency_stop_triggered</code>).
      </li>
    </ul>

    <h3>Limites actuelles :</h3>
    <p>
      Cette marche repose uniquement sur des positions fixes. Elle n’utilise pas de capteurs pour réagir en temps réel aux déséquilibres. Une marche vraiment autonome nécessiterait un système de stabilisation avec IMU et algorithmes avancés.
    </p>
  </div>
</div>

<div style="background-color: #f5f7fa; padding: 1em 1.2em; border-radius: 6px; margin-top: 1.5em; border-left: 4px solid #4a6ea9;">
  <div style="font-size: 20px; color: #333; margin-bottom: 0.8em;">
    <strong> Programmation Robot Bipède</strong> — 06/06/2025
  </div>
  <div style="font-size: 14px; color: #444;">
    <ul style="list-style-type: disc; padding-left: 1.2em; margin-bottom: 1em;">
      <li><strong>dynamixel_tests</strong>
        <ul style="list-style-type: circle; padding-left: 1.2em; margin-top: 0.5em;">
          <li><code style="font-size: 15px;">dynamixel_position_reader</code> : lit et affiche les positions actuelles des servomoteurs Dynamixel.</li>
          <li><code style="font-size: 15px;">voltage_monitor</code> : surveille et rapporte la tension d'alimentation de chaque servomoteur.</li>
        </ul>
      </li>
      <li><strong>robot_motion_routines</strong>
        <ul style="list-style-type: circle; padding-left: 1.2em; margin-top: 0.5em;">
          <li><code style="font-size: 15px;">robot_dance_controller</code> : contient les séquences de mouvements pour faire danser le robot.</li>
          <li><code style="font-size: 15px;">robot_left_leg_init</code> : initialise les servomoteurs de la jambe gauche du robot.</li>
          <li><code style="font-size: 15px;">robot_right_leg_init</code> : initialise les servomoteurs de la jambe droite du robot.</li>
          <li><code style="font-size: 15px;">robot_walk_controller_with_emergency_stop</code> : gère la marche avec fonction d'arrêt d'urgence.</li>
            <li><code style="font-size: 15px;">simple_dynamixel_controller</code> : interface basique pour contrôler les servomoteurs.</li>
        </ul>
      </li>
    </ul>
  </div>
  <div style="font-size: 14px; margin-top: 0.5em;">
      <a href="{{site.baseurl}}/assets/dynamixel_test.zip"
       download="robot_dynamixel_programmation.zip"
       style="color: #2a6496; text-decoration: none; font-weight: 500;">
      Télécharger le fichier ZIP
    </a>
  </div>
</div>


<script>
function openModal(modalId) {
  let modal = document.getElementById(modalId);
  modal.classList.add('show');
}

function closeModal(modalId) {
  let modal = document.getElementById(modalId);
  modal.classList.remove('show');
}

</script>