---
layout: default
nav_order: 2
title: Recherche Modules 
parent: Logiciel
---

# Architecture Modulaire du Robot Bipède

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

<div class="content-wrapper">

<div class="intro-box">
    <p>Notre robot bipède intègre une architecture modulaire où chaque composant remplit une fonction critique. Des moteurs à l'IA embarquée, ces modules interagissent en temps réel via des algorithmes optimisés pour assurer stabilité dynamique et locomotion adaptative. Cette architecture permet une maintenance simplifiée, des mises à jour incrémentales et une spécialisation des développements.</p>
</div>

<h2 class="section-header">Tableau des Modules et Algorithmes Associés</h2>

<p style="text-align:center; font-size:14px; margin-top:12px;">Ce tableau présente de manière structurée les travaux de recherche réalisés pour la conception du système.</p>

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
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/pilote_moteur/trapeze_vitesse" class="algorithm-link">Trapèze Vitesse</a>
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
            <a href="{{site.baseurl}}/arborescence/software/module/algo/ia/rl" class="algorithm-link">RL</a>
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
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/diag_tps_reel/anova" class="algorithm-link">ANOVA</a>
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
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/adapt_dynamique/fuzzylogic" class="algorithm-link">Fuzzy Logic</a>
            <a href="#" class="algorithm-link">RL Adaptatif</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/adapt_dynamique/gradient" class="algorithm-link"> Gradient Stochastique </a>
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
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/bdd/tsdb" class="algorithm-link">TSDB</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/bdd/regression" class="algorithm-link">Régression</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/bdd/k_means" class="algorithm-link">K-means</a>
            <a href="{{ site.baseurl }}/arborescence/software/module/algo/bdd/pca" class="algorithm-link">PCA</a>
        </div>
    </td>
  </tr>
</tbody>
</table>
</div>
