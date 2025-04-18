---
layout: default
nav_order: 3
title: Modules Principaux
parent: Logiciel
---

# Architecture Modulaire du Robot Bipède

<hr>

<style>
:root {
    --primary-color: rgb(28, 80, 131);
    --secondary-color: rgb(20, 60, 100);
    --accent-color: rgba(28, 80, 131, 0.1);
    --text-color: #333;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
}

.module-algorithms {
    margin-top: 0.5rem;
    font-size: 0.9rem;
}

.algorithm-link {
    display: inline-block;
    background-color: var(--accent-color);
    color: var(--primary-color);
    padding: 0.2rem 0.4rem; 
    margin: 0.2rem 0.1rem;
    border-radius: 4px;
    text-decoration: none;
    transition: all 0.2s ease;
    border: 1px solid rgba(28, 80, 131, 0.3);
    font-size: 0.75rem; 
}

.algorithm-link:hover {
    background-color: var(--primary-color);
    color: white;
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.table-container {
    overflow-x: auto;
    margin: 1.5rem 0;
}

.tg {
    border-collapse: collapse;
    border-spacing: 0;
    width: 100%;
    max-width: 100%;
    margin: 0 auto;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.tg td {
    border: 1px solid #ddd;
    font-family: Arial, sans-serif;
    font-size: 14px;
    overflow: hidden;
    padding: 10px 12px;
    word-break: normal;
}

.tg th {
    border: 1px solid #ddd;
    font-family: Verdana, Geneva, sans-serif;
    font-size: 14px;
    font-weight: bold;
    overflow: hidden;
    padding: 12px 15px;
    word-break: normal;
}

.tg .tg-dvid {
    background-color: #f8f9fa;
    font-weight: bold;
    vertical-align: top;
}

.tg .tg-rahz {
    background-color: var(--primary-color);
    color: white;
    text-align: center;
    vertical-align: middle;
}

.tg .tg-y698 {
    background-color: #f8f9fa;
    vertical-align: top;
}

.tg .tg-fymr {
    font-weight: bold;
    vertical-align: top;
}

.tg .tg-0pky {
    vertical-align: top;
}

#zoom-image {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1.5rem auto;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

#zoom-image:hover {
    transform: scale(1.02);
}

.center-text {
    text-align: center;
    margin: 1.5rem 0;
    color: var(--primary-color);
    font-weight: bold;
}

.diagram-container {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    margin: 2rem 0;
    border: 1px solid #ddd;
}

.diagram-title {
    text-align: center;
    color: var(--primary-color);
    margin-bottom: 1rem;
    font-weight: bold;
}

.legend {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    margin-top: 1rem;
}

.legend-item {
    display: flex;
    align-items: center;
    font-size: 0.8rem;
}

.legend-color {
    width: 16px;
    height: 16px;
    margin-right: 8px;
    border-radius: 3px;
}

</style>

<p style="text-align: justify;">Notre robot bipède intègre une architecture modulaire sophistiquée où chaque composant remplit une fonction critique. Des moteurs à l'IA embarquée, ces modules interagissent en temps réel via des algorithmes optimisés pour assurer stabilité dynamique et locomotion adaptative. Cette architecture permet une maintenance simplifiée, des mises à jour incrémentales et une spécialisation des développements.</p>
<h2 class="center-text">Tableau des Modules et Algorithmes Associés</h2>

<div class="table-container">
<table class="tg">
<thead>
  <tr>
    <th class="tg-rahz">Module</th>
    <th class="tg-rahz">Fonctionnalité</th>
    <th class="tg-rahz">Algorithmes</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-dvid">Pilote Moteur</td>
    <td class="tg-y698">Contrôle précis des actionneurs avec boucle de feedback en temps réel. Gère la conversion des commandes de haut niveau en signaux PWM.</td>
    <td class="tg-y698">
        <div class="module-algorithms">
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/pilote_moteur/pid" class="algorithm-link">PID</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/pilote_moteur/feedforward" class="algorithm-link">Feedforward</a>
            <a href="#" class="algorithm-link">Trapèze Vitesse</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-fymr">Stabilisation Dynamique</td>
    <td class="tg-0pky">Maintien de l'équilibre par ajustement en temps réel de la posture. Intègre données IMU et pression plantaire.</td>
    <td class="tg-0pky">
        <div class="module-algorithms">
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/pilote_moteur/pid" class="algorithm-link">PID</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/regulateur" class="algorithm-link">LQR</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/acquisition_donnée/kalman" class="algorithm-link">Kalman</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/mpc" class="algorithm-link">MPC</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-dvid">Acquisition des données</td>
    <td class="tg-y698">Collecte des données des capteurs.</td>
    <td class="tg-y698">
        <div class="module-algorithms">
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/acquisition_donnée/kalman" class="algorithm-link">Kalman</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/acquisition_donnée/FFT" class="algorithm-link">FFT</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/acquisition_donnée/filtre_complementarite" class="algorithm-link">Complémentarité</a>            
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-fymr">Planification de Trajectoire</td>
    <td class="tg-0pky">Génération de trajectoires lisses avec contraintes cinématiques.</td>
    <td class="tg-0pky">
        <div class="module-algorithms">
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/trajectoire/algo_A_etoile" class="algorithm-link">A*</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/trajectoire/rrt" class="algorithm-link">RRT</a>
            <a href="#" class="algorithm-link">Djikstra</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-dvid">Générateur de Marche</td>
    <td class="tg-y698">Synthèse de mouvements biomécaniques avec gestion des phases de double/simple appui et transitions fluides.</td>
    <td class="tg-y698">
        <div class="module-algorithms">
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/marche/zmp" class="algorithm-link">ZMP</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/marche/cpg" class="algorithm-link">CPG</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/marche/inverse_kinematics" class="algorithm-link">Inverse Kinematics</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/marche/jacobien" class="algorithm-link">Jacobien</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-fymr">Communication Interne</td>
    <td class="tg-0pky">Communication entre les différents modules</td>
    <td class="tg-0pky">
        <div class="module-algorithms">
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/communication/TCP.IP" class="algorithm-link">TCP/IP</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/communication/ROS2" class="algorithm-link">ROS 2</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/communication/Protobuf" Class="algorithm-link">Protobuf</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-dvid">Gestion Énergétique</td>
    <td class="tg-y698">Optimisation dynamique de la consommation avec stratégies d'économie adaptatives basées sur l'état des batteries.</td>
    <td class="tg-y698">
        <div class="module-algorithms">
            <a href="#" class="algorithm-link">MPPT</a>
            <a href="#" class="algorithm-link">Scheduling</a>
            <a href="#" class="algorithm-link">ML prédictif</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-fymr">Cerveau Autonome</td>
    <td class="tg-0pky">Décision contextuelle avec apprentissage continu. Intègre perception visuelle et stratégie de locomotion adaptative.</td>
    <td class="tg-0pky">
        <div class="module-algorithms">
            <a href="#" class="algorithm-link">RL (PPO)</a>
            <a href="#" class="algorithm-link">CNN</a>
            <a href="#" class="algorithm-link">GNN</a>
            <a href="#" class="algorithm-link">Bayesian Nets</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-dvid">Diagnostic Temps Réel</td>
    <td class="tg-y698">Surveillance multi-critères avec seuils adaptatifs. Génération d'alertes et modes dégradés.</td>
    <td class="tg-y698">
        <div class="module-algorithms">
            <a href="#" class="algorithm-link">ANOVA</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/acquisition_donnée/kalman" class="algorithm-link">Kalman</a>
            <a href="#" class="algorithm-link">LSTM Anomaly</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-fymr">Gestion des Erreurs</td>
    <td class="tg-0pky">Système hiérarchisé de gestion des pannes avec reconfiguration dynamique et stratégies de recovery.</td>
    <td class="tg-0pky">
        <div class="module-algorithms">
            <a href="#" class="algorithm-link">FMEA</a>
            <a href="#" class="algorithm-link">Arbres de Décision</a>
            <a href="#" class="algorithm-link">Voting</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-dvid">Adaptation Dynamique</td>
    <td class="tg-y698">Ajustement en ligne des paramètres de contrôle selon le terrain, charge et état mécanique.</td>
    <td class="tg-y698">
        <div class="module-algorithms">
            <a href="#" class="algorithm-link">Fuzzy Logic</a>
            <a href="#" class="algorithm-link">RL Adaptatif</a>
            <a href="#" class="algorithm-link">Gradient Stochastique</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-fymr">Optimisation Système</td>
    <td class="tg-0pky">Amélioration continue des performances via analyse des données opérationnelles.</td>
    <td class="tg-0pky">
        <div class="module-algorithms">
            <a href="#" class="algorithm-link">GA</a>
            <a href="#" class="algorithm-link">Bayesian Opt.</a>
            <a href="#" class="algorithm-link">Swarm</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-dvid">Synchronisation Temps Réel</td>
    <td class="tg-y698">Ordonnancement précis des tâches critiques avec gestion des contraintes temporelles strictes.</td>
    <td class="tg-y698">
        <div class="module-algorithms">
            <a href="#" class="algorithm-link">TDMA</a>
            <a href="#" class="algorithm-link">RTOS Scheduler</a>
            <a href="#" class="algorithm-link">Horloge Lamport</a>
        </div>
    </td>
  </tr>
  <tr>
    <td class="tg-fymr">Data Analytics</td>
    <td class="tg-0pky">Stockage structuré avec compression et analyse prédictive des tendances de performance.</td>
    <td class="tg-0pky">
        <div class="module-algorithms">
            <a href="#" class="algorithm-link">TSDB</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/bdd/regression" class="algorithm-link">Régression</a>
            <a href="#" class="algorithm-link">K-means</a>
            <a href="#" class="algorithm-link">PCA</a>
        </div>
    </td>
  </tr>
</tbody>
</table>
</div>
