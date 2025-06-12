---
layout: default
nav_order: 6
title: Résultats et Performances
has_children: true
---


<style>
:root {
    --primary: #1c5083;
    --primary-light: rgba(28, 80, 131, 0.15);
    --secondary: #0d2b4e;
    --accent: #4a90e2;
    --text: #2d3748;
    --light: #f8fafc;
    --border: #e2e8f0;
    --success: #38a169;
}

.page-header {
    text-align: center;
    margin-bottom: 2rem;
}

.video-highlight {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 3rem 0;
}

.vertical-video-container {
    width: 60%;
    max-width: 360px;
    aspect-ratio: 9 / 16;
    margin: 0 auto;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    background: black;
    position: relative;
}

.vertical-video-container video {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.result-badge {
    background: var(--primary);
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 50px;
    font-weight: 600;
    margin: 1.5rem 0;
    display: inline-block;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.feature-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border: 1px solid var(--border);
}

.feature-card h3 {
    color: var(--primary);
    margin-top: 0;
}

@media (max-width: 768px) {
    .vertical-video-container {
        width: 80%;
    }
}
</style>

<div class="page-header">
    <h1>Résultats et Performances</h1>
    <p class="lead">Démonstration des capacités actuelles de Roby</p>
</div>

<div class="video-highlight">
    <div class="result-badge">Démonstration Vidéo</div>    
    <div class="vertical-video-container">
        <video controls playsinline autoplay muted loop>
            <source src="{{site.baseurl}}/assets/mp4/resultatroby.mp4" type="video/mp4">
            Votre navigateur ne supporte pas la lecture de vidéos.
        </video>
    </div>
    <p><strong>Roby exécute une séquence de danse en maintenant parfaitement son équilibre</strong></p>
</div>

<div class="feature-grid">
    <div class="feature-card">
        <h3>Stabilisation</h3>
        <p>Maintien actif de l'équilibre pendant les mouvements grâce à notre algorithme de contrôle</p>
    </div>    
    <div class="feature-card">
        <h3>Coordination</h3>
        <p>Enchaînement fluide de 2 pas de danse avec synchronisation des articulations</p>
    </div>    
    <div class="feature-card">
        <h3>Robustesse</h3>
        <p>Structure mécanique résistante aux vibrations et perturbations</p>
    </div>
    <div class="feature-card">
        <h3>Prochaines Étapes</h3>
        <ul>
            <li>Développement de la marche complète</li>
            <li>Amélioration de la stabilité dynamique</li>
        </ul>
    </div>
</div>

