---
layout: default
nav_order: 3
title: Architecture Logicielle
parent: Logiciel
---

<style>
:root {
    --primary-color: #1c5083;
    --secondary-color: #0d2b4e;
    --accent-color: rgba(28, 80, 131, 0.15);
    --text-color: #2d3748;
    --light-bg: #f8fafc;
    --border-color: #e2e8f0;
}

.white-square-shadow {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.34);
    margin: 50px auto;
    max-width: 80%;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
}

h2, h3 {
    color: var(--primary-color);
    margin-top: 1.5rem;
}
</style>

# Architecture Logicielle

<hr>

<div style="font-size: 1.25rem; font-weight: 300; text-align: justify;">
    Cette section présente l'architecture logicielle mise en place pour répondre aux exigences et aux contraintes du projet.
</div>

## Logigramme de fonctionnement

<div class="white-square-shadow">
    <div class="diagram">
        <img src="{{site.baseurl}}/assets/ArchitectureLogicielle.drawio.png" alt="Logigramme de l'architecture logicielle">
    </div>
</div>