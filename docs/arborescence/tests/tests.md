---
layout: default
nav_order: 5
title: Tests et Validation
has_children: true
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

.header-divider {
    border: none;
    height: 3px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
    border-radius: 3px;
}

.test-cards {
    display: flex;
    gap: 2rem;
    margin: 2rem 0;
    flex-wrap: wrap;
    justify-content: center;
}

.test-card {
    flex: 1;
    min-width: 320px;
    max-width: 45%;
    background: white;
    border-radius: 8px;
    padding: 0.1rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border: 1px solid var(--border-color);
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
    text-align: center; /* Keep text-align for general card content */
}

.test-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
}

.test-card h3 {
    color: var(--primary-color);
    margin-top: 0;
    padding-bottom: 3rem; 
    border-bottom: 2px solid var(--accent-color);
    text-align: center;
    width: 100%;
    margin-bottom: 1rem; 
}

.test-card a {
    text-decoration: none;
    color: inherit;
    display: flex;
    flex-direction: column;
    justify-content: flex-start; /* Aligne le contenu au début du flex container */
    align-items: center; /* Centre les éléments horizontalement */
    height: 100%;
    width: 100%;
    padding-top: 1rem; /* Donne un peu d'espace au-dessus du titre */
}

.test-card p {
    color: var(--text-color);
    text-align: center;
    max-width: 100%;
    word-wrap: break-word;
    font-size:15px;
    margin-bottom:5rem;
    margin-top: 0; /* Important pour éviter le chevauchement si le h3 a une margin-bottom */
}
</style>

# Tests et Validation

<div class="header-divider"></div>

<p>Avant d'aboutir à notre prototype final, nous avons mené plusieurs campagnes de tests pour valider nos concepts :</p>

<div class="test-cards">
    <div class="test-card">
        <a href="{{site.baseurl}}/arborescence/tests/simulation-2d">
            <h3>Simulation 2D de la marche humaine</h3>
            <p>Modélisation théorique et simulation des mouvements avant implémentation mécanique</p>
        </a>
    </div>        
    <div class="test-card">
        <a href="{{site.baseurl}}/arborescence/tests/meca_proto">
            <h3>1er Prototype Mécanique</h3>
            <p>Validation des concepts mécaniques avec notre premier prototype physique</p>
        </a>
    </div>
</div>