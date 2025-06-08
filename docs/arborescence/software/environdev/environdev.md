---
layout: default
nav_order: 1
title: Environnement
parent: Logiciel
---

<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">

<div class="content-wrapper">
    <div class="hero-banner">
        <div class="hero-content">
            <h1>Configuration Arduino</h1>
            <p class="hero-subtitle">Guide complet pour configurer votre environnement de développement</p>
            <div class="badge-container">
                <span class="badge">VS Code</span>
                <span class="badge">Python</span>
                <span class="badge">Dynamixel</span>
            </div>
        </div>
    </div>
    <div class="intro-card">
        <div class="intro-text">
            <h2>Bien démarrer</h2>
            <p>Ce guide détaillé vous accompagne pas à pas dans la configuration de l'environnement de développement VS Code afin de pouvoir envoyer un code à la carte U2D2 du Robot Bipède. Suivez attentivement les étapes décrites ci-dessous pour préparer votre système.</p>
        </div>
    </div>
    <div class="step-container">
        <div class="step-header">
            <div class="step-number">1</div>
            <h2>Installation de l'IDE VS Code</h2>
        </div>
        <div class="step-content">
            <div class="logo-container">
                <img src="{{site.baseurl}}/assets/img/logos/vscode.png" alt="VS Code Logo">
            </div>
            <div class="step-text">
                <p>Visual Studio Code (VS Code) est un éditeur de code source gratuit, léger et multiplateforme, très utilisé pour le développement embarqué, y compris avec les cartes Arduino, ESP32 et autres microcontrôleurs.</p>
                <p>Si ce n'est pas déjà fait, téléchargez et installez la dernière version de VS Code depuis le site officiel :</p>
                <div class="button-container">
                    <a href="https://code.visualstudio.com/" class="download-button" target="_blank">
                        <span>Télécharger VS Code</span>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                            <polyline points="7 10 12 15 17 10"></polyline>
                            <line x1="12" y1="15" x2="12" y2="3"></line>
                        </svg>
                    </a>
                </div>
                <p>Suivez les instructions d'installation correspondant à votre système d'exploitation (Windows, macOS ou Linux).</p>
            </div>
        </div>
    </div>

    <div class="step-container">
        <div class="step-header">
            <div class="step-number">2</div>
            <h2>Installer Python</h2>
        </div>
        <div class="step-content">
            <div class="step-text">
                <p>Pour exécuter des scripts Python dans VS Code, vous devez installer Python et configurer correctement l'environnement. Voici les étapes à suivre :</p>
                
                <div class="instruction-card">
                    <div class="instruction-number">1</div>
                    <div class="instruction-text">
                        <p>Téléchargez et installez la dernière version de Python depuis le site officiel :</p>
                        <div class="button-container">
                            <a href="https://www.python.org/downloads/" class="secondary-button" target="_blank">
                                <span>Télécharger Python</span>
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                                    <polyline points="7 10 12 15 17 10"></polyline>
                                    <line x1="12" y1="15" x2="12" y2="3"></line>
                                </svg>
                            </a>
                        </div>
                        <p class="note">Lors de l'installation, assurez-vous de cocher la case <strong>"Add Python to PATH"</strong> avant de cliquer sur <em>"Install Now"</em>.</p>
                    </div>
                </div>

                <div class="instruction-card">
                    <div class="instruction-number">2</div>
                    <div class="instruction-text">
                        <p>Une fois Python installé, ouvrez <strong>VS Code</strong> et installez l'extension Python :</p>
                        <ol class="compact-list">
                            <li>Ouvrez le menu des extensions (<code>Ctrl+Shift+X</code>)</li>
                            <li>Recherchez "Python" (éditée par Microsoft)</li>
                            <li>Cliquez sur <strong>"Installer"</strong></li>
                        </ol>
                    </div>
                </div>

                <div class="instruction-card">
                    <div class="instruction-number">3</div>
                    <div class="instruction-text">
                        <p>Configurez l'interpréteur Python :</p>
                        <ol class="compact-list">
                            <li>Créez un nouveau fichier <code>.py</code> (ex: <code>test.py</code>)</li>
                            <li>Ouvrez la palette de commandes (<code>Ctrl+Shift+P</code>)</li>
                            <li>Tapez <em>"Python: Select Interpreter"</em></li>
                            <li>Choisissez la version de Python installée</li>
                        </ol>
                    </div>
                </div>

                <div class="test-instruction">
                    <p>Testez votre configuration avec ce code simple :</p>
                    <div class="code-block">
                        <button class="copy-button" onclick="copyCode('code1')">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                            </svg>
                            Copier
                        </button>
                        <pre><code id="code1">print("Hello, world!")</code></pre>
                    </div>
                    <p class="note">Exécutez avec <code>Ctrl+F5</code> ou en cliquant sur le bouton ▶ "Run" en haut à droite.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="step-container">
        <div class="step-header">
            <div class="step-number">3</div>
            <h2>Installation des Librairies</h2>
        </div>
        <div class="step-content">
            <div class="step-text">
                <p>Pour contrôler les moteurs Dynamixel dans votre projet de robot bipède, installez les bibliothèques nécessaires puis importez-les dans votre code :</p>
                
                <div class="code-block">
                    <button class="copy-button" onclick="copyCode('code2')">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                        </svg>
                        Copier
                    </button>
                    <pre><code id="code2">from dynamixel_sdk import *  # Bibliothèque pour communiquer avec les moteurs Dynamixel
