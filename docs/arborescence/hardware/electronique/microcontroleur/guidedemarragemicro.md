---
layout: default
nav_exclude: true
title: Guide de Démarrage Seeeduino BLE
---

# Guide De Démarrage - XIAO BLE

<hr>

<div class="intro-box">
    Accès à la documentation technique du constructeur : <a href="https://wiki.seeedstudio.com/XIAO_BLE/" target="_blank">Fiche constructeur</a>. Les images présentes dans ce guide ont été directement reprises de la documentation du constructeur.
</div>


<style>
:root {
    --primary-color: #1c5083;
    --secondary-color: #3a7cb9;
    --accent-color: #5fa8f3;
    --light-bg: #f8fafc;
    --border-color: #e2e8f0;
    --text-color: #2d3748;
    --code-bg: #edf2f7;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 2rem 0;
}

h2 {
    margin-top: 1.8em;
    color: var(--primary-color);
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 0.4em;
    font-size: 1.4em;
}

h3 {
    color: var(--secondary-color);
    margin-top: 1.5em;
    font-size: 1.2em;
}

.intro-box {
    background-color: var(--light-bg);
    border-left: 4px solid var(--primary-color);
    padding: 1.25rem;
    border-radius: 0 8px 8px 0;
    margin: 1.5rem 0;
    line-height: 1.6;
    text-align:justify;
}

.intro-box a {
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 500;
}

.intro-box a:hover {
    text-decoration: underline;
}

.content-section {
    margin-bottom: 2rem;
    line-height: 1.6;
    color: var(--text-color);
}

code {
    background-color: var(--code-bg);
    padding: 0.2em 0.4em;
    border-radius: 4px;
    font-family: monospace;
    font-size: 0.9em;
}

.result-box {
    background-color: #f0fdf4;
    border-left: 6px solid #3355ff;
    padding: 1rem;
    margin: 1.5rem 0;
    border-radius: 0 8px 8px 0;
    color: #063b5f;
    font-size: 0.95em;
}
.result-box strong {
    color:rgb(4, 91, 120);
}

</style>

<div class="content-section">
    <h2>Environnement de Développement : Arduino</h2>
    <p>Vérifier que toutes les étapes réalisées dans <a href="{{site.baseurl}}/arborescence/software/environdev/environdev">Configuration - Environnement de Développement</a> ont correctement été suivies.</p>
</div>

<div class="content-section">
    <h2>Connexion PC/Microcontrôleur</h2>
    <ol>
        <li>Connecter le microcontrôleur au PC via un câble USB-C</li>
        <li>Vérifier que le port COM est correctement détecté dans l'IDE Arduino</li>
        <li>Sélectionner le bon port dans <code>Tools</code> > <code>Port</code></li>
    </ol>
</div>

<img src="{{site.baseurl}}/assets/img/arduino-config/port.png" alt="connexion port" style="display: block; margin: 0 auto; max-width: 75%; height: auto;">

<div class="content-section">
    <h2>Code Test</h2>
    <p>Pour vérifier le bon fonctionnement de votre carte :</p>
    <ol>
        <li>Ouvrir l'IDE Arduino</li>
        <li>Suivre le chemin <code>File</code> > <code>Examples</code> > <code>01.Basics</code> > <code>Blink</code></li>
        <li>Compiler et uploader le programme</li>
        <li>Vérifier que la LED intégrée clignote</li>
    </ol>    
    <img src="{{site.baseurl}}/assets/img/arduino-config/blink.png" alt="Exemple de code Blink" style="display: block; margin: 0 auto; max-width: 75%; height: auto;">
</div>

<div class="result-box">
        <strong>Résultat Final :</strong> Observation d'un clignotement régulier de la LED intégrée (1 seconde allumée, 1 seconde éteinte)
</div>