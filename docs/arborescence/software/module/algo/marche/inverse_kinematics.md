---
layout: default
nav_exclude: true
title: Cinématique Inverse
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
        <h2>Qu'est-ce que la Cinématique Inverse ?</h2>
        <hr>
        <p class="lead justified-text">
            La cinématique inverse est une méthode utilisée en robotique pour déterminer les angles des articulations nécessaires pour positionner l'effecteur final (comme un pied ou une main) dans une position et orientation spécifiques.
        </p>
        <p class="justified-text">
            Contrairement à la cinématique directe qui calcule la position de l'effecteur à partir des angles des articulations, la cinématique inverse résout le problème inverse : trouver les angles articulaires pour atteindre une position désirée.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                La cinématique inverse est largement utilisée dans les jeux vidéo pour animer les personnages et dans les robots industriels pour le positionnement précis des outils.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général de la Cinématique Inverse</h2>
        <p class="justified-text">
            Pour un robot bipède, la cinématique inverse permet de calculer les angles des hanches, genoux et chevilles nécessaires pour positionner chaque pied selon une trajectoire de marche prédéfinie.
        </p>
        <div class="math-equation">
            <p>$$\theta = f^{-1}(x, y, z)$$</p>
        </div>
        <p class="justified-text">
            Pour les systèmes complexes comme les robots bipèdes, on utilise souvent des méthodes numériques itératives (comme l'algorithme CCD - Cyclic Coordinate Descent) ou des solutions analytiques lorsque possible.
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Application au robot bipède</h2>
        <p class="justified-text">
            Dans un robot bipède, la cinématique inverse est cruciale pour :
            <ul>
                <li>Calculer les positions articulaires pour chaque phase de la marche</li>
                <li>Maintenir l'équilibre lors des transferts de poids</li>
                <li>Adapter la posture en fonction du terrain</li>
                <li>Effectuer des mouvements précis comme monter des escaliers</li>
            </ul>
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation simplifiée de CCD (Cyclic Coordinate Descent)</span>
        </div>
        <pre><code>void solveIK(Limb& limb, Vector3 target) {
    const float tolerance = 0.01f;
    const int maxIterations = 100;
    
    for (int i = 0; i < maxIterations; i++) {
        for (int j = limb.joints.size() - 1; j >= 0; j--) {
            Vector3 toEnd = limb.endEffector - limb.joints[j].position;
            Vector3 toTarget = target - limb.joints[j].position;
            
            Quaternion rotation = Quaternion::FromToRotation(toEnd, toTarget);
            limb.joints[j].rotation = rotation * limb.joints[j].rotation;
            
            if ((limb.endEffector - target).magnitude() < tolerance)
                return;
        }
    }
}</code></pre>
    </div>
    <h2>Intégration dans l'architecture du robot</h2>
    <div class="pid-application">
        <div class="application-card">
            <h3>Contrôle des jambes</h3>
            <p>La cinématique inverse est utilisée pour convertir les trajectoires de marche (définies en coordonnées cartésiennes) en angles articulaires commandables par les servomoteurs.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Pour un pas en avant, on définit d'abord la trajectoire du pied dans l'espace 3D, puis on calcule les angles nécessaires à chaque instant pour chaque articulation de la jambe.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Atteindre la position cible avec une précision de ±2mm tout en respectant les limites articulaires
            </div>        
        </div>
        <div class="application-card">
            <h3>Équilibre dynamique</h3>
            <p>En combinant la cinématique inverse avec des capteurs IMU, on peut ajuster en temps réel la posture pour compenser les perturbations.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Maintenir le centre de masse au-dessus du polygone de sustentation
            </div>
        </div>
    </div>
</div>

<h3>Références</h3>
<ul>
  <li>Buss, S. R. (2004). <cite>Introduction to Inverse Kinematics with Jacobian Transpose, Pseudoinverse and Damped Least Squares methods</cite>. IEEE Journal of Robotics and Automation.</li>
  <li>Craig, J. J. (2005). <cite>Introduction to Robotics: Mechanics and Control</cite>. Pearson Education.</li>
  <li>Kofinas, N., Or, Y., & Chevallereau, C. (2021). <cite>Bipedal Locomotion Control with Inverse Dynamics</cite>. Frontiers in Robotics and AI.</li>
  <li>Siciliano, B., & Khatib, O. (2016). <cite>Springer Handbook of Robotics</cite>. Springer International Publishing.</li>
</ul>