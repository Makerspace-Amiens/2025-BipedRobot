---
layout: default
nav_exclude: true
title: Rapidly Exploring Random Tree
---
<!-- TEMPLATE POUR RAPIDLY EXPLORING RANDOM TREE (RRT) -->

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

.rrt-container {
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

<div class="rrt-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce qu'un RRT ?</h2>
        <hr>
        <p class="lead justified-text">
            Le Rapidly Exploring Random Tree (RRT) est un algorithme de planification de trajectoire qui explore efficacement des espaces de grande dimension en construisant un arbre couvrant qui se déploie rapidement dans l'espace non exploré.
        </p>
        <p class="justified-text">
            Développé par Steven M. LaValle en 1998, le RRT est particulièrement efficace pour résoudre des problèmes de planification de mouvement avec obstacles, où l'espace de configuration est complexe et de grande dimension.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Le RRT et ses variantes (comme RRT*) sont largement utilisés en robotique, notamment par la NASA pour la planification de trajectoires de robots spatiaux et par les voitures autonomes pour la navigation en environnement complexe.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général du RRT</h2>
        <p class="justified-text">
            L'algorithme RRT fonctionne selon les étapes suivantes :
        </p>
        <ol>
            <li>Initialisation : Création d'un arbre avec le point de départ comme racine</li>
            <li>Génération d'un point aléatoire dans l'espace de configuration</li>
            <li>Recherche du nœud existant le plus proche du point aléatoire</li>
            <li>Extension vers le point aléatoire (en vérifiant les collisions)</li>
            <li>Répétition jusqu'à atteindre la destination ou dépasser le nombre maximal d'itérations</li>
        </ol>             
   <div class="diagram-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/OXikozpLFGo" style="border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
    </iframe>
</div>       
        <p class="justified-text">
            Le RRT présente plusieurs avantages : il ne nécessite pas de discrétisation explicite de l'espace, gère bien les espaces de grande dimension, et converge vers une solution faisable (mais pas nécessairement optimale) si elle existe.
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer le RRT au projet ?</h2>
        <p class="justified-text">
            Dans un projet de robotique ou d'IA, le RRT peut être utilisé pour :
            <ul>
                <li>Planification de trajectoire pour robots mobiles</li>
                <li>Navigation autonome avec évitement d'obstacles</li>
                <li>Mouvement de bras robotiques dans des environnements encombrés</li>
                <li>Jeux vidéo pour le déplacement des NPC (personnages non-joueurs)</li>
            </ul>
        </p>
    </section>

    <div class="code-container">
        <div class="code-header">
            <span>Implémentation simplifiée de RRT</span>
        </div>
        <pre><code>def build_rrt(start, goal, space, obstacles, max_iter=1000, step_size=0.1):
    tree = Tree(start)
    
    for _ in range(max_iter):
        q_rand = random_sample(space)  # Point aléatoire
        q_near = nearest_neighbor(tree, q_rand)  # Nœud le plus proche
        q_new = extend(q_near, q_rand, step_size)  # Nouvelle configuration
        
        if not collision(q_new, obstacles):
            tree.add_node(q_new)
            tree.add_edge(q_near, q_new)
            
            if distance(q_new, goal) < threshold:
                return extract_path(tree, q_new)
    
    return None  # Aucun chemin trouvé
</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir le RRT ?</h2>
    <div class="rrt-application">
    <div class="application-card">
        <h3>Module de planification de mouvement</h3>
        <p>Le RRT peut être utilisé pour planifier des séquences de pas dans un environnement avec obstacles.</p>
        <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
        <p style="text-align: justify;">
            Pour un robot bipède, le RRT* peut générer un enchaînement de positions stables (appuis successifs) permettant d’atteindre une cible tout en évitant les obstacles et en respectant les contraintes de stabilité dynamique (ZMP, centre de masse, etc.).
        </p>
        <div class="goal">
            <span class="label">Objectif :</span> Générer une séquence de mouvements réalisables qui garantissent équilibre et évitement d’obstacles
        </div>        
    </div>
</div>

</div>

<h3>Références</h3>
<ul>
  <li>LaValle, S. M. (1998). <cite>Rapidly-exploring random trees: A new tool for path planning</cite>. Technical Report, Iowa State University.</li>
  <li>Karaman, S., & Frazzoli, E. (2011). <cite>Sampling-based algorithms for optimal motion planning</cite>. The International Journal of Robotics Research, 30(7), 846-894.</li>
  <li>LaValle, S. M. (2006). <cite>Planning Algorithms</cite>. Cambridge University Press.</li>
  <li>Gammell, J. D., Srinivasa, S. S., & Barfoot, T. D. (2014). <cite>Informed RRT*: Optimal sampling-based path planning focused via direct sampling of an admissible ellipsoidal heuristic</cite>. IEEE/RSJ International Conference on Intelligent Robots and Systems.</li>
</ul>