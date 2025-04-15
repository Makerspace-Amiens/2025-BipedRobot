---
layout: default
nav_exclude: true
title: Jacobien
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
        <h2>Qu'est-ce que le Jacobien ?</h2>
        <hr>
        <p class="lead justified-text">
            Le Jacobien est une matrice de dérivées partielles qui décrit comment les variations des variables d'entrée affectent les variables de sortie d'une fonction vectorielle.
        </p>
        <p class="justified-text">
            En robotique, et particulièrement pour un robot bipède, le Jacobien est crucial pour comprendre la relation entre les vitesses articulaires (variables d'entrée) et les vitesses du centre de masse ou des effecteurs (variables de sortie).
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p style="text-align:justify;">
                Le concept de matrice Jacobienne doit son nom au mathématicien Carl Gustav Jacob Jacobi (1804-1851). Elle est fondamentale en robotique pour la planification et le contrôle des mouvements.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général du Jacobien</h2>
        <p class="justified-text">
            Pour une fonction vectorielle f: ℝⁿ → ℝᵐ, le Jacobien J est une matrice m×n où chaque élément Jᵢⱼ est la dérivée partielle de la i-ème composante de f par rapport à la j-ème variable :
        </p>
        <div class="math-equation">
            <p>$$J = \begin{bmatrix}
            \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\
            \vdots & \ddots & \vdots \\
            \frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
            \end{bmatrix}$$</p>
        </div>
        <p class="justified-text">
            Pour un robot bipède, le Jacobien permet de relier les vitesses angulaires des articulations (hanches, genoux, chevilles) à la vitesse et à l'orientation du corps du robot dans l'espace.
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer le Jacobien à un robot bipède ?</h2>
        <p class="justified-text">
            Dans un robot bipède, le Jacobien est essentiel pour :
            <ul>
                <li>Calculer les vitesses et accélérations du centre de masse</li>
                <li>Maintenir l'équilibre dynamique</li>
                <li>Planifier les trajectoires des pieds</li>
                <li>Implémenter des contrôleurs en force ou en position</li>
                <li>Éviter les singularités (configurations où le robot perd sa mobilité)</li>
            </ul>
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation du Jacobien pour un robot bipède</span>
        </div>
        <pre><code>// Exemple simplifié de calcul du Jacobien pour une jambe de robot bipède
Eigen::MatrixXd computeLegJacobian(const VectorXd& joint_angles) {
    // Paramètres géométriques du robot
    const double l1 = 0.2; // Longueur cuisse
    const double l2 = 0.2; // Longueur tibia
    
    // Extraction des angles articulaires
    double q1 = joint_angles[0]; // Hanche
    double q2 = joint_angles[1]; // Genou
    
    // Initialisation de la matrice Jacobienne 2x2
    Eigen::MatrixXd J(2,2);
    
    // Calcul des éléments du Jacobien
    J(0,0) = -l1*sin(q1) - l2*sin(q1+q2);
    J(0,1) = -l2*sin(q1+q2);
    J(1,0) = l1*cos(q1) + l2*cos(q1+q2);
    J(1,1) = l2*cos(q1+q2);
    
    return J;
}</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir le Jacobien ?</h2>
    <div class="pid-application">
        <div class="application-card">
            <h3>Contrôle d'équilibre</h3>
            <p>Le Jacobien permet de calculer comment ajuster les angles des articulations pour maintenir le centre de masse dans une position stable.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Lorsque le robot commence à pencher vers l'avant, le Jacobien permet de déterminer quelles articulations doivent être ajustées et dans quelle proportion pour rétablir l'équilibre.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Maintenir le centre de masse au-dessus de la zone de support formée par les pieds
            </div>        
        </div>        
    </div>
</div>

<h3>Références</h3> <!--Style APA-->
<ul>
  <li>Siciliano, B., Sciavicco, L., Villani, L., & Oriolo, G. (2009). <cite>Robotics: Modelling, Planning and Control</cite>. Springer Science & Business Media.</li>
  <li>Featherstone, R. (2014). <cite>Rigid Body Dynamics Algorithms</cite>. Springer.</li>
  <li>Murray, R. M., Li, Z., & Sastry, S. S. (1994). <cite>A Mathematical Introduction to Robotic Manipulation</cite>. CRC Press.</li>
  <li>Sardain, P., & Bessonnet, G. (2004). <cite>Forces Acting on a Biped Robot. Center of Pressure—Zero Moment Point</cite>. IEEE Transactions on Systems, Man, and Cybernetics.</li>
</ul>