import time                  # Pour gérer les temporisations
import sys                   # Pour interagir avec le système
import keyboard              # Pour détecter les appuis clavier</code></pre>
                </div>
                
                <div class="info-card">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#1c5083" width="24px" height="24px">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/>
                    </svg>
                    <p>Assurez-vous d'avoir installé toutes les dépendances nécessaires avec <code>pip install dynamixel-sdk keyboard</code> avant d'exécuter votre script.</p>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
:root {
    --primary-color: #1c5083;
    --primary-light: #e6f0fa;
    --secondary-color: #143c64;
    --accent-color: #4a90e2;
    --text-color: #333;
    --light-bg: #f8f9fa;
    --border-color: #e1e4e8;
    --success-color: #28a745;
    --info-color: #17a2b8;
    --warning-color: #ffc107;
    --danger-color: #dc3545;
}

body {
    font-family: 'Roboto', sans-serif;
    color: var(--text-color);
    line-height: 1.6;
    background-color: #fff;
}

h1, h2, h3, h4 {
    font-weight: 600;
    color: var(--primary-color);
}

h2 {
    font-size: 1.75rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

pre, code {
    font-family: 'Fira Code', monospace;
    font-size: 0.9rem;
}

.content-wrapper {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.hero-banner {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    padding: 3rem 2rem;
    border-radius: 8px;
    margin: 2rem 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.hero-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

.hero-content h1 {
    color: white;
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

.hero-subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
    margin-bottom: 1.5rem;
}

.badge-container {
    display: flex;
    justify-content: center;
    gap: 0.8rem;
    flex-wrap: wrap;
}

.badge {
    background-color: rgba(255,255,255,0.15);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 500;
}

.intro-card {
    display: flex;
    align-items: flex-start;
    gap: 1.5rem;
    background-color: var(--light-bg);
    padding: 1.5rem;
    border-radius: 8px;
    margin: 2rem 0;
    border-left: 4px solid var(--primary-color);
}

.intro-icon {
    flex-shrink: 0;
}

.intro-text h2 {
    margin-top: 0;
    text-align:justify;
    font-size: 1.5rem;
}

.step-container {
    margin: 3rem 0;
}

.step-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.step-number {
    background-color: var(--primary-color);
    color: white;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    flex-shrink: 0;
}

.step-content {
    background-color: white;
    border-radius: 8px;
    padding: 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    border: 1px solid var(--border-color);
}

.logo-container {
    text-align: center;
    margin: 1rem 0;
}

.logo-container img {
    max-width: 150px;
    height: auto;
    margin: 1rem 0;
}

.button-container {
    margin: 1.5rem 0;
}

.download-button, .secondary-button {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    border-radius: 6px;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.2s ease;
}

.download-button {
    background-color: var(--primary-color);
    color: white;
    border: 1px solid var(--primary-color);
}

.download-button:hover {
    background-color: var(--secondary-color);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.secondary-button {
    background-color: white;
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
}

.secondary-button:hover {
    background-color: var(--primary-light);
}

.instruction-card {
    display: flex;
    gap: 1rem;
    margin: 1.5rem 0;
    padding: 1.25rem;
    background-color: var(--light-bg);
    border-radius: 6px;
    border-left: 3px solid var(--primary-color);
}

.instruction-number {
    background-color: var(--primary-color);
    color: white;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    flex-shrink: 0;
    font-size: 0.9rem;
}

.instruction-text {
    flex-grow: 1;
}

.compact-list {
    padding-left: 1.25rem;
    margin: 0.5rem 0;
}

.compact-list li {
    margin-bottom: 0.5rem;
}

.note {
    font-size: 0.9rem;
    color: #666;
    font-style: italic;
    margin-top: 0.5rem;
}

.test-instruction {
    margin: 2rem 0;
}

.code-block {
    position: relative;
    background-color: #f5f7fa;
    border-radius: 6px;
    padding: 1rem;
    margin: 1rem 0;
    border: 1px solid var(--border-color);
    overflow: hidden;
}

.code-block pre {
    margin: 0;
    overflow-x: auto;
}

.code-block code {
    color: #2d3748;
    line-height: 1.5;
}

.copy-button {
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    padding: 0.25rem 0.75rem;
    background-color: white;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    font-size: 0.8rem;
    cursor: pointer;
    transition: all 0.2s ease;
}

.copy-button:hover {
    background-color: var(--primary-light);
    border-color: var(--primary-color);
}

.copy-button svg {
    width: 14px;
    height: 14px;
}

.info-card {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    background-color: var(--primary-light);
    padding: 1rem;
    border-radius: 6px;
    margin: 1.5rem 0;
}

.info-card svg {
    flex-shrink: 0;
    margin-top: 0.15rem;
}

.info-card p {
    margin: 0;
}

@media (max-width: 768px) {
    .hero-content h1 {
        font-size: 2rem;
    }
    
    .intro-card {
        flex-direction: column;
    }
    
    .instruction-card {
        flex-direction: column;
    }
    
    .step-header {
        flex-direction: column;
        align-items: flex-start;
    }
}
</style>

<script>
function copyCode(elementId) {
    const element = document.getElementById(elementId);
    const text = element.textContent;
    navigator.clipboard.writeText(text.trim()).then(() => {
        // Show feedback
        const button = element.parentElement.querySelector('.copy-button');
        button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Copié!';
        setTimeout(() => {
            button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copier';
        }, 2000);
    });
}
</script>