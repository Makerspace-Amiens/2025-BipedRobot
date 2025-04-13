---
layout: default
nav_exclude: true
title: Model Predictive Control
---
<!-- TEMPLATE POUR MODEL PREDICTIVE CONTROL -->

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

.mpc-container {
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

<div class="mpc-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce que le Model Predictive Control ?</h2>
        <hr>
        <p class="lead justified-text">
            Le Model Predictive Control (MPC) ou Commande Prédictive est une méthode avancée de contrôle qui utilise un modèle du système pour prédire son comportement futur et calculer une séquence optimale de commandes.
        </p>
        <p class="justified-text">
            Contrairement aux contrôleurs classiques qui réagissent aux erreurs passées, le MPC anticipe les évolutions futures du système en résolvant à chaque pas de temps un problème d'optimisation sous contraintes.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Le MPC est largement utilisé dans l'industrie pétrochimique depuis les années 1980, où il permet de gérer des processus complexes avec des contraintes multiples tout en optimisant les coûts de production.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général du MPC</h2>
        <p class="justified-text">
            Le MPC fonctionne selon trois étapes clés répétées à chaque instant :
        </p>
        <ol>
            <li>Prédiction : Utilisation d'un modèle pour prédire les sorties futures sur un horizon donné</li>
            <li>Optimisation : Résolution d'un problème d'optimisation pour minimiser un critère sous contraintes</li>
            <li>Application : Seul le premier élément de la séquence optimisée est appliqué au système</li>
        </ol>
        <div class="math-equation">
            <p>$$\min_u \sum_{k=0}^{N_p} \|y(t+k|t) - r(t+k)\|^2_Q + \sum_{k=0}^{N_c-1} \|\Delta u(t+k)\|^2_R$$</p>
        </div>
        <p class="justified-text">
            L'horizon de prédiction (Np) et l'horizon de contrôle (Nc) sont des paramètres clés. Le MPC peut intégrer naturellement des contraintes sur les états, les sorties et les commandes, ce qui le rend particulièrement robuste.
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer le MPC au projet ?</h2>
        <p class="justified-text">
            Dans le cadre d'un projet de robotique ou d'automatisme, le MPC peut être utilisé pour la commande de trajectoire, la régulation de processus ou l'évitement d'obstacles. Sa capacité à gérer les contraintes le rend idéal pour des systèmes avec limites physiques (vitesse max, amplitude des actionneurs, etc.).
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation simplifiée de MPC</span>
        </div>
        <pre><code># Pseudocode pour MPC
def mpc_controller(current_state, reference):
    # Initialisation
    u_opt = []
    
    # Boucle d'optimisation sur l'horizon
    for k in range(horizon):
        # Calcul des prédictions
        predictions = model.predict(current_state, u_opt)
        
        # Résolution du problème d'optimisation
        u_opt = solve_optimization(predictions, reference)
        
        # Application de la première commande
        apply_control(u_opt[0])
        
        # Mise à jour de l'état
        current_state = get_new_state()
</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir le MPC ?</h2>
    <div class="mpc-application">
        <div class="application-card">
            <h3>Commande de trajectoire</h3>
            <p>Le MPC peut générer des trajectoires optimales en tenant compte des contraintes dynamiques du système.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Pour un robot mobile, le MPC peut calculer la séquence de commandes (vitesse, angle) permettant d'atteindre une cible tout en évitant les obstacles et en respectant les limites physiques du robot.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Minimiser le temps de parcours tout en garantissant la sécurité et le confort (accélérations limitées)
            </div>        
        </div>
    </div>
</div>

<h3>Références</h3> <!--Style APA-->
<ul>
  <li>Rawlings, J. B., Mayne, D. Q., & Diehl, M. (2017). <cite>Model Predictive Control: Theory, Computation, and Design</cite>. Nob Hill Publishing.</li>
  <li>Camacho, E. F., & Bordons, C. (2007). <cite>Model Predictive Control</cite>. Springer Science & Business Media.</li>
  <li>Garcia, C. E., Prett, D. M., & Morari, M. (1989). <cite>Model predictive control: theory and practice—a survey</cite>. Automatica, 25(3), 335-348.</li>
  <li>Qin, S. J., & Badgwell, T. A. (2003). <cite>A survey of industrial model predictive control technology</cite>. Control engineering practice, 11(7), 733-764.</li>
</ul>