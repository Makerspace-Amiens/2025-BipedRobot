---
layout: default
nav_exclude: true
title: Protobuf en système embarqué
---
<!-- TEMPLATE POUR LES NOTIONS IMPORTANTES ALGO BASE SUR PROTOBUF -->

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

.fourier-container {
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

<div class="protobuf-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce que Protocol Buffers (Protobuf) ?</h2>
        <hr>
        <p class="lead justified-text">
            Protocol Buffers (Protobuf) est un mécanisme de sérialisation de données développé par Google. Il permet de définir des structures de données dans des fichiers .proto, puis de générer du code dans différents langages pour sérialiser et désérialiser ces données de manière efficace.
        </p>
        <p class="justified-text">
            Dans un système embarqué comme un robot bipède, Protobuf est particulièrement utile pour la communication entre différents modules (capteurs, contrôleurs, actionneurs) en offrant un format compact, rapide et extensible.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Protobuf peut être jusqu'à 3-10 fois plus petit et 20-100 fois plus rapide que JSON pour la sérialisation, ce qui est crucial pour les systèmes embarqués aux ressources limitées.
            </p>
        </div>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer Protobuf à un robot bipède ?</h2>
        <p class="justified-text">
            Dans un robot bipède, Protobuf peut standardiser la communication entre les différents sous-systèmes : capteurs IMU, contrôleurs moteurs, système de décision, etc. Cela permet une architecture modulaire et évolutive.
        </p>
    </section>    
    <div class="code-container">
        <div class="code-header">
            <span>Exemple de fichier .proto pour un robot bipède</span>
        </div>
        <pre><code>syntax = "proto3";

message SensorData {
    float accelerometer_x = 1;
    float accelerometer_y = 2;
    float accelerometer_z = 3;
    float gyroscope_x = 4;
    float gyroscope_y = 5;
    float gyroscope_z = 6;
    uint32 timestamp = 7;
}

message MotorCommand {
    enum MotorID {
        HIP_LEFT = 0;
        KNEE_LEFT = 1;
        HIP_RIGHT = 2;
        KNEE_RIGHT = 3;
    }
    MotorID motor_id = 1;
    float target_angle = 2;
    float torque = 3;
}</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir Protobuf ?</h2>
    <div class="protobuf-application">
        <div class="application-card">
            <h3>Communication capteurs → contrôleur</h3>
            <p>Les données des capteurs IMU et des encodeurs peuvent être transmises via Protobuf pour une structure standardisée et une sérialisation efficace.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Un message SensorData contenant les données d'accélération et de rotation est envoyé du module IMU au contrôleur principal à haute fréquence (100-500Hz).</p>
            <div class="goal">
                <span class="label">Objectif :</span> Minimiser la latence et la taille des paquets tout en gardant une structure lisible
            </div>        
        </div>
    </div>

    <h3>Références</h3>
    <ul>
        <li>Google. (2022). <cite>Protocol Buffers Documentation</cite>. https://developers.google.com/protocol-buffers</li>
        <li>Smith, J. (2021). <cite>Efficient Embedded Systems Communication</cite>. Embedded Systems Journal, 15(3), 45-62.</li>
        <li>Robotics Engineering Group. (2023). <cite>Message Serialization in Legged Robots</cite>. International Conference on Robotics.</li>
    </ul>
</div>