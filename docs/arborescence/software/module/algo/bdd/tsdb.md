---
layout: default
nav_exclude: true
title: TSDB pour robot bipède
---

<!-- KaTeX CDN -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body);"></script>

<style>
:root {
    --primary-color: rgb(28, 80, 131);
    --secondary-color: rgb(28, 80, 131);
    --accent-color: rgb(28, 80, 131);
}

.tsdb-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.math-equation {
    font-size: 1.5rem;
    text-align: center;
    margin: 2rem 0;
    padding: 1.5rem;
    background-color: #f8f9fa;
    border-radius: 8px;
    border-left: 4px solid var(--primary-color);
}

.diagram-container {
    background-color: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    margin: 2rem 0;
    text-align: center;
}

.did-you-know {
    background-color: #f8f9fa;
    border-left: 4px solid var(--primary-color);
    border-radius: 8px;
    padding: 1.5rem;
    margin: 2rem 0;
}

.application-card {
    background: #f8f9fa;
    border-left: 4px solid rgb(28, 80, 131);
    padding: 1.2rem;
    border-radius: 0 4px 4px 0;
    margin-bottom: 1rem;
}

.application-card h3 {
    margin-top: 0;
    color: rgb(28, 80, 131);
}

.goal {
    background: #e8f0fe;
    padding: 0.6rem;
    border-radius: 4px;
    margin: 0.8rem 0;
}

.goal .label {
    font-weight: bold;
    color: var(white);
}

.note {
    font-size: 0.9em;
    color: #666;
    margin-top: 0.8rem;
}

.did-you-know h3 {
    color: var(--primary-color);
    margin-top: 0;
}

.justified-text {
    text-align: justify;
}

.code-container {
    background-color: #282c34;
    color: #abb2bf;
    border-radius: 8px;
    padding: 1.5rem;
    font-family: 'Consolas', 'Monaco', monospace;
    margin: 2rem 0;
    position: relative;
    overflow-x: auto;
}

.code-header {
    background-color: #21252b;
    padding: 0.5rem 1rem;
    border-radius: 8px 8px 0 0;
    margin: -1.5rem -1.5rem 1rem -1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #abb2bf;
    font-family: sans-serif;
}

.code-header button {
    background: none;
    border: none;
    color: inherit;
    cursor: pointer;
    font-size: 1rem;
}

.code-header button:hover {
    color: white;
}

pre {
    margin: 0;
    white-space: pre-wrap;
    word-wrap: break-word;
}

code {
    font-family: 'Consolas', 'Monaco', monospace;
}

.img-fluid {
    max-width: 100%;
    height: auto;
}

.text-muted {
    color: #6c757d;
}

.lead {
    font-size: 1.25rem;
    font-weight: 300;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
}
</style>

<div class="tsdb-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce qu'une TSDB (Time Series Database) ?</h2>
        <hr>
        <p class="lead justified-text">
            Une base de données temporelle (TSDB) est spécialement conçue pour stocker et interroger des données indexées dans le temps, ce qui est crucial pour les systèmes robotiques comme les robots bipèdes.
        </p>
        <p class="justified-text">
            Contrairement aux bases de données relationnelles traditionnelles, les TSDB sont optimisées pour gérer des flux continus de données avec des timestamps, comme les mesures des capteurs, les états des actionneurs ou les données de localisation.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Les TSDB comme InfluxDB ou TimescaleDB peuvent ingérer des millions de points de données par seconde avec un encombrement minimal, ce qui les rend idéales pour la robotique en temps réel.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe des TSDB pour la robotique</h2>
        <p class="justified-text">
            Dans un robot bipède, une TSDB permet de :
        </p>
        <ul>
            <li>Stocker l'historique des états du robot (angles articulaires, accélérations, etc.)</li>
            <li>Effectuer des analyses temporelles pour détecter des motifs de mouvement</li>
            <li>Optimiser les requêtes temporelles pour la détection d'anomalies</li>
            <li>Faciliter le débogage en enregistrant tous les états système</li>
        </ul>
        <div class="math-equation">
            <p>$$\text{Performance} = \frac{\text{Requêtes temporelles}}{\text{Temps de réponse}}$$</p>
        </div>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Application au projet de robot bipède</h2>
        <p class="justified-text">
            Dans notre robot bipède, la TSDB servira de système centralisé pour :
        </p>
        <ul>
            <li>L'enregistrement des données des capteurs IMU</li>
            <li>Le suivi des commandes envoyées aux servomoteurs</li>
            <li>L'analyse des performances de l'algorithme de marche</li>
            <li>Le stockage des logs système avec timestamp</li>
        </ul>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Exemple d'intégration TSDB (Python avec InfluxDB)</span>
        </div>
        <pre><code>from influxdb_client import InfluxDBClient

# Configuration de la TSDB
client = InfluxDBClient(url="http://localhost:8086", token="robot-token", org="biped-robot")
write_api = client.write_api()

def store_sensor_data(timestamp, sensor_type, values):
    data = {
        "measurement": sensor_type,
        "tags": {"robot": "biped-v1"},
        "time": timestamp,
        "fields": values
    }
    write_api.write(bucket="robot_data", record=data)

# Exemple d'utilisation
store_sensor_data("2023-01-01T00:00:00Z", "imu", {
    "accel_x": 0.12,
    "accel_y": 0.05,
    "accel_z": 9.81
})</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir la TSDB ?</h2>
    <div class="tsdb-application">
        <div class="application-card">
            <h3>Module de collecte des données</h3>
            <p>La TSDB intervient au niveau de la couche de persistance des données du robot.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Toutes les données des capteurs (IMU, encodeurs, forces) sont timestampées et stockées dans la TSDB avant traitement par l'algorithme de contrôle.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Permettre une analyse rétrospective des mouvements et optimiser les paramètres de marche
            </div>
        </div>
        <div class="application-card">
            <h3>Module de diagnostic</h3>
            <p>La TSDB permet de stocker les états internes du système de contrôle pour le débogage.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Identifier les causes des instabilités en analysant les séries temporelles des états du robot
            </div>
        </div>
        <div class="application-card">
            <h3>Module d'apprentissage</h3>
            <p>Les données historiques servent à entraîner des modèles de prédiction de mouvement.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Améliorer les algorithmes de marche par analyse des données passées
            </div>
        </div>
    </div>
</div>

<h3>Références</h3>
<ul>
  <li>InfluxDB Documentation. (2023). <cite>Time series data collection for robotics</cite>. InfluxData.</li>
  <li>Robotics, S. (2022). <cite>Efficient Data Management in Legged Robots</cite>. Journal of Robotic Systems.</li>
  <li>TimescaleDB. (2023). <cite>Time-series data for real-time systems</cite>. Timescale Inc.</li>
  <li>Bipedal Robotics Group. (2023). <cite>Data-driven control optimization</cite>. MIT Press.</li>
</ul>