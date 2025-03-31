---
layout: default
nav_order: 1
title: Environnement
parent: Logiciel
---

# Environnement de Développement

## Outils et Langage : Python ou C++ ?

<style>
.logos {
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.logos img {
    width: 120px; 
    height: auto;
    background-color: transparent;
}
</style>
<br><br>

<div class="logos">
    <img src="{{ site.baseurl }}/assets/img/logos/python_logo.jpg" alt="Python Logo">
    <img src="{{ site.baseurl }}/assets/img/logos/cpp_logo.png" alt="C++ Logo">
</div>

<br><br>

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-qt50{background-color:#001258;border-color:inherit;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;
  font-size:12px;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-b131{background-color:#efefef;border-color:inherit;font-size:12px;text-align:center;vertical-align:top}
.tg .tg-dkpo{background-color:#001258;border-color:inherit;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;
  font-size:12px;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-gzo9{border-color:inherit;font-size:12px;text-align:center;vertical-align:top}
.tg .tg-irt2{background-color:#efefef;border-color:inherit;font-size:12px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0p48{border-color:inherit;font-size:12px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-1dax{border-color:inherit;font-size:12px;text-align:center;vertical-align:middle}
</style>
<table class="tg" style="undefined;table-layout: fixed; width: 568px"><colgroup>
<col style="width: 164.272727px">
<col style="width: 197.272727px">
<col style="width: 206.272727px">
</colgroup>
<thead>
  <tr>
    <th class="tg-qt50">Critères</th>
    <th class="tg-dkpo">Python</th>
    <th class="tg-qt50">C++</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-irt2">Accessibilité et apprentissage</td>
    <td class="tg-b131"> Très accessible pour les débutants grâce à une syntaxe simple </td>
    <td class="tg-b131">Nécessite une bonne compréhension des concepts avancés</td>
  </tr>
  <tr>
    <td class="tg-0p48">Performance (temps réel)</td>
    <td class="tg-gzo9">Moins performant en termes de vitesse d'exécution, mais suffisant pour des tâches simples</td>
    <td class="tg-1dax"> Excellente performance pour des applications temps réel, comme la robotique </td>
  </tr>
  <tr>
    <td class="tg-irt2">Gestion de la mémoire</td>
    <td class="tg-b131"> Automatique via le garbage collector </td>
    <td class="tg-b131">Contrôle manuel, permettant une gestion précise mais complexe de la mémoire</td>
  </tr>
  <tr>
    <td class="tg-0p48">Bibliothèques et écosystème</td>
    <td class="tg-gzo9"> Large choix de bibliothèques pour le machine learning, l'IA, et la robotique (ex: NumPy, PySerial) </td>
    <td class="tg-gzo9">Moins d'options pour des applications robotiques générales, mais des bibliothèques comme ROS et OpenCV offrent une grande puissance</td>
  </tr>
  <tr>
    <td class="tg-irt2">Prise en charge de l'IA et du Machine Learning</td>
    <td class="tg-b131"> Excellent pour l'IA, avec des bibliothèques comme TensorFlow et PyTorch </td>
    <td class="tg-b131">Utilisé moins fréquemment pour l'IA, mais reste viable avec Dlib, OpenCV et autres</td>
  </tr>
  <tr>
    <td class="tg-0p48">Temps de développement</td>
    <td class="tg-gzo9"> Plus rapide grâce à une syntaxe concise et une large base de bibliothèques </td>
    <td class="tg-gzo9">Plus long en raison de la gestion manuelle des ressources et de la complexité du langage</td>
  </tr>
  <tr>
    <td class="tg-irt2">Compatibilité et intégration robotique</td>
    <td class="tg-b131">Bonne compatibilité, mais moins adapté aux tâches critiques et en temps réel</td>
    <td class="tg-b131"> Idéal pour des applications robotiques critiques, avec un excellent contrôle sur le matériel </td>
  </tr>
  <tr>
    <td class="tg-0p48">Débogage et tests</td>
    <td class="tg-gzo9"> Outils de débogage très accessibles avec des IDE comme VS Code et PyCharm </td>
    <td class="tg-gzo9">Débogage plus complexe mais puissant avec des outils comme GDB</td>
  </tr>
  <tr>
    <td class="tg-irt2">Maintenance et évolution</td>
    <td class="tg-b131"> Facile à maintenir grâce à une grande simplicité syntaxique </td>
    <td class="tg-b131">Plus difficile à maintenir en raison de la gestion manuelle des ressources et des complexités</td>
  </tr>
</tbody></table>

<div style="text-align: justify;">
    <div>
        <h3>Pourquoi nous avons choisi C++ pour notre projet robotique ?</h3>
        <p>C++ est largement considéré comme le langage de choix pour les applications robotiques en raison de ses performances et de sa flexibilité. Voici pourquoi nous avons opté pour C++ :</p>
        <ul>
            <li><strong>Performance optimale</strong> : C++ permet un contrôle direct du matériel, ce qui est essentiel pour des systèmes à haute performance et des applications temps réel.</li><br>
            <li><strong>Contrôle sur la mémoire</strong> : C++ offre une gestion fine de la mémoire, essentielle pour les applications robotiques où la réactivité et la performance sont cruciales.</li><br>
            <li><strong>Large écosystème en robotique</strong> : C++ est utilisé dans de nombreuses bibliothèques comme ROS (Robot Operating System), facilitant l'intégration de composants robotiques complexes.</li><br>
        </ul>
    </div>
</div>

## Choix de l'IDE : **Pourquoi Visual Studio Code ?**

<br>
<div class="logos">
    <img src="{{ site.baseurl }}/assets/img/logos/vscode.png" alt="VS Code Logo">
</div><br>

<div style="text-align: justify;">
    <div>      
        <ul>
            <li><strong>Légèreté : </strong> VS Code est un éditeur léger mais puissant, parfait pour le développement Python. Il permet de travailler efficacement sans être aussi lourd qu'un IDE complet comme PyCharm.</li><br>
            <li><strong>Extensibilité : </strong> Grâce à un large écosystème de plugins, VS Code offre une personnalisation facile pour le développement Python, y compris l'intégration de bibliothèques tierces, des outils de gestion de version, des extensions pour la gestion des serveurs, etc.</li><br>
            <li><strong>Support pour Python :</strong> VS Code dispose d'une extension Python officielle qui facilite la gestion de l'environnement Python, l'exécution de tests, le débogage, et l'autocomplétion.</li>
        </ul>
    </div>
</div>

## Installation & Configuration

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-eqth{background-color:#001258;border-color:#000000;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;
  font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg" style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
  <tr>
    <th class="tg-eqth">Outils</th>
    <th class="tg-eqth">Étapes d'Installation</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">VS Code</td>
    <td class="tg-0pky">
      1. Télécharger depuis <a href="https://code.visualstudio.com/download" target="_blank">visualstudio.com</a><br>
      2. Installe-le selon les instructions pour ton système d’exploitation.<br>
    </td>
  </tr>
  <tr>
<td class="tg-fymr">C++</td>
<td class="tg-0pky">
  1. Télécharger et installer un compilateur comme MinGW-w64 ou MSVC.<br>
  2. Configurer les variables d'environnement si nécessaire.<br>
  3. Vérifier l'installation avec : <code>g++ --version</code> ou <code>cl</code> dans le terminal.<br>
</td>
  </tr>
  <tr>
    <td class="tg-fymr">MySQL</td>
    <td class="tg-0pky">
      1. Télécharger MySQL depuis <a href="https://www.mysql.com/" target="_blank">mysql.com</a><br>
      2. Suivre l'installation standard et configurer un utilisateur root.<br>
      3. Vérifier l'installation avec : <code>mysql --version</code> dans le terminal.
    </td>
  </tr>
  <tr>
    <td class="tg-fymr">MongoDB</td>
    <td class="tg-0pky">
      1. Télécharger MongoDB depuis <a href="https://www.mongodb.com/" target="_blank">mongodb.com</a><br>
      2. Installer MongoDB Community Server et lancer le serveur avec : <code>mongod</code><br>
      3. Vérifier l'installation avec : <code>mongod --version</code> dans le terminal.
    </td>
  </tr>
  <tr>
    <td class="tg-fymr">PlatformIO</td>
    <td class="tg-0pky">
      1. Ouvrir VS Code et installer l'extension PlatformIO IDE depuis la section Extensions.<br>
      2. Après installation, redémarrer VS Code pour activer l'extension.<br>
    </td>
  </tr>
</tbody>
</table>

<h2>Installation des bibliothèques</h2>

<p style="text-align: justify;">Une fois l’environnement prêt, nous allons installer les bibliothèques nécessaires au bon fonctionnement du projet en utilisant la commande suivante : <code>pio lib install [NOM_DE_LA_BIBLIOTHÈQUE]</code></p>

<h3>Bibliothèques à installer</h3>
<ul>
  <li><strong>Dynamixel    </strong><code>pio lib install https://github.com/ROBOTIS-GIT/DynamixelSDK.git</code><br> 
  Permet de contrôler les servomoteurs Dynamixel (AX-12+, etc.). Elle facilite la communication avec les moteurs via un bus série et offre des fonctions pour lire/écrire leurs paramètres (vitesse, position, couple…). <br><br>
  </li>
  <li><strong>feilipu/FreeRTOS    </strong><code>pio lib install feilipu/FreeRTOS@^11.1.0-3	</code><br> 
  Implémente un système d’exploitation temps réel (RTOS) pour gérer les tâches du robot de manière efficace. Cela permet, par exemple, d’exécuter plusieurs processus en parallèle comme la gestion des moteurs et la collecte des données capteurs.<br><br></li>

  <li><strong>adafruit/Adafruit Unified Sensor    </strong><code>pio lib install adafruit/Adafruit Unified Sensor@^1.1.15</code><br> 
  Fournit une interface standardisée pour l'utilisation de divers capteurs Adafruit. Utile si ton robot utilise des capteurs de position, d’accélération ou de température pour améliorer son contrôle et sa stabilité. <br><br>
  </li>
</ul>
