---
layout: default
nav_exclude: true
title: Filtrage de Kalman
---
<!-- TEMPLATE POUR LES NOTIONS IMPORTANTES ALGO BASE SUR LE FILTRAGE DE KALMAN, PENSER A MODIFIER AVEC LA NOTION VOULUE-->

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
           mettre texte
        </p>
        <p class="justified-text">
           mettre texte
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                mettre texte
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général du Filtre de Kalman</h2>
        <p class="justified-text">
            mettre texte
        </p>
        <div class="math-equation">
            <p>$$mettre texte$$</p>
        </div>
        <div class="diagram-container">
            <img src="{{ site.baseurl }}/assets/img/etude_algo/fft/FFT-algorithm.png" alt="Illustration de la Transformée de Fourier" class="img-fluid">
            <p class="text-muted">mettre texte</p>
        </div>
        <p class="justified-text">
            mettre texte
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer cette notion au projet ?</h2>
        <p class="justified-text">
            mettre texte
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation Filtrage de Kalman</span>
        </div>
        <pre><code>template &lt;class T&gt;
        </code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir le Filtre de Kalman ?</h2>
    <div class="pid-application">
        <div class="application-card">
            <h3>mettre module</h3>
            <p>mettre texte</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">texte</p>
            <div class="goal">
                <span class="label">Objectif :</span> mettre texte
        </div>        
    </div>
</div>

<h3>Références</h3> <!--Style APA-->
<ul>
  <li>mettre texte<cite>mettre texte</cite>mettre texte</li>
  <li>mettre texte<cite>mettre texte</cite>mettre texte</li>
  <li>mettre texte <cite>mettre texte</cite> mettre texte</li>
  <li>mettre texte<cite>mettre texte</cite> mettre texte</li>
</ul>
