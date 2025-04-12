---
layout: default
nav_exclude: true
title: Filtre Complémentaire
---
<!-- TEMPLATE POUR LES NOTIONS IMPORTANTES ALGO BASE SUR LE FILTRAGE COMPLEMENTAIRE -->

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

<div class="kalman-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce qu'un filtre complémentaire ?</h2>
        <hr>
        <p class="lead justified-text">
            Le filtre complémentaire est une technique de fusion de capteurs simple mais efficace qui combine les mesures de deux capteurs ou sources de données ayant des caractéristiques spectrales complémentaires.
        </p>
        <p class="justified-text">
            Contrairement au filtre de Kalman plus complexe, le filtre complémentaire utilise une approche basée sur les fréquences pour fusionner les données : un capteur fournit les basses fréquences (comme un gyroscope) et l'autre les hautes fréquences (comme un accéléromètre).
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Le filtre complémentaire est très populaire dans les systèmes embarqués car il nécessite peu de ressources de calcul tout en fournissant des résultats satisfaisants pour de nombreuses applications comme la stabilisation de drones ou la mesure d'orientation.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général du Filtre Complémentaire</h2>
        <p class="justified-text">
            Le filtre complémentaire fonctionne selon le principe suivant : il combine deux sources de données en utilisant un facteur de gain α (entre 0 et 1) qui détermine quelle source est privilégiée pour chaque plage de fréquence.
        </p>
        <div class="math-equation">
            <p>$$\theta = \alpha \cdot (\theta_{prev} + \omega \cdot dt) + (1 - \alpha) \cdot \theta_{mesure}$$</p>
        </div>
       <p class="justified-text">
            Pour l'estimation d'angle, on utilise typiquement le gyroscope (bon en dynamique mais sujet à la dérive) et l'accéléromètre (précis en statique mais bruyant en dynamique). Le filtre complémentaire permet d'obtenir une estimation stable et précise de l'angle en combinant les avantages des deux capteurs.
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer cette notion au projet ?</h2>
        <p class="justified-text">
            Dans un projet de robotique ou drone, le filtre complémentaire peut être utilisé pour estimer l'orientation à partir des données IMU (Inertial Measurement Unit). C'est une solution légère et efficace qui convient particulièrement aux microcontrôleurs avec des ressources limitées.
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation Filtre Complémentaire</span>
            <button onclick="copyCode()">📋 Copier</button>
        </div>
        <pre><code>// Implémentation simple d'un filtre complémentaire en C++
float complementaryFilter(float accelAngle, float gyroRate, float dt, float alpha) {
    static float angle = 0;
    // Partie gyroscope (intégration)
    angle += gyroRate * dt;
    // Fusion avec l'accéléromètre
    angle = alpha * angle + (1 - alpha) * accelAngle;
    return angle;
}</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir le Filtre Complémentaire ?</h2>
    <div class="pid-application">
        <div class="application-card">
            <h3>Estimation d'orientation</h3>
            <p>Le filtre complémentaire peut être utilisé pour estimer les angles de roulis et de tangage à partir des données d'un IMU.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Sur un drone, on peut l'utiliser pour combiner les mesures d'accéléromètre (précises à basse fréquence) et de gyroscope (précises à haute fréquence) pour obtenir une estimation stable de l'orientation.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Obtenir une estimation d'angle précise et stable avec un minimum de ressources de calcul
        </div>        
    </div>
</div>

<h3>Références</h3> <!--Style APA-->
<ul>
  <li>Bohn, J., & Lynch, E. (2014). <cite>Complementary filtering for robotic applications</cite>. Journal of Robotics, 12(3), 45-52.</li>
  <li>Mahony, R., Hamel, T., & Pflimlin, J. M. (2008). <cite>Nonlinear complementary filters on the special orthogonal group</cite>. IEEE Transactions on Automatic Control, 53(5), 1203-1218.</li>
  <li>Euston, M., Coote, P., Mahony, R., Kim, J., & Hamel, T. (2008). <cite>A complementary filter for attitude estimation of a fixed-wing UAV</cite>. IEEE/RSJ International Conference on Intelligent Robots and Systems.</li>
  <li>Valenti, R. G., Dryanovski, I., & Xiao, J. (2015). <cite>Keeping a good attitude: A quaternion-based orientation filter for IMUs and MARGs</cite>. Sensors, 15(8), 19302-19330.</li>
</ul>

<script>
function copyCode() {
    const code = document.querySelector('.code-container code').innerText;
    navigator.clipboard.writeText(code);
    
    // Feedback visuel
    const button = document.querySelector('.code-header button');
    const originalText = button.innerHTML;
    button.innerHTML = '✓ Copié!';

    setTimeout(() => {
        button.innerHTML = originalText;
    }, 2000);
}
</script>