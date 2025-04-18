---
layout: default
nav_exclude: true
title: Trapèze vitesse pour moteurs
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

.trapeze-container {
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

<div class="trapeze-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce que le profil trapèze vitesse ?</h2>
        <hr>
        <p class="lead justified-text">
            Le profil trapèze vitesse est une méthode de contrôle de mouvement qui permet d'optimiser l'accélération et la décélération des moteurs pour un mouvement fluide et précis.
        </p>
        <p class="justified-text">
            Ce profil divise le mouvement en trois phases : une phase d'accélération, une phase à vitesse constante, et une phase de décélération. Cette approche est particulièrement utile pour les robots bipèdes où les mouvements doivent être précis et contrôlés pour maintenir l'équilibre.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Le profil trapèze est largement utilisé en robotique car il réduit les à-coups mécaniques et les oscillations, tout en minimisant la consommation d'énergie.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe du trapèze vitesse</h2>
        <p class="justified-text">
            Le profil trapèze se caractérise par trois paramètres principaux :
        </p>
        <ul>
            <li>Vitesse maximale (Vmax)</li>
            <li>Accélération (A)</li>
            <li>Décélération (D)</li>
        </ul>
        <div class="math-equation">
            <p>$$ t_{acc} = \frac{V_{max}}{A} \quad t_{dec} = \frac{V_{max}}{D} $$</p>
        </div>
        <p class="justified-text">
            Pour un robot bipède, ces paramètres doivent être soigneusement choisis en fonction de la dynamique du robot, de sa masse et des contraintes mécaniques des articulations.
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Application au robot bipède</h2>
        <p class="justified-text">
            Pour un robot bipède, le profil trapèze vitesse peut être utilisé pour contrôler :
        </p>
        <ul>
            <li>Les mouvements des articulations (hanches, genoux, chevilles)</li>
            <li>La transition du poids d'une jambe à l'autre</li>
            <li>Les mouvements de marche ou de rotation</li>
        </ul>
        <p class="justified-text">
            L'implémentation nécessite de synchroniser parfaitement les moteurs des deux jambes pour maintenir l'équilibre pendant toutes les phases du mouvement.
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation du trapèze vitesse (Arduino/C++)</span>
        </div>
        <pre><code>class TrapezoidalProfile {
public:
    TrapezoidalProfile(float maxVel, float accel, float decel) 
        : Vmax(maxVel), A(accel), D(decel) {}
    
    void compute(float distance) {
        // Calcul des temps d'accélération et décélération
        t_acc = Vmax / A;
        t_dec = Vmax / D;
        
        // Distance nécessaire pour atteindre Vmax
        d_acc = 0.5 * A * t_acc * t_acc;
        d_dec = 0.5 * D * t_dec * t_dec;
        
        if (d_acc + d_dec > distance) {
            // Profil triangulaire (pas de phase à vitesse constante)
            Vmax = sqrt((2 * distance * A * D) / (A + D));
            t_acc = Vmax / A;
            t_dec = Vmax / D;
            t_const = 0;
        } else {
            // Profil trapèze classique
            t_const = (distance - d_acc - d_dec) / Vmax;
        }
    }
    
    float getVelocity(float t) {
        if (t < t_acc) return A * t;
        else if (t < t_acc + t_const) return Vmax;
        else if (t < t_acc + t_const + t_dec) return Vmax - D * (t - t_acc - t_const);
        else return 0;
    }

private:
    float Vmax, A, D;
    float t_acc = 0, t_dec = 0, t_const = 0;
    float d_acc = 0, d_dec = 0;
};</code></pre>
    </div>
    <h2>Intégration dans le contrôle des moteurs du bipède</h2>
    <div class="pid-application">
        <div class="application-card">
            <h3>Contrôle des articulations</h3>
            <p>Chaque articulation peut être contrôlée avec son propre profil trapèze, synchronisé avec les autres moteurs.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Pour un pas avant, la hanche et le genou de la jambe avant suivent un profil trapèze pendant que la jambe arrière maintient l'équilibre.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Atteindre la position cible en minimisant les oscillations et en conservant l'équilibre
            </div>
        </div>
        <div class="application-card">
            <h3>Transition de poids</h3>
            <p>Le transfert du poids d'une jambe à l'autre doit suivre un profil précis pour éviter les chocs.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Transition fluide avec accélération et décélération contrôlées
            </div>
        </div>
    </div>
</div>

<h3>Références</h3>
<ul>
  <li>Craig, J. J. (2005). <cite>Introduction to Robotics: Mechanics and Control</cite>. Pearson Education.</li>
  <li>Siciliano, B., Sciavicco, L., Villani, L., & Oriolo, G. (2009). <cite>Robotics: Modelling, Planning and Control</cite>. Springer.</li>
  <li>Spong, M. W., Hutchinson, S., & Vidyasagar, M. (2006). <cite>Robot Modeling and Control</cite>. Wiley.</li>
</ul>