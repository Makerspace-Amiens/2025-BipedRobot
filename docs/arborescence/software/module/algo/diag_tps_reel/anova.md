---
layout: default
nav_exclude: true
title: ANOVA
---
<!-- Template modifié pour l'Analyse de la Variance (ANOVA) -->

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

.anova-container {
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

<div class="anova-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce que l'Analyse de la Variance (ANOVA) ?</h2>
        <hr>
        <p class="lead justified-text">
            L'Analyse de la Variance (ANOVA) est une méthode statistique utilisée pour comparer les moyennes de plusieurs groupes et déterminer si des différences significatives existent entre eux.
        </p>
        <p class="justified-text">
            Développée par Ronald Fisher dans les années 1920, l'ANOVA décompose la variabilité totale des données en composantes expliquées par différents facteurs et en résidus aléatoires.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                L'ANOVA est particulièrement utile lorsque vous avez plus de deux groupes à comparer, car elle évite le problème d'accumulation d'erreurs qui survient lorsqu'on effectue de multiples tests t.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général de l'ANOVA</h2>
        <p class="justified-text">
            L'ANOVA repose sur le calcul de deux estimations de la variance : la variance inter-groupes (expliquée par le facteur étudié) et la variance intra-groupes (résiduelle). Le test F compare ces deux variances.
        </p>
        <div class="math-equation">
            <p>$$F = \frac{\text{Variance inter-groupes}}{\text{Variance intra-groupes}} = \frac{MS_{between}}{MS_{within}}$$</p>
        </div>
        <p class="justified-text">
            Si la valeur F calculée est supérieure à la valeur critique de la distribution F, on rejette l'hypothèse nulle d'égalité des moyennes et on conclut qu'au moins un groupe diffère significativement des autres.
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer l'ANOVA au projet de robot bipède ?</h2>
        <p class="justified-text">
            Dans le contexte d'un robot bipède, l'ANOVA peut être utilisée pour comparer l'efficacité de différents algorithmes de contrôle, paramètres de marche, ou configurations matérielles en mesurant des variables comme la stabilité, la consommation énergétique ou la vitesse.
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation de l'ANOVA en Python</span>
        </div>
        <pre><code>import numpy as np
import pandas as pd
from scipy import stats

# Données expérimentales: performances de 3 algorithmes différents
algo1 = [8.5, 8.2, 8.4, 8.3, 8.6]  # Algorithme A
algo2 = [7.9, 8.0, 7.8, 7.7, 8.1]  # Algorithme B
algo3 = [8.8, 8.7, 8.9, 8.6, 8.5]  # Algorithme C

# Test ANOVA unidirectionnelle
f_value, p_value = stats.f_oneway(algo1, algo2, algo3)

print(f"Valeur F: {f_value:.4f}")
print(f"Valeur p: {p_value:.4f}")

if p_value < 0.05:
    print("Différence significative entre les algorithmes")
else:
    print("Pas de différence significative")</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir l'ANOVA ?</h2>
    <div class="anova-application" style=" margin-top:15px;">
        <div class="application-card">
            <h3>Évaluation des algorithmes de contrôle</h3>
            <p>Comparaison de plusieurs algorithmes de contrôle PID pour déterminer lequel offre les meilleures performances en termes de précision et de consommation énergétique.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Sélectionner l'algorithme le plus efficace pour le maintien de l'équilibre
            </div>
        </div>
        <div class="application-card">
            <h3>Analyse des capteurs</h3>
            <p>Évaluation de la précision et de la cohérence des données provenant de différents capteurs (gyroscopes, accéléromètres) pour déterminer s'ils fournissent des mesures équivalentes.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Assurer la fiabilité du système de perception pour le contrôle du robot
            </div>
        </div>
    </div>
</div>

<h3>Références</h3> <!--Style APA-->
<ul>
  <li>Fisher, R. A. (1925). <cite>Statistical Methods for Research Workers</cite>. Edinburgh: Oliver and Boyd.</li>
  <li>Montgomery, D. C. (2017). <cite>Design and Analysis of Experiments</cite> (9th ed.). Wiley.</li>
  <li>Field, A. (2018). <cite>Discovering Statistics Using IBM SPSS Statistics</cite> (5th ed.). Sage.</li>
  <li>Howell, D. C. (2012). <cite>Statistical Methods for Psychology</cite> (8th ed.). Cengage Learning.</li>
</ul>