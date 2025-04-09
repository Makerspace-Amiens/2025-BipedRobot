---
layout: default
nav_exclude: true
title: TCP/IP
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

.tcpip-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
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
    position: relative;
}

.application-card {
    background: #f8f9fa;
    border-left: 4px solid var(--primary-color);
    padding: 1.2rem;
    border-radius: 0 4px 4px 0;
    margin-bottom: 1.5rem;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.application-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.application-card h3 {
    margin-top: 0;
    color: var(--primary-color);
    padding-bottom: 0.5rem;
}

.goal {
    background: #e8f0fe;
    padding: 0.8rem 1rem;
    border-radius: 4px;
}

.goal .label {
    font-weight: bold;
    color: white;
}

.note {
    font-size: 0.9em;
    color: #666;
    margin-top: 0.8rem;
    font-style: italic;
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
    transition: color 0.2s;
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
    border-radius: 8px;
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

/* Styles améliorés pour la comparaison OSI/TCP */
.layers-comparison {
    display: flex;
    justify-content: center;
    margin: 3rem 0;
    gap: 2rem;
    flex-wrap: wrap;
}

.layer-model {
    flex: 1;
    min-width: 300px;
    max-width: 480px;
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    animation: slideUp 0.6s cubic-bezier(0.22, 1, 0.36, 1) forwards;
    opacity: 0;
}

.layer-model:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.12);
}

.layer-model h3 {
    color: white;
    text-align: center;
    margin: 0;
    padding: 1.5rem;
    font-size: 1.3rem;
    font-weight: 500;
    letter-spacing: 0.5px;
}

