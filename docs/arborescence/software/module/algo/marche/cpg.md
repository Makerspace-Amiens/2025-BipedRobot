---
layout: default
nav_exclude: true
title: CPG (Central Pattern Generator)
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

.cpg-container {
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

<div class="cpg-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce qu'un CPG (Central Pattern Generator) ?</h2>
        <hr>
        <p class="lead justified-text">
            Un Central Pattern Generator (CPG) est un réseau neuronal capable de produire des motifs rythmiques sans nécessiter d'entrées sensorielles ou de commandes centrales.
        </p>
        <p class="justified-text">
            Dans le contexte de la robotique et de la génération de marche, les CPGs sont utilisés pour créer des mouvements rythmiques coordonnés comme la marche, la nage ou le vol chez les animaux, et sont reproduits artificiellement pour contrôler les robots.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Les CPGs biologiques ont été découverts en étudiant comment des animaux, comme les salamandres ou les cafards, pouvaient continuer à marcher même après que leur moelle épinière ait été séparée de leur cerveau.
            </p>
        </div>
    </section>

    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe des CPGs pour la génération de marche</h2>
        <p class="justified-text">
            Les CPGs artificiels pour la marche sont typiquement implémentés comme des systèmes d'oscillateurs couplés, souvent modélisés par des équations différentielles non-linéaires.
        </p>
        <div class="math-equation">
            <p>$$\dot{x}_i = \alpha x_i - \omega y_i + \sum_{j=1}^N w_{ij} f(x_j, y_j)$$</p>
            <p>$$\dot{y}_i = \omega x_i + \alpha y_i + \sum_{j=1}^N w_{ij} f(x_j, y_j)$$</p>
        </div>
        <p class="justified-text">
            Chaque oscillateur dans le réseau CPG correspond typiquement à un degré de liberté (par exemple une articulation de la jambe). Les connexions entre oscillateurs déterminent la coordination entre les membres.
        </p>
    </section>

    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Application des CPGs en robotique mobile</h2>
        <p class="justified-text">
            Dans un projet de robotique, un CPG peut être utilisé pour générer les signaux de commande des actionneurs qui contrôlent les mouvements des jambes du robot. Les paramètres du CPG peuvent être ajustés pour différentes allures (marche lente, course, etc.).
        </p>
    </section>

    <div class="code-container">
        <div class="code-header">
            <span>Implémentation simplifiée d'un oscillateur CPG</span>
        </div>
        <pre><code>class CPGOscillator:
    def __init__(self, alpha, omega, coupling_weights):
        self.alpha = alpha  # paramètre de stabilité
        self.omega = omega  # fréquence
        self.weights = coupling_weights  # poids des connexions
        
    def update(self, x, y, neighbors):
        dx = self.alpha * x - self.omega * y
        dy = self.omega * x + self.alpha * y
        
        # Couplage avec les oscillateurs voisins
        for j, (xj, yj) in enumerate(neighbors):
            dx += self.weights[j] * (xj - x)
            dy += self.weights[j] * (yj - y)
            
        return dx, dy</code></pre>
    </div>

<h2>Implémentation pour robot bipède</h2>
<div class="application-card">
    <h3>Architecture de base</h3>
    <p>Un CPG pour bipède utilise typiquement :</p>
    <ul>
        <li>6 oscillateurs (hanche/genou/cheville × 2 jambes)</li>
        <li>Couplage alterné entre jambes (déphasage 180°)</li>
        <li>Couplage synchronisé pour les articulations d'une même jambe</li>
    </ul>
    <div class="goal">
        <span class="label">Fonctionnement :</span>
        <ol>
            <li>Le CPG génère des signaux rythmiques</li>
            <li>Transformation en positions articulaires</li>
            <li>Correction par feedback sensoriel</li>
        </ol>
    </div>
</div>
</div>

<h3>Références</h3>
<ul>
  <li>Ijspeert, A. J. (2008). <cite>Central pattern generators for locomotion control in animals and robots: A review</cite>. Neural Networks, 21(4), 642-653.</li>
  <li>Grillner, S. (2003). <cite>The motor infrastructure: From ion channels to neuronal networks</cite>. Nature Reviews Neuroscience, 4(7), 573-586.</li>
  <li>Kimura, H., Fukuoka, Y., & Cohen, A. H. (2007). <cite>Adaptive dynamic walking of a quadruped robot on natural ground based on biological concepts</cite>. The International Journal of Robotics Research, 26(5), 475-490.</li>
  <li>Righetti, L., & Ijspeert, A. J. (2008). <cite>Pattern generators with sensory feedback for the control of quadruped locomotion</cite>. IEEE International Conference on Robotics and Automation.</li>
</ul>