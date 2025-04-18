---
layout: default
nav_exclude: true
title: Commande Feedforward
---

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
        <h2>Qu'est-ce que la commande Feedforward ?</h2>
        <hr>
        <p class="lead justified-text">
            La commande feedforward (ou "pré-action") est une technique de contrôle qui anticipe les perturbations et les besoins du système en utilisant un modèle de celui-ci.
        </p>
        <p class="justified-text">
            Contrairement au contrôle feedback qui réagit aux erreurs après qu'elles se sont produites, le feedforward agit de manière proactive pour minimiser ces erreurs avant même qu'elles n'apparaissent.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Dans les robots bipèdes, le feedforward est essentiel pour maintenir l'équilibre car il permet d'anticiper les mouvements nécessaires avant que le déséquilibre ne soit détecté par les capteurs.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général du Feedforward</h2>
        <p class="justified-text">
            Le contrôle feedforward utilise une connaissance a priori du système et des perturbations pour calculer la commande nécessaire. Pour un robot bipède, cela signifie :
        </p>
        <div class="math-equation">
            <p>$$u_{ff} = M^{-1}(\theta)(\ddot{\theta}_d + C(\theta, \dot{\theta}) + G(\theta))$$</p>
        </div>
        <div class="diagram-container">
            <img src="{{ site.baseurl }}/assets/img/etude_algo/feedforward/Schema-de-commande-hybride-feedforward-feedback.png" alt="Schéma de commande feedforward" class="img-fluid">
            <p class="text-muted">Schéma de commande hybride feedforward/feedback</p>
        </div>
        <p class="justified-text">
            Où M est la matrice d'inertie, C les forces centrifuges et de Coriolis, G les forces gravitationnelles, et θd la trajectoire désirée.
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Application au robot bipède</h2>
        <p class="justified-text">
            Pour un robot bipède, le feedforward permet :
            <ul>
                <li>D'anticiper les couples nécessaires pour les mouvements planifiés</li>
                <li>De compenser la dynamique intrinsèque du robot (inertie, gravité)</li>
                <li>De réduire la charge de calcul du feedback en fournissant une première approximation de la commande</li>
            </ul>
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation Feedforward pour moteurs</span>
        </div>
        <pre><code>// Modèle simplifié de feedforward pour un moteur
float computeFeedforward(float desiredAngle, float desiredVelocity, float desiredAcceleration) {
    // Paramètres du moteur et du segment
    float inertia = 0.01f;  // Moment d'inertie estimé
    float friction = 0.05f; // Coefficient de friction
    
    // Calcul du couple feedforward
    float torque = inertia * desiredAcceleration 
                 + friction * desiredVelocity
                 + computeGravityCompensation(desiredAngle);
    
    return torque;
}

float computeGravityCompensation(float angle) {
    // Compensation de l'effet de la gravité
    float mass = 0.2f;      // Masse estimée
    float length = 0.1f;    // Longueur du segment
    float g = 9.81f;        // Gravité
    
    return mass * g * length * sin(angle);
}</code></pre>
    </div>
    <h2>Intégration dans l'architecture du robot</h2>
    <div class="pid-application">
        <div class="application-card">
            <h3>Contrôle des moteurs</h3>
            <p>Le feedforward peut être combiné avec un contrôleur PID pour améliorer la performance :</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Pour la marche, calculer d'abord le couple théorique nécessaire (feedforward) puis utiliser le PID pour corriger les erreurs résiduelles.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Réduire l'erreur de suivi de trajectoire et améliorer la stabilité
            </div>        
        </div>
    </div>
</div>

<h3>Références</h3>
<ul>
  <li>Siciliano, B., Sciavicco, L., Villani, L., & Oriolo, G. (2010). <cite>Robotics: Modelling, Planning and Control</cite>. Springer.</li>
  <li>Spong, M. W., Hutchinson, S., & Vidyasagar, M. (2006). <cite>Robot Modeling and Control</cite>. Wiley.</li>
  <li>Pratt, J., & Tedrake, R. (2006). <cite>Velocity-Based Stability Margins for Fast Bipedal Walking</cite>. Fast Motions in Robotics.</li>
  <li>Wieber, P.-B. (2006). <cite>Trajectory Free Linear Model Predictive Control for Stable Walking in the Presence of Strong Perturbations</cite>. Humanoids.</li>
</ul>