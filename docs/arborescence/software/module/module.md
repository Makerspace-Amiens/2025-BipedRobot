---
layout: default
nav_order: 3
title: Modules Principaux
parent : Logiciel
---

# Listes de Modules 

<p style="text-align: justify;"> Chaque module est conçu pour remplir une fonction clé, allant du contrôle des moteurs à la gestion de l'énergie, en passant par la stabilisation et la communication interne. Ces modules travaillent de manière intégrée pour assurer la performance et la stabilité du robot. Vous trouverez également les algorithmes utilisés pour optimiser chaque fonction. </p>

## Récapitulatif des Modules 

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:12px;
  overflow:hidden;padding:8px 4px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:12px;
  font-weight:normal;overflow:hidden;padding:8px 4px;word-break:normal;}
.tg .tg-dvid{background-color:#efefef;border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-rahz{background-color:#001258;border-color:inherit;color:#ffffff;font-family:Verdana, Geneva, sans-serif !important;
  font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-y698{background-color:#efefef;border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg" style="undefined;table-layout: fixed; width: 600px"><colgroup>
<col style="width: 150px">
<col style="width: 300px">
<col style="width: 150px">
</colgroup>
<thead>
  <tr>
    <th class="tg-rahz">Noms des Modules</th>
    <th class="tg-rahz">Fonctionnalité</th>
    <th class="tg-rahz">Algorithmes </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-dvid">Commande Moteur</td>
    <td class="tg-y698">Contrôle des moteurs du robot pour les mouvements de base (avancer, reculer, tourner)</td>
    <td class="tg-y698"><a href="{{ site.baseurl }}/arborescence/software/module/pid">Proportionnel Intégral Dérivé</a></td>
  </tr>
  <tr>
    <td class="tg-fymr">Stabilisation</td>
    <td class="tg-0pky">Maintien de l’équilibre du robot, gestion des déplacements</td>
    <td class="tg-0pky"><a href="{{ site.baseurl }}/arborescence/software/module/pid">Proportionnel Intégral Dérivé</a>, Régulateur Quadratique Linéaire, Filtrage Kalman</td>
  </tr>
  <tr>
    <td class="tg-dvid">Acquisition de données</td>
    <td class="tg-y698">Collecte des données des capteurs</td>
    <td class="tg-y698">Filtrage des données (Kalman, etc.), Filtre de complémentarité, FFT</td>
  </tr>
  <tr>
    <td class="tg-fymr">Planification de trajectoires</td>
    <td class="tg-0pky">Détermination du chemin à suivre, gestion des obstacles, calcul des trajectoires</td>
    <td class="tg-0pky">A*, Djikstra, RRT</td>
  </tr>
  <tr>
    <td class="tg-dvid">Algorithme de Marche</td>
    <td class="tg-y698">Gestion de la marche, coordination des mouvements des jambes pour une locomotion fluide</td>
    <td class="tg-y698">ZMP, CPG</td>
  </tr>
  <tr>
    <td class="tg-fymr">Communication Interne</td>
    <td class="tg-0pky">Communication entre les différents modules</td>
    <td class="tg-0pky">TCP/IP, ROS 2, MQTT, Protobuf</td>
  </tr>
  <tr>
    <td class="tg-dvid">Gestion d’énergie</td>
    <td class="tg-y698">Optimisation de la consommation d’énergie du robot</td>
    <td class="tg-y698">Algorithmes d’économie d’énergie</td>
  </tr>
  <tr>
    <td class="tg-fymr">Module IA</td>
    <td class="tg-0pky">Prise de décision autonome, apprentissage par renforcement ou supervision</td>
    <td class="tg-0pky">Reinforcement Learning, Réseau Neuronaux Convolutif</td>
  </tr>
  <tr>
    <td class="tg-dvid">Surveillance du Système</td>
    <td class="tg-y698">Surveillance en temps réel de l’état du robot</td>
    <td class="tg-y698">Modèle de diagnostic préditif, Filtrage de Kalman</td>
  </tr>
  <tr>
    <td class="tg-fymr">Gestion d’erreurs</td>
    <td class="tg-0pky">Détection et gestion des erreurs de fonctionnement</td>
    <td class="tg-0pky">Système détection d’erreurs avec classification et réponse adaptative</td>
  </tr>
  <tr>
    <td class="tg-dvid">Réglage Dynamique des Mouvements</td>
    <td class="tg-y698">Ajustement des paramètres de mouvement en fonction des conditions réelles</td>
    <td class="tg-y698">Contrôle adaptatif, Fuzzy Logic</td>
  </tr>
  <tr>
    <td class="tg-fymr">Analyse et Optimisation</td>
    <td class="tg-0pky">Optimisation des performances</td>
    <td class="tg-0pky">Algorithmes Génétiques, Simulated Annealing, Optimisation par essaim</td>
  </tr>
  <tr>
    <td class="tg-dvid">Synchronisation Capteur et Moteur</td>
    <td class="tg-y698">Synchronisation des données des capteurs et des actions des moteurs</td>
    <td class="tg-y698">Filtrage de Kalman, synchronisation temps réel, compensation latence</td>
  </tr>
  <tr>
    <td class="tg-fymr">Base de données & Modélisation</td>
    <td class="tg-0pky">Stockage et analyse des données de performance et des logs du robot</td>
    <td class="tg-0pky">DataLogging, Régression, Prétraitement des données, Clustering</td>
  </tr>
</tbody>
</table>

## Où nos modules s'intègrent-ils dans le code ?

<p style="text-align: justify;">Ci-dessous, un diagramme illustrant l'intervention de chaque module dans le processus de marche d'un robot bipède à son stade optimal. Certains modules, indiqués en jaune, sont optionnels et seront développés si le temps le permet.</p>


  <img src="{{ site.baseurl }}/assets/img/AlgoMarche.png" alt="Algorithme Global de Marche" id="zoom-image">