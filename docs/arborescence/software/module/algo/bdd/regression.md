---
layout: default
nav_exclude: true
title: Regression Linéaire
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
        <h2>Qu'est-ce que la Régression Linéaire ?</h2>
        <hr>
        <p class="lead justified-text">
           La Régression Linéaire est l'une des méthodes statistiques les plus fondamentales et les plus utilisées en analyse de données.
        </p>
        <p class="justified-text">
           La régression linéaire est une méthode statistique qui permet de modéliser la relation entre une variable dépendante (Y) et une ou plusieurs variables indépendantes (X) à l'aide d'une droite. Elle sert à :
        <ul style="margin-left:20px;">
            <li><strong>Prédire une valeur</strong> : Estimer des résultats futurs basés sur des données historiques</li>
            <li><strong>Comprendre les relations</strong> : Quantifier comment une variable influe sur une autre</li>
            <li><strong>Identifier les tendances</strong> : Détecter des patterns linéaires dans les données</li>
            <li><strong>Effectuer des analyses</strong> : Tester des hypothèses sur les relations entre variables</li>
        </ul>
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
               La régression linéaire a été développée par Francis Galton au 19ème siècle pour étudier la relation entre les tailles des parents et des enfants. Il a observé que les enfants de parents très grands avaient tendance à être plus petits que leurs parents, et vice versa - un phénomène qu'il a appelé "régression vers la moyenne", donnant ainsi son nom à cette méthode.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général de la Régression Linéaire</h2>
        <p class="justified-text">
            La régression linéaire simple modélise la relation entre deux variables par une droite d'équation :
        </p>
        <div class="math-equation">
            <p>$$ Y = aX + b + \epsilon $$</p>
        </div>
        <div style="text-align:justify;">
         <p>Où :</p>
            <ul>
                <li>Y : Variable dépendante</li>
                <li>X : Variable indépendante </li>
                <li>a : Coefficient directeur (pente)</li>
                <li>b : Ordonnée à l'origine</li>
                <li>ε : Terme d'erreur (bruit)</li>
            </ul>
        <p><strong> Variable Dépendante : </strong>La variable dépendante (<em>Y</em>) est celle que l'on cherche à prédire ou à expliquer. Sa valeur dépend de celle de la variable indépendante. Par exemple, si l'on étudie l'effet de l'entraînement sur la performance, la performance serait la variable dépendante.</p>
        <p><strong> Variable Indépendante : </strong>La variable indépendante (<em>X</em>) est celle que l'on manipule ou mesure pour observer son influence sur la variable dépendante. Elle est considérée comme la cause dans la relation. Dans l'exemple précédent, l'entraînement serait la variable indépendante.</p>
        </div>
        <div class="diagram-container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/1200px-Linear_regression.svg.png" alt="Exemple de régression linéaire" class="img-fluid">
            <p class="text-muted">Droite de régression optimale minimisant la somme des carrés des résidus</p>
        </div>
        <p class="justified-text">
            La méthode des moindres carrés ordinaires (MCO) est utilisée pour trouver les paramètres a et b qui minimisent la somme des carrés des écarts entre les valeurs observées et les valeurs prédites par le modèle.
        </p>
        <div class="did-you-know">
            <h3>Cas multivarié</h3>
            <p>
                Pour plusieurs variables explicatives, on parle de régression linéaire multiple :
                $$ Y = a_1X_1 + a_2X_2 + ... + a_nX_n + b + \epsilon $$
                Les principes restent similaires, mais l'interprétation devient plus complexe.
            </p>
        </div>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer cette notion au projet ?</h2>
        <p class="justified-text">
            La régression linéaire peut être utilisée dans divers contextes de projet :
        </p>
        <ul>
            <li>Prédiction de valeurs futures basées sur des tendances passées</li>
            <li>Analyse de l'impact de différentes variables sur une grandeur mesurée</li>
            <li>Lissage de données bruitées</li>
            <li>Détection d'anomalies (points très éloignés de la droite de régression)</li>
        </ul>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation Python de la Régression Linéaire</span>
        </div>
        <pre><code># Exemple avec scikit-learn
import numpy as np
from sklearn.linear_model import LinearRegression

# Données d'exemple
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Variable indépendante
Y = np.array([2, 4, 5, 4, 5])                 # Variable dépendante

# Création et entraînement du modèle
model = LinearRegression()
model.fit(X, Y)

# Prédiction
Y_pred = model.predict(X)

# Coefficients
print(f"Coefficient a (pente): {model.coef_[0]:.2f}")
print(f"Ordonnée à l'origine b: {model.intercept_:.2f}")
print(f"Score R²: {model.score(X, Y):.2f}")</code></pre>
    </div>
    <h2>Dans quels modules peut intervenir la Régression Linéaire ?</h2>
    <div class="pid-application">
        <div class="application-card">
            <h3>Module de stabilisation du robot</h3>
                <p>La régression peut être utilisée pour analyser l’évolution de l’angle d’inclinaison du robot afin de détecter une perte d’équilibre progressive.</p>
                <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Pendant la marche, on enregistre l’angle d’un gyroscope sur quelques secondes. On ajuste une droite. Si la pente est trop forte (le robot penche trop rapidement), alors une correction moteur peut être déclenchée automatiquement.</p>
        <div class="goal">
            <span class="label">Objectif :</span> anticiper une chute et stabiliser le robot plus efficacement.
        </div>
    </div>

<h3>Références</h3> <!--Style APA-->
<ul>
  <li>James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). <cite>An Introduction to Statistical Learning</cite>. Springer.</li>
  <li>Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). <cite>Introduction to Linear Regression Analysis</cite>. Wiley.</li>
  <li>Pedregosa, F., et al. (2011). <cite>Scikit-learn: Machine Learning in Python</cite>. Journal of Machine Learning Research.</li>
  <li>Galton, F. (1886). <cite>Regression Towards Mediocrity in Hereditary Stature</cite>. The Journal of the Anthropological Institute.</li>
</ul>