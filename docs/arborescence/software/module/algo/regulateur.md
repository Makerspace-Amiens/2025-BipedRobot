---
layout: default
nav_exclude: true
title: Régulateur Quadratique Linéaire (LQR)
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
        <h2>Qu'est-ce qu'un Régulateur Quadratique Linéaire (LQR) ?</h2>
        <hr>
        <p class="lead justified-text">
            Le Régulateur Quadratique Linéaire (LQR) est une méthode de contrôle optimal pour les systèmes dynamiques linéaires qui minimise une fonction de coût quadratique.
        </p>
        <p class="justified-text">
            Le LQR est largement utilisé en robotique et automatique pour stabiliser des systèmes tout en minimisant l'énergie consommée. Il combine les états du système avec les entrées de commande pour trouver la loi de contrôle optimale.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Le LQR a été développé dans les années 1960 par Rudolf Kalman (le même que pour le filtre de Kalman) et est devenu un outil fondamental en contrôle optimal. Il est particulièrement efficace pour les systèmes où on doit trouver un compromis entre performance et consommation d'énergie.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général du LQR</h2>
        <p class="justified-text">
            Le LQR résout un problème d'optimisation où l'on cherche à minimiser une fonction de coût quadratique qui dépend à la fois de l'état du système et de la commande appliquée.
        </p>
        <div class="math-equation">
            <p>$$ J = \int_{0}^{\infty} (x^T Q x + u^T R u) dt $$</p>
        </div>
        <p class="justified-text">
            Où:
            <ul>
                <li><strong>x</strong> est le vecteur d'état du système</li>
                <li><strong>u</strong> est le vecteur de commande</li>
                <li><strong>Q</strong> est une matrice définie positive pondérant l'importance des états</li>
                <li><strong>R</strong> est une matrice définie positive pondérant l'importance des commandes</li>
            </ul>
            La solution donne une loi de commande optimale de la forme <strong>u = -Kx</strong>, où K est la matrice de gain optimale.
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer le LQR pour stabiliser le robot ?</h2>
        <p class="justified-text">
            Pour stabiliser un robot, le LQR peut être utilisé pour calculer les gains optimaux du contrôleur qui maintiennent le robot dans la position désirée tout en minimisant l'énergie dépensée.
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation basique d'un LQR en Python</span>
            <button onclick="copyCode()">📋 Copier</button>
        </div>
        <pre><code>import numpy as np
from scipy.linalg import solve_continuous_are

def lqr(A, B, Q, R):
    """Résout le problème LQR pour un système continu
    Args:
        A, B: Matrices d'état du système dx/dt = A x + B u
        Q: Matrice de coût pour l'état
        R: Matrice de coût pour la commande
    Returns:
        K: Matrice de gain optimale
    """
    # Résolution de l'équation de Riccati
    P = solve_continuous_are(A, B, Q, R)
    
    # Calcul de la matrice de gain
    K = np.linalg.inv(R) @ B.T @ P
    
    return K

# Exemple pour un pendule inversé
A = np.array([[0, 1], [1, 0]])
B = np.array([[0], [1]])
Q = np.eye(2)  # Poids sur l'état
R = np.eye(1)  # Poids sur la commande

K = lqr(A, B, Q, R)
print("Matrice de gain LQR:", K)
</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir le LQR ?</h2>
    <div class="pid-application">
        <div class="application-card">
            <h3>Module de stabilisation du robot bipède</h3>
            <p>Le contrôleur LQR (Linear Quadratic Regulator) peut être intégré au système de contrôle du robot bipède afin d'assurer son équilibre dynamique lors de la marche ou en position statique.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
            <p style="text-align: justify;">Pour le robot bipède, la dynamique (position angulaire des articulations, vitesse angulaire, etc.) est modélisée par un système d’équations d’état. Le LQR calcule alors les gains optimaux pour corriger les écarts de posture en ajustant les servomoteurs des jambes, tout en minimisant l’effort moteur et la consommation énergétique.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Maintenir l'équilibre du robot bipède en temps réel avec un minimum d'énergie
            </div>        
        </div>
    </div>

</div>
<h3>Références</h3>
<ul>
  <li>Bryson, A. E., & Ho, Y. C. (1975). <cite>Applied Optimal Control</cite>. Hemisphere Publishing.</li>
  <li>Anderson, B. D., & Moore, J. B. (1990). <cite>Optimal Control: Linear Quadratic Methods</cite>. Prentice-Hall.</li>
  <li>Stanford University. <cite>Linear Quadratic Regulator (LQR)</cite> - Cours de robotique.</li>
  <li>Matlab Documentation. <cite>lqr function reference</cite>.</li>
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