.osi-model h3 {
    background: linear-gradient(135deg, #1565c0, #0d47a1);
}

.tcpip-model h3 {
    background: linear-gradient(135deg, #2e7d32, #1b5e20);
}

.layer-stack {
    padding: 1.5rem;
}

.layer-item {
    display: flex;
    align-items: center;
    margin: 0.8rem 0;
    padding: 1.2rem;
    border-radius: 8px;
    position: relative;
    background-color: white;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
    cursor: default;
}

.layer-item:hover {
    transform: translateX(8px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.layer-item::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 5px;
    height: 100%;
    transition: all 0.3s ease;
}

.layer-item:hover::before {
    width: 8px;
}

.layer-number {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    margin-right: 1.2rem;
    font-weight: bold;
    color: white;
    flex-shrink: 0;
    font-size: 1.1rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.layer-content {
    flex: 1;
}

.layer-title {
    font-weight: 600;
    margin-bottom: 0.3rem;
}

.protocol-badge {
    font-size: 0.85rem;
    color: #555;
    background: #f0f0f0;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    display: inline-block;
}

/* Couleurs des couches OSI */
.osi-layer-7 { background-color: #e3f2fd; }
.osi-layer-7::before, .osi-layer-7 .layer-number { background-color: #1565c0; }

.osi-layer-6 { background-color: #bbdefb; }
.osi-layer-6::before, .osi-layer-6 .layer-number { background-color: #1976d2; }

.osi-layer-5 { background-color: #90caf9; }
.osi-layer-5::before, .osi-layer-5 .layer-number { background-color: #2196f3; }

.osi-layer-4 { background-color: #64b5f6; }
.osi-layer-4::before, .osi-layer-4 .layer-number { background-color: #42a5f5; }

.osi-layer-3 { background-color: #42a5f5; }
.osi-layer-3::before, .osi-layer-3 .layer-number { background-color: #64b5f6; }

.osi-layer-2 { background-color: #2196f3; }
.osi-layer-2::before, .osi-layer-2 .layer-number { background-color: #90caf9; }

.osi-layer-1 { background-color: #1976d2; color: white; }
.osi-layer-1::before { background-color: #bbdefb; }
.osi-layer-1 .layer-number { background-color: #bbdefb; color: #1976d2; }

/* Couleurs des couches TCP/IP */
.tcpip-layer-app { background-color: #e8f5e9; }
.tcpip-layer-app::before, .tcpip-layer-app .layer-number { background-color: #2e7d32; }

.tcpip-layer-trans { background-color: #c8e6c9; }
.tcpip-layer-trans::before, .tcpip-layer-trans .layer-number { background-color: #388e3c; }

.tcpip-layer-net { background-color: #a5d6a7; }
.tcpip-layer-net::before, .tcpip-layer-net .layer-number { background-color: #43a047; }

.tcpip-layer-acc { background-color: #81c784; color: white; }
.tcpip-layer-acc::before { background-color: #4caf50; }
.tcpip-layer-acc .layer-number { background-color: #4caf50; }

/* Animation */
@keyframes slideUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

.layer-model {
    animation: slideUp 0.6s cubic-bezier(0.22, 1, 0.36, 1) forwards;
    opacity: 0;
}

.layer-model:nth-child(2) {
    animation-delay: 0.15s;
}

/* Responsive */
@media (max-width: 768px) {
    .layers-comparison {
        flex-direction: column;
        align-items: center;
    }
    
    .layer-model {
        min-width: 100%;
    }
    
    .tcpip-container {
        padding: 15px;
    }
}

/* Tooltip pour les protocoles */
.protocol-badge {
    position: relative;
    cursor: help;
}

.protocol-badge:hover::after {
    content: attr(data-tooltip);
    position: absolute;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    background: #333;
    color: white;
    padding: 0.5rem;
    border-radius: 4px;
    font-size: 0.8rem;
    white-space: nowrap;
    z-index: 10;
    margin-bottom: 5px;
}

</style>


<div class="tcpip-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce que le protocole TCP/IP ?</h2>
        <hr>
        <p class="lead justified-text">
           TCP/IP (Transmission Control Protocol/Internet Protocol) est la suite de protocoles fondamentaux qui régit le fonctionnement d'Internet et des réseaux modernes. C'est le langage universel qui permet aux différents appareils connectés de communiquer entre eux, quelle que soit leur architecture matérielle ou logicielle.
        </p>
        <p class="justified-text">
           Développé dans les années 1970 par le département américain de la Défense (DARPA), TCP/IP est devenu le standard incontournable pour les communications réseau. Contrairement au modèle OSI théorique, TCP/IP a été conçu pour résoudre des problèmes pratiques de communication entre systèmes hétérogènes.
       </p>
        <div class="did-you-know">
            <h3>Le saviez-vous ?</h3>
            <p>
                Le modèle TCP/IP est souvent comparé au modèle OSI en 7 couches, mais il n'en comporte que 4 : Application, Transport, Internet et Accès réseau. Cette simplification pragmatique est l'une des clés de son succès et de son adoption massive dans le monde entier.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Architecture TCP/IP vs OSI</h2>
        <p class="justified-text">
            La comparaison entre les modèles OSI et TCP/IP révèle des approches différentes mais complémentaires de la communication réseau. Voici une analyse détaillée des deux architectures :
        </p>        
        <div class="layers-comparison">
            <!-- Modèle OSI -->
            <div class="layer-model osi-model">
                <h3>Modèle OSI (7 couches)</h3>
                <div class="layer-stack">
                    <div class="layer-item osi-layer-7">
                        <div class="layer-number">7</div>
                        <div class="layer-content">
                            <div class="layer-title">Application</div>
                            <div class="protocol-badge" data-tooltip="Protocoles applicatifs">HTTP, FTP</div>
                        </div>
                    </div>
                    <div class="layer-item osi-layer-6">
                        <div class="layer-number">6</div>
                        <div class="layer-content">
                            <div class="layer-title">Présentation</div>
                            <div class="protocol-badge" data-tooltip="Chiffrement et formatage">SSL, TLS</div>
                        </div>
                    </div>
                    <div class="layer-item osi-layer-5">
                        <div class="layer-number">5</div>
                        <div class="layer-content">
                            <div class="layer-title">Session</div>
                            <div class="protocol-badge" data-tooltip="Gestion des sessions">NetBIOS</div>
                        </div>
                    </div>
                    <div class="layer-item osi-layer-4">
                        <div class="layer-number">4</div>
                        <div class="layer-content">
                            <div class="layer-title">Transport</div>
                            <div class="protocol-badge" data-tooltip="Transport fiable ou non">TCP, UDP</div>
                        </div>
                    </div>
                    <div class="layer-item osi-layer-3">
                        <div class="layer-number">3</div>
                        <div class="layer-content">
                            <div class="layer-title">Réseau</div>
                            <div class="protocol-badge" data-tooltip="Routage des paquets">IP</div>
                        </div>
                    </div>
                    <div class="layer-item osi-layer-2">
                        <div class="layer-number">2</div>
                        <div class="layer-content">
                            <div class="layer-title">Liaison de données</div>
                            <div class="protocol-badge" data-tooltip="Accès au média">Ethernet</div>
                        </div>
                    </div>
                    <div class="layer-item osi-layer-1">
                        <div class="layer-number">1</div>
                        <div class="layer-content">
                            <div class="layer-title">Physique</div>
                            <div class="protocol-badge" data-tooltip="Signaux physiques">Câble, Signal</div>
                        </div>
                    </div>
                </div>
            </div>            
            <!-- Modèle TCP/IP -->
            <div class="layer-model tcpip-model">
                <h3>Modèle TCP/IP (4 couches)</h3>
                <div class="layer-stack">
                    <div class="layer-item tcpip-layer-app">
                        <div class="layer-number">4</div>
                        <div class="layer-content">
                            <div class="layer-title">Application</div>
                            <div class="protocol-badge" data-tooltip="Combine OSI 5-7">HTTP, FTP, SMTP</div>
                        </div>
                    </div>
                    <div class="layer-item tcpip-layer-trans">
                        <div class="layer-number">3</div>
                        <div class="layer-content">
                            <div class="layer-title">Transport</div>
                            <div class="protocol-badge" data-tooltip="Flux de données">TCP, UDP</div>
                        </div>
                    </div>
                    <div class="layer-item tcpip-layer-net">
                        <div class="layer-number">2</div>
                        <div class="layer-content">
                            <div class="layer-title">Internet</div>
                            <div class="protocol-badge" data-tooltip="Adressage logique">IP</div>
                        </div>
                    </div>
                    <div class="layer-item tcpip-layer-acc">
                        <div class="layer-number">1</div>
                        <div class="layer-content">
                            <div class="layer-title">Accès Réseau</div>
                            <div class="protocol-badge" data-tooltip="Combine OSI 1-2">Ethernet, Wi-Fi</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>        
        <div class="note">
            <p>Note : Le modèle TCP/IP est plus ancien que le modèle OSI et a été développé pour répondre à des besoins concrets, alors que le modèle OSI est une norme théorique créée ultérieurement pour standardiser les communications.</p>
        </div>
    </section>    
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Applications dans les systèmes robotiques</h2>
        <hr>
        <p class="justified-text">
            Pour un robot bipède ou tout système embarqué complexe, TCP/IP peut être crucial dans plusieurs scénarios :
        </p>        
        <div class="application-card">
            <h3>Communication Interne Distribuée</h3>
            <p>Dans une architecture où différents microcontrôleurs gèrent des membres spécifiques :</p>
            <ul>
                <li>Échange de données entre le contrôleur principal et les sous-systèmes</li>
                <li>Synchronisation des actionneurs via Ethernet temps réel</li>
                <li>Collecte centralisée des données des capteurs</li>
            </ul>            
            <div class="goal">
                <span class="label">Objectif :</span> Minimiser la latence dans la transmission des données critiques pour l'équilibre, avec tolérance aux pertes de paquets occasionnelles.
            </div>            
        </div>
    </section>
</div>

<script>
function copyCode() {
    const codeBlock = event.target.closest('.code-container').querySelector('code');
    const code = codeBlock.innerText;
    navigator.clipboard.writeText(code);
    
    const button = event.target.closest('button');
    const originalText = button.innerHTML;
    button.innerHTML = '✓ Copié!';

    setTimeout(() => {
        button.innerHTML = originalText;
    }, 2000);
}

// Animation au scroll
document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.layer-model, .application-card').forEach(el => {
        el.style.opacity = 0;
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});
</script>