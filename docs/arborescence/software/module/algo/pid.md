---
layout: default
nav_exclude: true
title: Contrôleur PID - Explications
---

<!-- KaTeX CDN -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body);"></script>

<style>
:root {
    --primary-color:rgb(28, 80, 131);
    --secondary-color:rgb(28, 80, 131);;
    --accent-color: rgb(28, 80, 131);;
}

.pid-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.pid-equation {
    background-color: white;
    border-radius: 10px;
    padding: 2rem;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    margin: 2rem 0;
    border-left: 5px solid var(--accent-color);
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
}

.did-you-know {
    background-color: #f8f9fa;
    border-left: 4px solid var(--primary-color);
    border-radius: 8px;
    padding: 1.5rem;
    margin: 2rem 0;
}

.pid-application {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.application-card {
    background: #f8f9fa;
    border-left: 4px solid rgb(28, 80, 131);
    padding: 1.2rem;
    border-radius: 0 4px 4px 0;
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
    color: rgb(240, 240, 240);
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

.did-you-know i {
    margin-right: 10px;
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

.code-header button:hover {
    color: white;
}

pre {
    margin: 0;
    white-space: pre-wrap;
}

.lead {
    font-size: 1.25rem;
    font-weight: 300;
}

code {
    font-family: inherit;
}
</style>

<div class="pid-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce qu'un Contrôleur PID ?</h2>
        <p class="lead justified-text">
            Un contrôleur PID (Proportionnel, Intégral, Dérivé) est utilisé pour ajuster dynamiquement un système afin de minimiser une erreur entre une valeur mesurée et une consigne désirée.
        </p>
        <p class="justified-text">
            Ce type de contrôleur est largement employé dans de nombreux domaines, tels que la robotique, le contrôle moteur, l'équilibrage, les drones, les systèmes de chauffage/climatisation et bien d'autres applications industrielles.
        </p>
        <div class="did-you-know">
            <h3><i class="bi bi-lightbulb"></i> Saviez-vous ?</h3>
            <p>
                Le contrôleur PID a été inventé en 1911 par Elmer Sperry pour le pilotage automatique des navires, et a été formalisé mathématiquement en 1922 par Nicolas Minorsky.
            </p>
        </div>
    </section>
    <!-- Principe Général du PID -->
    <section id="principe">
        <h2>Principe Général du PID</h2>
        <div class="math-equation">
            e(t) = consigne - mesure
        </div>
        <div class="diagram-container">
            <img src="{{ site.baseurl }}/assets/img/etude_algo/pid.jpg" alt="Diagramme du contrôleur PID" class="img-fluid">
            <p class="text-muted" style="text-align: center;">Schéma de fonctionnement d'un contrôleur PID</p>
        </div>
        <h2>Équation Mathématique du PID</h2>
        <div class="math-equation">
            <p>$$u(t) = K_p \cdot e(t) + K_i \int e(t) dt + K_d \cdot \frac{de(t)}{dt}$$</p>
        </div>
        <p class="justified-text">
            Un contrôleur PID agit en combinant trois termes, chacun ayant un rôle spécifique dans la régulation du système :
        </p>
        <ul class="justified-text">
            <li><strong>Proportionnel (P) :</strong> Il génère une action proportionnelle à l'erreur actuelle. Un grand coefficient <em>Kp</em> entraîne une correction rapide mais peut causer une instabilité.</li><br>
            <li><strong>Intégral (I) :</strong> Il corrige l’erreur accumulée dans le temps pour éliminer l’écart statique. Un <em>Ki</em> trop grand peut rendre le système lent et provoquer des oscillations.</li><br>
            <li><strong>Dérivé (D) :</strong> Il anticipe les variations de l'erreur en utilisant sa dérivée. Il aide à réduire les oscillations mais est sensible aux bruits du signal.</li>
        </ul>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer cette notion au projet ?</h2>
        <p style="text-align: justify;"> Nous nous appuierons principalement sur les travaux de <a href="https://github.com/nicholastmosher/PID" target="_blank">Nick Mosher</a>, qui propose une approche détaillée pour l'implémentation du contrôleur PID dans un environnement de programmation. Nous examinerons comment adapter ses principes à notre robot bipède et comment optimiser son utilisation afin d'assurer une régulation précise et efficace des mouvements et de la stabilisation. </p>
        <h4><strong>Initialisation</strong></h4>
        <div class="justified-text">
        L'implémentation du PID en C++ commence par la création d'une classe représentant le contrôleur. Comme mentionné précédemment, nous avons une classe PID qui prend en charge les trois paramètres essentiels : Kp, Ki, et Kd. Ces coefficients seront ajustés en fonction des tests et des besoins de régulation.<br><br>
        Voici une version étendue de l'implémentation C++ pour mieux comprendre les processus internes et l'application du PID :</div>
        <div class="code-container">
            <div class="code-header">
                <span>PID.cpp</span>
                <button onclick="copyCode()" style="background:none;border:none;color:inherit;cursor:pointer;">📋 Copier</button>
            </div>
            <pre><code>#include &lt;iostream&gt;
#include &lt;chrono&gt;
#include &lt;functional&gt;

template &lt;class T&gt;
class PIDController {
private:
    double _p, _i, _d;
    T target, output, currentFeedback, lastFeedback, error, lastError;
    long currentTime, lastTime;
    int integralCumulation, maxCumulation;
    
public:
    PIDController(double p, double i, double d, std::function<T()> pidSource, std::function<void(T)> pidOutput)
        : _p(p), _i(i), _d(d), target(0), output(0), currentFeedback(0), lastFeedback(0), error(0), lastError(0),
          currentTime(0), lastTime(0), integralCumulation(0), maxCumulation(30000) {
        _pidSource.swap(pidSource);
        _pidOutput.swap(pidOutput);
    }

    T tick() {
        currentFeedback = _pidSource();
        
        // Calcul de l'erreur
        error = target - currentFeedback;

        // Calcul de l'intégrale et de la dérivée
        long deltaTime = currentTime - lastTime;
        int cycleIntegral = ((lastError + error) / 2) * deltaTime;
        integralCumulation += cycleIntegral;
        double cycleDerivative = (error - lastError) / deltaTime;

        // Limiter l'intégrale
        if(integralCumulation > maxCumulation) integralCumulation = maxCumulation;
        if(integralCumulation < -maxCumulation) integralCumulation = -maxCumulation;

        // Calcul du résultat PID
        output = (error * _p) + (integralCumulation * _i) + (cycleDerivative * _d);
        
        // Sauvegarder l'état actuel
        lastFeedback = currentFeedback;
        lastError = error;
        lastTime = currentTime;

        // Retourner la valeur du feedback
        _pidOutput(output);
        return currentFeedback;
    }

    void setTarget(T t) { target = t; }
    T getTarget() { return target; }
    T getOutput() { return output; }
    T getFeedback() { return currentFeedback; }
    T getError() { return error; }
};
};</code></pre>
        </div>
<h2>Dans quelle partie du code peut intervenir le PID ?</h2><br>

<div class="pid-application">
    <div class="application-card">
        <h3>Module de contrôle des moteurs</h3>
        <p>Le PID peut être appliqué aux moteurs pour réguler la vitesse et la position des membres du robot.</p>
        <p><strong>Exemple :</strong> Lorsqu'un membre doit se déplacer, le PID ajuste la puissance envoyée aux moteurs en fonction de l'écart entre la consigne et la position actuelle.</p>
        <div class="goal">
            <span class="label">Objectif :</span> Améliorer la fluidité et la précision des mouvements.
        </div>
        <div class="note">
            <em>Remarque :</em> Nos servomoteurs disposent déjà d'un PID intégré.
        </div>
    </div>
    <div class="application-card">
        <h3>Stabilisation du robot</h3>
        <p>Le PID peut ajuster l'équilibre du robot en analysant les données des capteurs inertiels (IMU) et en corrigeant la posture en temps réel.</p>
        <div class="goal">
            <span class="label">Objectif :</span> Minimiser les oscillations et éviter les chutes.
        </div>
    </div>
    <div class="application-card">
        <h3>Contrôle de la trajectoire</h3>
        <p>Lors de la marche, un PID peut corriger les déviations de trajectoire détectées par les capteurs de position.</p>
        <div class="goal">
            <span class="label">Objectif :</span> Maintenir une trajectoire stable malgré les irrégularités du sol.
        </div>
    </div>
</div>


<script>
function copyCode() {
    const code = document.querySelector('.code-container code').innerText;
    navigator.clipboard.writeText(code);
    
    // Feedback visuel
    const button = document.querySelector('.code-header button');
    const originalText = button.innerHTML;
    button.innerHTML = '✓ Copié!';

    setTimeout(() => {
        button.innerHTML = originalText;
    }, 2000);
}
</script>
