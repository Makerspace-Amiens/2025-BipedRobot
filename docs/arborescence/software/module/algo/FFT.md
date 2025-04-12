---
layout: default
nav_exclude: true
title: Transformée de Fourier
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

<div class="fourier-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce qu'une Transformée de Fourier ?</h2>
        <hr>
        <p class="lead justified-text">
            La transformée de Fourier est un outil mathématique fondamental permettant de passer d'une vision temporelle à une vision fréquentielle d'un signal. Elle permet de décomposer un signal complexe en une somme d'ondes sinusoïdales simples, facilitant ainsi l'analyse de ses composantes.
        </p>
        <p class="justified-text">
            Elle est utilisée dans de nombreux domaines : traitement du signal audio, imagerie médicale, analyse vibratoire, robotique, intelligence artificielle, etc.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                Joseph Fourier, physicien français, a introduit cette idée en 1822 dans le but d'étudier la propagation de la chaleur. Aujourd'hui, ses travaux sont essentiels dans l'ingénierie moderne.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général de la Transformée de Fourier</h2>
        <p class="justified-text">
            L'idée principale est que tout signal périodique peut être vu comme une superposition de signaux sinusoïdaux. La transformée de Fourier permet d'identifier ces composantes en déterminant leurs fréquences, amplitudes et phases.
        </p>
        <div class="math-equation">
            <p>$$F(f) = \int_{-\infty}^{+\infty} x(t) \cdot e^{-j 2\pi f t} \, dt$$</p>
        </div>
        <div class="diagram-container">
            <img src="{{ site.baseurl }}/assets/img/etude_algo/fft/FFT-algorithm.png" alt="Illustration de la Transformée de Fourier" class="img-fluid">
            <p class="text-muted">Passage du domaine temporel au domaine fréquentiel</p>
        </div>
        <p class="justified-text">
            L'équation ci-dessus représente la transformée de Fourier continue. On l'utilise lorsqu'on a un signal analogique. Pour les signaux numériques, on utilise plutôt la transformée de Fourier discrète (TFD), souvent calculée grâce à la FFT (Fast Fourier Transform).
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer cette notion au projet ?</h2>
        <p class="justified-text">
            Dans le cadre de notre robot bipède, la transformée de Fourier pourrait être utilisée pour analyser les signaux issus des capteurs (IMU, gyroscope, accéléromètre) afin de détecter des oscillations non souhaitées ou pour filtrer les bruits parasites. Cela nous permettrait d'améliorer la stabilité en temps réel via des traitements de signal.<br>
            Pour l'implémentation de la transformée de Fourier, je me suis appuyée sur les travaux disponibles en open source, notamment <a href="https://github.com/EE-Abdullah/FFT-cpp/blob/master/src/FFT.cpp" target="_blank">ce code C++ de FFT</a> développé par EE-Abdullah.
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation Transformée de Fourier</span>
        </div>
        <pre><code>template &lt;class T&gt;
#include &lt;Eigen/Dense&gt;
#include &lt;cmath&gt;
#include "../include/FFT.hpp"

int reverse(int b, int n)
{
    int k = 1;
    int A = b;
    int result = 0;
    int s = 0;
    int A_right = A;
    int A_left = A;
    while (n-k >= 0)
    {
        A_right = (int)(A >> n-k) & (int)(std::pow(2, n)-1) & (int)std::pow(2, s);
        A_left = (int)(A << n-k) & (int)(std::pow(2, n)-1) & (int)std::pow(2, n-1-s);
        result = result | A_left | A_right;
        s++;
        k += 2;
    }
    return result;
}

Eigen::VectorXcd order(Eigen::VectorXd& x_n)
{
    int N = x_n.size();
    int n_bits = std::log2(N);
    Eigen::VectorXcd x_n_ord(N);
    int new_index = 0;
    for (int i=0; i&lt;N; ++i)
    {
        new_index = reverse(i, n_bits);
        x_n_ord(i) = x_n(new_index);
    }
    return x_n_ord;
}

