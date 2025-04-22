---
layout: default
nav_exclude: true
title: Analyse en Composantes Principales (PCA)
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
        <h2>Qu'est-ce que l'Analyse en Composantes Principales ?</h2>
        <hr>
        <p class="lead justified-text">
            L'Analyse en Composantes Principales (PCA) est une méthode statistique de réduction de dimensionnalité qui transforme un ensemble de variables potentiellement corrélées en un ensemble de valeurs linéairement non corrélées appelées composantes principales.
        </p>
        <p class="justified-text">
            Cette technique est largement utilisée dans divers domaines comme la biologie, la finance, le machine learning, la psychométrie et bien d'autres. Elle permet de visualiser des données multidimensionnelles, d'éliminer le bruit et d'extraire les informations les plus pertinentes.
        </p>
        <div class="did-you-know">
            <h3>Le saviez-vous ?</h3>
            <p>La NASA utilise la PCA pour analyser les données hyperspectrales des télescopes spatiaux. Cette méthode permet de détecter des composés chimiques dans l'espace en réduisant la dimensionnalité des spectres de lumière capturés (plus de 200 longueurs d'onde différentes).</p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général de l'Analyse en Composantes Principales</h2>
        <p class="justified-text">
            La PCA repose sur une transformation linéaire qui projette les données dans un nouvel espace de dimension inférieure ou égale à l'espace original. Les axes de ce nouvel espace (les composantes principales) sont choisis pour maximiser la variance des données projetées.
        </p>
        <div class="math-equation">
            <p>$$X' = X \cdot W$$</p>
        </div>
        <p class="justified-text">Où \(X\) est la matrice des données centrées, \(W\) est la matrice des vecteurs propres de la matrice de covariance, et \(X'\) est la matrice des données transformées.</p>
        <div class="diagram-container">
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
                <iframe width="560" height="315"  src="https://www.youtube.com/embed/FD4DeN81ODY" title="PCA Visualization for Robotics" frameborder="0"  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"  allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>
</div>
        <p class="justified-text">
            Les étapes principales de l'algorithme PCA sont :
            <ol>
                <li>Centrer les données (soustraire la moyenne)</li>
                <li>Calculer la matrice de covariance</li>
                <li>Calculer les valeurs propres et vecteurs propres de la matrice de covariance</li>
                <li>Trier les composantes par ordre décroissant de variance expliquée</li>
                <li>Projeter les données originales sur les composantes sélectionnées</li>
            </ol>
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer cette notion au projet ?</h2>
        <p class="justified-text">
            Dans le cadre d'un projet de traitement de données, la PCA peut être utilisée pour :
            <ul>
                <li>Réduire la dimensionnalité des données avant l'apprentissage automatique</li>
                <li>Visualiser des données multidimensionnelles en 2D ou 3D</li>
                <li>Éliminer le bruit et les corrélations entre variables</li>
                <li>Extraire les caractéristiques les plus importantes</li>
            </ul>
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation de PCA en Python</span>
        </div>
        <pre><code>from sklearn.decomposition import PCA
import numpy as np

# Données d'exemple (4 dimensions)
X = np.array([[-1, -1, 0, 2], [-2, -1, 1, 1], [-3, -2, 2, 0], 
              [1, 1, 0, -2], [2, 1, -1, -1], [3, 2, -2, 0]])

# Initialisation de PCA avec 2 composantes
pca = PCA(n_components=2)

# Application de PCA
X_transformed = pca.fit_transform(X)

print("Données transformées :")
print(X_transformed)
print("\nVariance expliquée par composante :", pca.explained_variance_ratio_)
</code></pre>
    </div>
<h2>Applications de la PCA dans un robot bipède</h2>
<div class="pid-application">
    <div class="application-card">
        <h3>Analyse des capteurs inertiels</h3>
        <p>La PCA peut traiter les données des IMU (Inertial Measurement Units) pour :</p>
        <ul>
            <li>Extraire les mouvements principaux (avancement, balancement)</li>
            <li>Détecter les vibrations parasites</li>
            <li>Simplifier le contrôle d'équilibre</li>
        </ul>        
        <p><strong>Exemple concret :</strong> En réduisant les 6 dimensions des données IMU (3 accélérations + 3 rotations) à seulement 2 composantes principales, on peut visualiser facilement l'état d'équilibre du robot.</p>
    </div>
    <div class="application-card">
        <h3>Optimisation des trajectoires</h3>
        <p>Analyse des patterns de marche par PCA :</p>
        <div style="font-size:14px; text-align:center; margin:10px 0;">
            $$ \text{Trajectoire} = \sum_{i=1}^{k} \alpha_i \cdot \text{PC}_i $$
        </div>
        <p>Où :</p>
        <ul style="margin-top:5px;">
            <li><strong>PC<sub>i</sub></strong> : les mouvements principaux extraits (ex: mouvement avant/arrière, balancement latéral)</li>
            <li><strong>α<sub>i</sub></strong> : l'importance de chaque mouvement dans la marche</li>
        </ul>        
        <p><strong>Avantage :</strong> Cette décomposition permet d'adapter la marche en modifiant seulement quelques coefficients (α) au lieu de recalculer tous les angles articulaires.</p>
    </div>
    <div class="application-card">
        <h3>Détection de mouvements anormaux</h3>
        <p>La PCA aide à repérer les comportements inhabituels :</p>
        <ol style="margin-top:10px;">
            <li>Apprendre les mouvements normaux du robot</li>
            <li>Calculer l'erreur de reconstruction</li>
            <li>Détecter quand le robot trébuche ou perd l'équilibre</li>
        </ol>        
        <p><strong>En pratique :</strong> Si l'erreur dépasse un seuil, le système peut déclencher une correction d'équilibre ou un arrêt d'urgence.</p>
    </div>
</div>

<h3>Références</h3>
<ul>
  <li>Jolliffe, I. T. (2002). <cite>Principal Component Analysis</cite> (2nd ed.). Springer.</li>
  <li>Abdi, H., & Williams, L. J. (2010). <cite>Principal component analysis</cite>. Wiley Interdisciplinary Reviews: Computational Statistics, 2(4), 433-459.</li>
  <li>Shlens, J. (2014). <cite>A tutorial on principal component analysis</cite>. arXiv preprint arXiv:1404.1100.</li>
  <li>Bishop, C. M. (2006). <cite>Pattern Recognition and Machine Learning</cite>. Springer (chapitre 12).</li>
</ul>