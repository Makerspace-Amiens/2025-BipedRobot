---
layout: default
nav_exclude: true
title: Logique Floue (Fuzzy Logic)
---
<!-- Template pour la Logique Floue (Fuzzy Logic) -->

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

.fuzzy-container {
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

<div class="fuzzy-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce que la Logique Floue (Fuzzy Logic) ?</h2>
        <hr>
        <p class="lead justified-text">
            La logique floue est une forme de logique multivaluée qui permet de traiter des concepts imprécis comme "un peu", "beaucoup" ou "environ", contrairement à la logique booléenne classique qui ne connaît que vrai ou faux.
        </p>
        <p class="justified-text">
            Développée par Lotfi Zadeh en 1965, elle est particulièrement utile pour les systèmes de contrôle complexes où les entrées sont continues et imprécises, comme dans le cas des robots bipèdes.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                La logique floue est largement utilisée dans les systèmes de contrôle industriels, les appareils électroménagers (comme les machines à laver "intelligentes") et même dans certains systèmes de freinage ABS.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général de la Logique Floue</h2>
        <p class="justified-text">
            Un système flou se compose de trois étapes principales : la fuzzification (transformation des entrées précises en degrés d'appartenance à des ensembles flous), l'inférence (application des règles floues) et la défuzzification (transformation du résultat flou en sortie précise).
        </p>
        <div class="math-equation">
            <p>$$\mu_A(x) : X \rightarrow [0,1]$$</p>
        </div>
        <p class="justified-text">
            Les règles floues prennent la forme "SI...ALORS..." et permettent d'exprimer une connaissance experte sous une forme compréhensible par la machine. Par exemple : "SI l'inclinaison est Forte ALORS augmente beaucoup le couple".
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer la Logique Floue au robot bipède ?</h2>
        <p class="justified-text">
            Pour un robot bipède, la logique floue est idéale pour le contrôle de l'équilibre et de la marche, car elle peut gérer les multiples capteurs et actionneurs de manière robuste face aux incertitudes des mesures et aux perturbations externes.
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation d'un contrôleur flou en Python (skfuzzy)</span>
        </div>
        <pre><code>import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variables d'entrée/sortie
inclinaison = ctrl.Antecedent(np.arange(-30, 31, 1), 'inclinaison')
vitesse_ang = ctrl.Antecedent(np.arange(-10, 11, 1), 'vitesse_angulaire')
couple = ctrl.Consequent(np.arange(-5, 6, 1), 'couple_moteur')

# Fonctions d'appartenance
names = ['neg_grande', 'neg_moyenne', 'nulle', 'pos_moyenne', 'pos_grande']
inclinaison.automf(names=names)
vitesse_ang.automf(names=names)
couple.automf(names=names)

# Règles floues
rule1 = ctrl.Rule(inclinaison['neg_grande'] & vitesse_ang['neg_moyenne'], couple['pos_grande'])
rule2 = ctrl.Rule(inclinaison['pos_moyenne'] & vitesse_ang['nulle'], couple['neg_moyenne'])
# ... autres règles

# Système de contrôle
systeme_controle = ctrl.ControlSystem([rule1, rule2])
simulation = ctrl.ControlSystemSimulation(systeme_controle)

# Exemple d'utilisation
simulation.input['inclinaison'] = -15  # degrés
simulation.input['vitesse_angulaire'] = -3  # degrés/s
simulation.compute()
print(simulation.output['couple_moteur'])</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir la Logique Floue ?</h2>
    <div class="fuzzy-application">
        <div class="application-card">
            <h3>Contrôle de l'équilibre</h3>
            <p>Un contrôleur flou peut déterminer les corrections à apporter aux moteurs en fonction de l'inclinaison et de la vitesse angulaire du robot, exprimées en termes linguistiques comme "légèrement penché" ou "chutant rapidement".</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Le système évalue en temps réel l'angle d'inclinaison et sa dérivée pour ajuster le couple des moteurs des hanches et des chevilles selon des règles floues préétablies.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Maintenir l'équilibre du robot dans diverses conditions avec une réponse robuste aux perturbations
            </div>        
        </div>
        <div class="application-card">
            <h3>Gestion de la marche</h3>
            <p>La logique floue peut coordonner le mouvement des jambes en fonction de la vitesse désirée, de l'état du terrain et de l'équilibre actuel, en ajustant dynamiquement la longueur et la fréquence des pas.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Adapter la démarche du robot à différentes situations tout en conservant la stabilité
            </div>
        </div>
        <div class="application-card">
            <h3>Détection et réaction aux obstacles</h3>
            <p>En combinant les données des capteurs de distance et d'inclinaison, un système flou peut décider de la meilleure réaction (ralentir, ajuster la trajectoire, s'arrêter) face à un obstacle imprévu.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Permettre une navigation autonome et sûre dans des environnements complexes
            </div>
        </div>
    </div>
</div>

<h3>Références</h3> <!--Style APA-->
<ul>
  <li>Zadeh, L. A. (1965). <cite>Fuzzy sets</cite>. Information and Control, 8(3), 338-353.</li>
  <li>Passino, K. M., & Yurkovich, S. (1998). <cite>Fuzzy Control</cite>. Addison-Wesley.</li>
  <li>Ross, T. J. (2010). <cite>Fuzzy Logic with Engineering Applications</cite> (3rd ed.). Wiley.</li>
  <li>Lee, C. C. (1990). <cite>Fuzzy logic in control systems: fuzzy logic controller</cite>. IEEE Transactions on Systems, Man, and Cybernetics, 20(2), 404-418.</li>
</ul>