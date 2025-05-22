---
layout: default
nav_order: 8
title: Documentation
has_children: true
---

<style>
:root {
    --primary-color: #1c5083;
    --secondary-color: #3a7cb9;
    --accent-color: #5fa8f3;
    --light-bg: #f8fafc;
    --border-color: #e2e8f0;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
}

.docs-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

.doc-card {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    padding: 20px;
    margin-bottom: 30px;
}

.doc-links {
    display: grid;
    grid-template-columns: 1fr;
    gap: 15px;
}

.doc-link {
    display: flex;
    align-items: center;
    padding: 12px 15px;
    background: var(--light-bg);
    border-radius: 6px;
    transition: all 0.3s ease;
    text-decoration: none;
    color: var(--primary-color);
    border-left: 4px solid var(--accent-color);
}

.doc-link:hover {
    background: #e6f0fa;
    transform: translateX(5px);
}

.doc-link i {
    margin-right: 10px;
    color: var(--secondary-color);
}
</style>

<div class="docs-container">
    <h1>Documentation et Ressources</h1>    
    <hr>    
    <div class="doc-card">
        <p style="text-align: justify; margin-bottom: 25px;">
            Retrouvez ici tous les guides créés par notre équipe ainsi que les ressources techniques utiles pour vos projets.
        </p>        
        <div class="doc-links">
            <a href="https://www.farnell.com/datasheets/2054525.pdf" class="doc-link">
                <i></i> DataSheet Alimentation Tenma
            </a>   
            <a href="https://emanual.robotis.com/docs/en/dxl/dxl-quick-start-guide/" class="doc-link">
                <i></i> Documentation Technique Dynamixel Starter Kit
            </a>
            <a href="https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/" class="doc-link">
                <i></i> Documentation Technique Dynamixel Wizard
            </a>            
            <a href="https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/" class="doc-link">
                <i></i> Documentation Technique Servomoteurs Dynamixel AX12A
            </a>                     
            <a href="{{site.baseurl}}/arborescence/hardware/electronique/dynamixel/wizard" class="doc-link">
                <i></i> Guide d'Utilisation Dynamixel Wizard
            </a>
        </div>
    </div>
</div>