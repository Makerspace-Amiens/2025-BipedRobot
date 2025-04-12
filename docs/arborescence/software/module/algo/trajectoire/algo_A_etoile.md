---
layout: default
nav_exclude: true
title: A étoile
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
        <h2>Qu'est-ce que l'algorithme A* (A star) ?</h2>
        <hr>
        <p class="lead justified-text">
            L'algorithme A* (prononcé "A étoile") est un algorithme de recherche de chemin dans un graphe, entre un nœud initial et un nœud final. Il est largement utilisé en intelligence artificielle et en robotique pour trouver des chemins optimaux.
        </p>
        <p class="justified-text">
            A* combine les avantages de l'algorithme de Dijkstra (qui garantit un chemin optimal) et de la recherche gloutonne (qui est efficace). Il utilise une fonction heuristique pour estimer le coût restant jusqu'à la destination, ce qui le rend très efficace pour trouver des solutions optimales.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                L'algorithme A* a été développé en 1968 par Peter Hart, Nils Nilsson et Bertram Raphael. Il est considéré comme l'un des algorithmes de recherche de chemin les plus performants lorsqu'une bonne heuristique est disponible.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général de l'algorithme A*</h2>
        <p class="justified-text">
            A* fonctionne en maintenant une liste de nœuds à explorer (open list) et une liste de nœuds déjà explorés (closed list). À chaque étape, il sélectionne le nœud le plus prometteur selon la fonction d'évaluation :
        </p>
        <div class="math-equation">
            <p>$$f(n) = g(n) + h(n)$$</p>
        </div>
        <p class="justified-text">
            Où :
            <ul>
                <li><strong>g(n)</strong> est le coût du chemin du nœud de départ au nœud n</li>
                <li><strong>h(n)</strong> est l'estimation heuristique du coût du chemin du nœud n au nœud d'arrivée</li>
                <li><strong>f(n)</strong> est le coût total estimé du chemin passant par n</li>
            </ul>
        </p>
        <div class="diagram-container">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/-L-WgKMFuhE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <p class="justified-text">
            L'algorithme est complet (il trouvera toujours une solution si elle existe) et optimal (il trouvera la solution la moins coûteuse) si l'heuristique est admissible (ne surestime jamais le coût réel).
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer cette notion au projet ?</h2>
        <p class="justified-text">
            Dans un projet de robotique ou de jeu vidéo, A* peut être utilisé pour :
            <ul>
                <li>Calculer des trajectoires optimales pour un robot</li>
                <li>Trouver le chemin le plus court dans un labyrinthe ou une carte</li>
                <li>Planifier des déplacements en évitant les obstacles</li>
                <li>Optimiser les déplacements d'unités dans un jeu de stratégie</li>
            </ul>
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation de l'algorithme A*</span>
            <button onclick="copyCode()">📋 Copier</button>
        </div>
        <pre><code>def a_star(start, goal, graph):
    open_set = PriorityQueue()
    open_set.put(start, 0)
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    while not open_set.empty():
        current = open_set.get()

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph.neighbors(current):
            tentative_g_score = g_score[current] + graph.cost(current, neighbor)
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in open_set:
                    open_set.put(neighbor, f_score[neighbor])

    return None  # Pas de chemin trouvé</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir l'algorithme A*?</h2>
    <div class="pid-application">
        <div class="application-card">
            <h3>Système de navigation</h3>
            <p>Dans un système de navigation autonome, A* peut être utilisé pour calculer le chemin optimal entre la position actuelle et la destination.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Pour un robot de livraison dans un entrepôt, A* peut calculer le chemin le plus court entre les rayonnages en tenant compte des allées, des obstacles fixes et des zones à éviter.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Implémenter A* pour permettre au robot de trouver son chemin de manière autonome tout en optimisant la distance parcourue.
            </div>        
        </div>
    </div>
</div>

<h3>Références</h3> <!--Style APA-->
<ul>
  <li>James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). <cite>An Introduction to Statistical Learning</cite>. Springer.</li>
  <li>Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). <cite>Introduction to Linear Regression Analysis</cite>. Wiley.</li>
  <li>Pedregosa, F., et al. (2011). <cite>Scikit-learn: Machine Learning in Python</cite>. Journal of Machine Learning Research.</li>
  <li>Galton, F. (1886). <cite>Regression Towards Mediocrity in Hereditary Stature</cite>. The Journal of the Anthropological Institute.</li>
</ul>