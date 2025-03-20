---
layout: default
nav_order: 2
title: Environnement
parent : Logiciel
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
    width: 130px; 
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
  font-size:11px;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-b131{background-color:#efefef;border-color:inherit;font-size:11px;text-align:center;vertical-align:top}
.tg .tg-dkpo{background-color:#001258;border-color:inherit;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;
  font-size:11px;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-gzo9{border-color:inherit;font-size:11px;text-align:center;vertical-align:top}
.tg .tg-irt2{background-color:#efefef;border-color:inherit;font-size:11px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0p48{border-color:inherit;font-size:11px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-1dax{border-color:inherit;font-size:11px;text-align:center;vertical-align:middle}
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
    <td class="tg-irt2">Facilité d'Apprentissage</td>
    <td class="tg-b131"><span style="background-color:#C9FFF5">Très accessible</span></td>
    <td class="tg-b131">Plus complexe, nécessite une meilleure compréhension des concepts bas-niveau</td>
  </tr>
  <tr>
    <td class="tg-0p48">Vitesse d'exécution</td>
    <td class="tg-gzo9">Moins rapide, interprété</td>
    <td class="tg-1dax"><span style="background-color:#C9FFF5">Plus rapide, compilé, donc meilleure performance en termes de vitesse d'exécution</span></td>
  </tr>
  <tr>
    <td class="tg-irt2">Gestion de la mémoire</td>
    <td class="tg-b131"><span style="background-color:#C9FFF5">Automatique via le garbage collector</span></td>
    <td class="tg-b131">Moins de bibliothèque prête à l'emploi pour la robotique </td>
  </tr>
  <tr>
    <td class="tg-0p48">Bibliothèque</td>
    <td class="tg-gzo9"><span style="background-color:#C9FFF5">Large écosystème de bibliothèques (pySerial, NumPy, etc.)</span></td>
    <td class="tg-gzo9">Moins de bibliothèques prêtes à l'emploi pour la robotique, mais plus puissant pour des applications bas-niveau</td>
  </tr>
  <tr>
    <td class="tg-irt2">Utilisation IA</td>
    <td class="tg-b131"><span style="background-color:#C9FFF5">Idéal pour l'intelligence artificielle et le machine learning (TensorFlow, PyTorch)</span></td>
    <td class="tg-b131">Moins utilisé pour l'IA, mais possible via des bibliothèques comme Dlib ou OpenCV</td>
  </tr>
  <tr>
    <td class="tg-0p48">Temps de développement</td>
    <td class="tg-gzo9"><span style="background-color:#C9FFF5">Plus rapide grâce à une syntaxe concise et à une grande bibliothèque de modules</span></td>
    <td class="tg-gzo9">Plus long à cause de la complexité de la gestion des ressources, mais plus de contrôle</td>
  </tr>
  <tr>
    <td class="tg-irt2">Robotique</td>
    <td class="tg-b131">Moins performant pour des tâches critiques en temps réel </td>
    <td class="tg-b131"><span style="background-color:#C9FFF5">Excellente performance en temps réel</span></td>
  </tr>
  <tr>
    <td class="tg-0p48">Compatibilité avec le matériel</td>
    <td class="tg-gzo9">Excellente compatibilité</td>
    <td class="tg-gzo9"><span style="background-color:#C9FFF5">Très bonne compatibilité</span></td>
  </tr>
  <tr>
    <td class="tg-irt2">Débogage et tests</td>
    <td class="tg-b131"><span style="background-color:#C9FFF5">Outils de débogage faciles d'accès avec des IDE comme VS Code, PyCharm</span></td>
    <td class="tg-b131">Outils de débogage puissants mais plus complexes à configurer (ex. GDB)</td>
  </tr>
  <tr>
    <td class="tg-0p48">Facilité d’intégration</td>
    <td class="tg-gzo9">Facile à intégrer avec d'autres systèmes ou outils logiciels</td>
    <td class="tg-gzo9"><span style="background-color:#C9FFF5">Meilleure Intégration avec le hardware bas-niveau et plus de flexibilité</span></td>
  </tr>
  <tr>
    <td class="tg-irt2">Maintenance</td>
    <td class="tg-b131"><span style="background-color:#C9FFF5">Facile à maintenir </span></td>
    <td class="tg-b131">Difficile à maintenir à cause de la complexité et de la gestion des ressources</td>
  </tr>
</tbody></table>


<div style="text-align: justify;">
    <div>
        <h3>Notre choix final se porte sur Python. <strong>Pourquoi ?</strong></h3>
        <p>Python est largement reconnu comme l'un des meilleurs langages de programmation pour les débutants souhaitant apprendre la robotique. Voici les raisons qui justifient ce choix :</p>
        <ul>
            <li><strong>Courbe d'apprentissage douce</strong> : Python est un langage facile à comprendre et à maîtriser, même pour les novices. Sa syntaxe claire et concise permet de se concentrer davantage sur la logique du programme que sur la complexité du code.</li><br>
            <li><strong>Bibliothèques puissantes</strong> : Python dispose de nombreuses bibliothèques adaptées à la robotique, comme PySerial, RPi.GPIO, TensorFlow et OpenCV, qui facilitent l'intégration de capteurs, la gestion des moteurs, ainsi que l'implémentation de l'intelligence artificielle et de la vision par ordinateur.</li>
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
            <li><strong>Légèreté : </strong> : VS Code est un éditeur léger mais puissant, parfait pour le développement Python. Il permet de travailler efficacement sans être aussi lourd qu'un IDE complet comme PyCharm.</li><br>
            <li><strong>Extensibilité : </strong> : Grâce à un large écosystème de plugins, VS Code offre une personnalisation facile pour le développement Python, y compris l'intégration de bibliothèques tierces, des outils de gestion de version, des extensions pour la gestion des serveurs, etc.</li><br>
            <li><strong>Support pour Python :</strong> : VS Code dispose d'une extension Python officielle qui facilite la gestion de l'environnement Python, l'exécution de tests, le débogage, et l'autocomplétion.</li>
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
<table class="tg" style="undefined;table-layout: fixed; width: 601px"><colgroup>
<col style="width: 139.2px">
<col style="width: 462.2px">
</colgroup>
<thead>
  <tr>
    <th class="tg-eqth">Outils</th>
    <th class="tg-eqth">Etapes d'Installation</th>
  </tr></thead>
<tbody>
 <tr>
    <td class="tg-fymr">VS Code</td>
    <td class="tg-0pky">
     1. Télécharger depuis <a href="https://code.visualstudio.com/download" target="_blank">visualstudio.com</a><br>
     2. Installe-le selon les instructions pour ton système d’exploitation<br>
     3. Ouvre VS Code et installe l'extension Python 
        <br>- Va dans la barre latérale à gauche et clique sur l'icône des Extensions
        <br>- Installe Python <i>(comme ci-dessous)</i>
    </td>
  </tr>
  <tr>
    <td class="tg-fymr">Python</td>
    <td class="tg-0pky">
     1. Télécharger la dernière version de Python depuis <a href="https://www.python.org" target="_blank">python.org</a><br>
     2. Lancer l'installateur et cocher Add Python to PATH<br>
     3. Vérifier l'installation avec : <code>python --version</code>
</td>
  </tr>
  <tr>
    <td class="tg-fymr">MySQL</td>
    <td class="tg-0pky">
    1. Télécharger et installer MySQL depuis MySQL depuis <a href="https://www.mysql.com/" target="_blank"> mysql.com</a><br>
    2. Suivre l'installation standard et configurer un utilisateur root<br>
    3. Vérifier l'installation : <code>mysql --version</code></td>
  </tr>
  <tr>
    <td class="tg-fymr">MangoDB</td>
    <td class="tg-0pky">
    1. Télécharger MongoDB depuis <a href="https://www.mongodb.com/" target="_blank"> mongodb.com</a><br>
    2. Installer MongoDB Community Server et lancer mongod<br>
    3. Vérifier l'installation avec <code>mongod --version</code></td>
  </tr>
  <tr>
    <td class="tg-fymr">Dynamixel SDK</td>
    <td class="tg-0pky">
        1. Télécharger Dynamixel SDK depuis <a href="https://github.com/ROBOTIS-GIT/DynamixelSDK">GitHub - DynamixelSDK</a><br>
        2. Installer Python et Pip si ce n'est pas déjà fait (<code>python --version</code>, <code>pip --version</code>)<br>
        3. Installer Dynamixel SDK via pip : <code>pip install dynamixel-sdk</code>
    </td>
    </tr>
    <tr>
    <td class="tg-fymr">Autre bibliothèqes.....</td>
    <td class="tg-0pky">
    </td>
  </tr>
</tbody>
</table>

## Installation des Dépendances 

<style>
    .code-block {
        font-family: monospace;
        font-size: 16px;
        display: block;
        white-space: pre-wrap;
        background-color:rgb(218, 212, 212);
        padding: 10px;
        border-radius: 5px;
    }
</style>

Pour installer les dépendances propres au projet, nous allons créer un fichier <code>requirements.txt</code>.

À l'intérieur, nous allons définir les dépendances nécessaires :

<pre class="code-block">
numpy
scipy
matplotlib
pyserial
</pre>

Ensuite, dans le terminal de commande, exécutez :

<pre class="code-block">pip install -r requirements.txt</pre>

## Comment Exécuter le Code ? 

<i>(en cours de développement)</i>
