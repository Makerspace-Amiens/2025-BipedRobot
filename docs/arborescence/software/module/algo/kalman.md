---
layout: default
nav_exclude: true
title: Filtrage de Kalman
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
        <h2>Qu'est-ce qu'un filtre de Kalman ?</h2>
        <hr>
        <p class="lead justified-text">
           Un filtre de Kalman est un algorithme de traitement du signal qui permet d'estimer l'état d'un système à partir des données mesurées.
        </p>
        <p class="justified-text">
           Développé par Rudolf Kalman en 1960, ce filtre optimal combine une série de mesures imprécises pour produire une estimation plus précise de l'état du système. Il est largement utilisé en navigation, robotique, traitement d'images et bien d'autres domaines.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Le filtre de Kalman a été utilisé dans le programme Apollo de la NASA pour guider les vaisseaux spatiaux vers la Lune !
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général du Filtre de Kalman</h2>
        <p class="justified-text">
            Le filtre de Kalman fonctionne en deux étapes principales : prédiction et mise à jour. Il maintient une estimation de l'état du système et de son incertitude (matrice de covariance)
        </p>
        <div class="math-equation">
            <p>$$\begin{cases} \text{Prédiction:} & \hat{x}_k^- = F_k\hat{x}_{k-1} + B_ku_k \\ & P_k^- = F_kP_{k-1}F_k^T + Q_k \\ \\ \text{Mise à jour:} & K_k = P_k^-H_k^T(H_kP_k^-H_k^T + R_k)^{-1} \\ & \hat{x}_k = \hat{x}_k^- + K_k(z_k - H_k\hat{x}_k^-) \\ & P_k = (I - K_kH_k)P_k^- \end{cases}$$</p>
        </div>
        <p class="justified-text">
            Où:
            <ul>
                <li>\( \hat{x} \): estimation de l'état</li>
                <li>\( P \): matrice de covariance d'erreur</li>
                <li>\( F \): matrice de transition d'état</li>
                <li>\( Q \): covariance du bruit de processus</li>
                <li>\( R \): covariance du bruit de mesure</li>
                <li>\( K \): gain de Kalman</li>
                <li>\( z \): mesure observée</li>
            </ul>
        </p>
        <div class="diagram-container">
            <img src="{{ site.baseurl }}/assets/img/etude_algo/kalman/Basic_concept_of_Kalman_filtering.svg.png" alt="Illustration du Filtre de Kalman" class="img-fluid">
            <p class="text-muted">Concept de base du filtre de Kalman <a href="https://fr.wikipedia.org/wiki/Filtre_de_Kalman">[Wikipédia]</a></p>
        </div>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer cette notion au projet ?</h2>
        <p>Nous nous appuierons principalement sur les travaux de <a href="https://github.com/hmartiro/kalman-cpp" target="_blank">hmartiro</a>, qui propose une implémentation détaillée de l'algorithme de Kalman en C++. Nous examinerons comment adapter ses principes à notre robot bipède.</p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation Filtrage de Kalman</span>
            <button onclick="copyCode()">📋 Copier</button>
        </div>
        <pre><code>
/**
* Implementation of KalmanFilter class.
*
* @author: Hayk Martirosyan
* @date: 2014.11.15
*/

#include  &lt;iostream&gt;
#include  &lt;stdexcept&gt;
#include "kalman.hpp"

KalmanFilter::KalmanFilter(
    double dt,
    const Eigen::MatrixXd& A,
    const Eigen::MatrixXd& C,
    const Eigen::MatrixXd& Q,
    const Eigen::MatrixXd& R,
    const Eigen::MatrixXd& P)
  : A(A), C(C), Q(Q), R(R), P0(P),
    m(C.rows()), n(A.rows()), dt(dt), initialized(false),
    I(n, n), x_hat(n), x_hat_new(n)
{
  I.setIdentity();
}

KalmanFilter::KalmanFilter() {}

void KalmanFilter::init(double t0, const Eigen::VectorXd& x0) {
  x_hat = x0;
  P = P0;
  this->t0 = t0;
  t = t0;
  initialized = true;
}

void KalmanFilter::init() {
  x_hat.setZero();
  P = P0;
  t0 = 0;
  t = t0;
  initialized = true;
}

void KalmanFilter::update(const Eigen::VectorXd& y) {

  if(!initialized)
    throw std::runtime_error("Filter is not initialized!");

  x_hat_new = A * x_hat;
  P = A*P*A.transpose() + Q;
  K = P*C.transpose()*(C*P*C.transpose() + R).inverse();
  x_hat_new += K * (y - C*x_hat_new);
  P = (I - K*C)*P;
  x_hat = x_hat_new;

  t += dt;
}

void KalmanFilter::update(const Eigen::VectorXd& y, double dt, const Eigen::MatrixXd A) {

  this->A = A;
  this->dt = dt;
  update(y);
}
        </code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir le Filtre de Kalman ?</h2>
    <div class="pid-application">
        <div class="application-card">
            <h3>Stabilisation</h3>
                <p>Le filtre de Kalman peut être utilisé pour estimer l'angle d'inclinaison et la vitesse angulaire du robot à partir des données bruyante de l'IMU (gyroscope+accéléromètre).</p>
                <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">En fusionnant les mesures à court terme précises du gyroscope avec les mesures à long terme stables de l'accéléromètre, on obtient une estimation plus précise de l'orientation.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Maintenir l'équilibre du robot en fournissant une estimation lissée de son inclinaison
            </div>
        </div>
        <div class="application-card">
             <h3>Acquisition des données</h3>
                <p>Filtrage des mesures des capteurs (codeurs moteurs, FSR, IMU) pour réduire le bruit de mesure et améliorer la qualité des données.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Lors de la marche, les capteurs de force (FSR) subissent des perturbations. Le filtre permet d'estimer la vraie force appliquée.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Obtenir des mesures propres et exploitables malgré le bruit inhérent aux capteurs
            </div>
        </div>
        <div class="application-card">
            <h3>Surveillance du Système</h3>
            <p>Estimation de l'état interne du robot (position, vitesse, accélération) à partir de mesures partielles et incomplètes.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Reconstruction de la trajectoire complète du centre de masse à partir de mesures intermittentes.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Fournir une vue complète de l'état du système pour les algorithmes de contrôle
            </div>
        </div>
        <div class="application-card">
            <h3>Synchronisation Capteurs et Moteur</h3>
            <p></p>Compensation des délais entre les mesures des capteurs et l'action des moteurs par prédiction de l'état futur.
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">Prédire la position future des jambes pour anticiper les commandes moteurs et réduire la latence.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Améliorer la réactivité du système en compensant les retards de mesure.
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