Eigen::VectorXcd computation(Eigen::VectorXcd&& x_seg_A, Eigen::VectorXcd&& x_seg_B, int N)
{
    int N_prev = x_seg_A.size();
    int N_next = N_prev * 2;
    int s = (int)std::log2(N_next);
    int W_length = std::pow(2, s-1);
    std::complex&lt;double&gt; W = std::polar(1.0, -2*M_PI/N);
    Eigen::VectorXcd W_K(W_length);
    int num_pairs = (int)(N/(std::pow(2, s)));
    W_K.setConstant(W);
    W_K = W_K.binaryExpr(
        Eigen::VectorXcd::LinSpaced(W_K.size(), 0, W_K.size()-1),
        [&](std::complex&lt;double&gt; w_k, std::complex&lt;double&gt; i) {
            return std::pow(w_k, num_pairs*i.real());
        }
    );
    Eigen::VectorXcd H_K = W_K.cwiseProduct(x_seg_B);
    Eigen::VectorXcd X_K(N_next);
    X_K.segment(0, W_length) = x_seg_A + H_K;
    X_K.segment(W_length, W_length) = x_seg_A - H_K;
    return X_K;
}

Eigen::VectorXcd segment(Eigen::VectorXcd& x_n_sort)
{
    int N = x_n_sort.size();
    int total_stages = (int)std::log2(N);
    Eigen::VectorXcd X_K = x_n_sort;
    int num_pairs = 0;
    int index = 0;
    int input_chunk = 0;
    int output_chunk = 0;
    for (int s=1; s&lt;=total_stages; ++s) {
        index = 0;
        input_chunk = (int)(std::pow(2, s-1));
        output_chunk = (int)(std::pow(2, s));
        num_pairs = (int)(N/(std::pow(2, s)));
        for (int i=1; i&lt;=num_pairs; ++i) {
            X_K.segment(index, output_chunk) =
                computation(
                    X_K.segment(index, input_chunk),
                    X_K.segment(index+input_chunk, input_chunk),
                    N
                );
            index = index + output_chunk;
        }
    }
    return X_K;
}

Eigen::VectorXcd FFT(Eigen::VectorXd& x_n)
{
    int N = x_n.size();
    Eigen::VectorXcd x_n_ord = order(x_n);
    Eigen::VectorXcd X_K = segment(x_n_ord);
    return X_K;
}</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir la Transformée de Fourier ?</h2>
    <div class="pid-application">
        <div class="application-card">
            <h3>Acquisition des données</h3>
            <p>La FFT peut être utilisée pour analyser les données des capteurs inertiels et détecter des vibrations ou oscillations indésirables.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;"> Lors de l'acquisition des données, le capteur IMU envoie des mesures d'accélération et de vitesse angulaire sur plusieurs axes (X, Y, Z). Ces signaux sont ensuite échantillonnés à des intervalles réguliers. En appliquant la FFT sur les données temporelles, on obtient un spectre de fréquence qui nous permet d'identifier les pics de fréquence. Par exemple, si un pic se trouve à une fréquence de 50 Hz, cela peut indiquer une vibration indésirable provenant d’un moteur ou d'un autre composant du robot.Une fois identifiées, ces fréquences peuvent être filtrées ou atténuées à l’aide de filtres passe-bas ou passe-bande pour minimiser leur impact sur les performances du robot.</p>
            <div class="goal">
                <span class="label">Objectif :</span> Améliorer la stabilité et réduire les vibrations parasites.
            </div>
        </div>        
    </div>
</div>
<h3>Références</h3>
<ul>
  <li>Fourier, J. (1822). <cite>Théorie analytique de la chaleur</cite>. Firmin Didot.</li>
  <li>Cooley, J. W., & Tukey, J. W. (1965). <cite>An algorithm for the machine calculation of complex Fourier series</cite>. Mathematics of Computation.</li>
  <li>Abdullah, E. E. (2020). <cite>FFT Implementation in C++</cite>. GitHub repository.</li>
  <li>Smith, S. W. (1997). <cite>The Scientist and Engineer's Guide to Digital Signal Processing</cite>. California Technical Publishing.</li>
</ul>