---
layout: default
nav_exclude: true
title: Algorithme ZMP
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

.zmp-container {
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


<div class="zmp-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce que le Zero Moment Point (ZMP) ?</h2>
        <hr>
        <p class="lead justified-text">
            Le Zero Moment Point (ZMP) est un concept fondamental en robotique humanoïde qui représente le point sur le sol où le moment des forces est nul.
        </p>
        <p class="justified-text">
            Développé à l'origine pour la marche bipède, le ZMP est utilisé pour évaluer la stabilité d'un robot. Lorsque le ZMP reste à l'intérieur du polygone de sustentation (la zone délimitée par les points de contact avec le sol), le robot maintient son équilibre.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Le concept de ZMP a été introduit par Miomir Vukobratović dans les années 1960 pour le contrôle des robots marcheurs. Il est aujourd'hui largement utilisé dans les robots humanoïdes comme ASIMO et Atlas.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général du ZMP</h2>
        <p class="justified-text">
            Le ZMP est calculé à partir des forces et moments exercés par le robot sur le sol. Mathématiquement, il peut être exprimé comme :
        </p>
        <div class="math-equation">
            <p>$$x_{zmp} = \frac{\sum m_i(x_i(\ddot{z}_i + g) - z_i\ddot{x}_i) - \sum I_i\dot{\omega}_{iy}}{\sum m_i(\ddot{z}_i + g)}$$</p>
            <p>$$y_{zmp} = \frac{\sum m_i(y_i(\ddot{z}_i + g) - z_i\ddot{y}_i) - \sum I_i\dot{\omega}_{ix}}{\sum m_i(\ddot{z}_i + g)}$$</p>
        </div>
        <div class="diagram-container">
            <img src="{{ site.baseurl }}/assets/img/etude_algo/zmp/zmp.gif" alt="Illustration du Zero Moment Point" class="img-fluid">
            <p class="text-muted">Schéma expliquant le ZMP sur sol horizontal</p>
        </div>
        <p style="font-size: 0.8em; text-align: center;">Source image : <a href="https://fr.wikipedia.org/wiki/Zero_Moment_Point" target="_blank">Wikipédia - Zero Moment Point</a></p>
        <p class="justified-text">
            En pratique, le calcul du ZMP nécessite de connaître les positions, accélérations et inerties de tous les segments du robot. Pour les robots équipés de capteurs de force dans les pieds, le ZMP peut également être estimé directement à partir des mesures.
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer le ZMP dans un projet robotique ?</h2>
        <p class="justified-text">
            Dans un projet de robotique humanoïde ou quadrupède, le ZMP peut être utilisé pour :
            <ul>
                <li>Évaluer la stabilité du robot en temps réel</li>
                <li>Générer des trajectoires de marche stables</li>
                <li>Corriger la posture pour éviter les chutes</li>
                <li>Optimiser la consommation énergétique</li>
            </ul>
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation basique du ZMP</span>
        </div>
        <pre><code>class ZMPCalculator:
    def __init__(self, robot_mass, gravity=9.81):
        self.mass = robot_mass
        self.g = gravity
    
    def compute_zmp(self, com_pos, com_acc, total_moment):
        """
        Calcule le ZMP à partir de:
        - com_pos: position du centre de masse (x,y,z)
        - com_acc: accélération du centre de masse (ax,ay,az)
        - total_moment: moment total (Mx, My)
        """
        denominator = self.mass * (com_acc[2] + self.g)
        
        x_zmp = (com_pos[0] * (com_acc[2] + self.g) - 
                com_pos[2] * com_acc[0] - 
                total_moment[1]/self.mass) / denominator
        
        y_zmp = (com_pos[1] * (com_acc[2] + self.g) - 
                com_pos[2] * com_acc[1] + 
                total_moment[0]/self.mass) / denominator
        
        return (x_zmp, y_zmp)</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir le ZMP ?</h2>
    <div class="zmp-application">
        <div class="application-card">
            <h3>Contrôle de la marche</h3>
            <p>Le ZMP est essentiel pour générer des trajectoires de marche stables. En surveillant en permanence la position du ZMP, le système de contrôle peut ajuster les mouvements pour maintenir l'équilibre.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Dans un générateur de pas, le ZMP permet de déterminer la position optimale du pied suivant pour garantir la stabilité pendant le transfert de poids.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Maintenir le ZMP à l'intérieur du polygone de sustentation pendant au moins 80% du cycle de marche.
            </div>        
    </div>
</div>


<h3>Références</h3>
<ul>
  <li>Wikipédia. <cite>Zero Moment Point</cite>.</li>
  <li>Vukobratović, M., & Borovac, B. (2004). <cite>Zero-moment point—Thirty five years of its life</cite>. International Journal of Humanoid Robotics, 1(1), 157-173.</li>
  <li>Sardain, P., & Bessonnet, G. (2004). <cite>Forces acting on a biped robot. Center of pressure—Zero moment point</cite>. IEEE Transactions on Systems, Man, and Cybernetics, 34(5), 630-637.</li>
  <li>Boston Dynamics. <cite>Atlas Control System Whitepaper</cite> (ZMP-based stabilization).</li>
</ul>
