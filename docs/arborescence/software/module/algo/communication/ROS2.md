---
layout: default
nav_exclude: true
title: ROS2 - Robot Operating System 2
---

<!-- ROS2 TEMPLATE POUR LES NOTIONS IMPORTANTES -->

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
        <h2>Qu'est-ce que ROS2 ?</h2>
        <hr>
        <p class="lead justified-text">
            ROS2 (Robot Operating System 2) est un framework middleware open-source de qualité industrielle pour le développement de systèmes robotiques distribués. Son architecture décentralisée permet une communication temps réel entre composants hétérogènes via des mécanismes de publication/abonnement.
        </p>
        <p class="justified-text">
            Contrairement à ROS1, ROS2 intègre nativement :
            <ul>
                <li>Un protocole DDS (Data Distribution Service) pour les communications inter-processus</li>
                <li>La gestion de la qualité de service (QoS) pour les applications critiques</li>
                <li>Un support multiplateforme étendu (Linux, Windows, RTOS, microcontrôleurs)</li>
                <li>Une sécurité renforcée avec TLS/DTLS et contrôle d'accès</li>
            </ul>
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                La NASA utilise ROS2 pour ses robots spatiaux, et il équipe des voitures autonomes chez Toyota et BMW. Sa capacité à gérer des systèmes complexes le rend indispensable pour la robotique moderne.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Architecture Technique de ROS2</h2>
        <p class="justified-text">
            ROS2 implémente une architecture basée sur 4 couches clés :
        </p>
        <ol>
            <li><strong>Middleware DDS</strong> : Gère la découverte des nœuds et le transport des données</li>
            <li><strong>Client Library (rcl)</strong> : Interface unifiée pour C++, Python, etc.</li>
            <li><strong>Nœuds</strong> : Unités fonctionnelles autonomes</li>
            <li><strong>Espace de noms</strong> : Isolation des composants</li>
        </ol>        
        <div class="math-equation">
            <p>$$\text{Appli Robotique} \xrightarrow{\text{RCL}} \text{DDS} \xrightarrow{\text{Protocoles}} \text{Réseau}$$</p>
        </div>        
        <p class="justified-text">
            Les 3 mécanismes de communication principaux :
            <ul>
                <li><strong>Topics</strong> : Flux de données asynchrones (best-effort)</li>
                <li><strong>Services</strong> : Appels RPC synchrones</li>
                <li><strong>Actions</strong> : Pattern client-serveur avec feedback</li>
            </ul>
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Intégration ROS2 dans un Robot Bipède</h2>
        <p class="justified-text">
            Pour un robot bipède, ROS2 permet une architecture modulaire avec :
        </p>        
        <div class="application-card">
            <h3>Gestion des Contraintes Temps-Réel</h3>
            <p>Configuration QoS pour :</p>
            <ul>
                <li>Deadlines critiques (commande moteur)</li>
                <li>Livraison garantie des messages</li>
                <li>Priorité des flux de données</li>
            </ul>
        </div>        
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Structure Optimisée d'un Nœud Temps-Réel</span>
        </div>
        <pre><code># Configuration QoS pour la commande moteur
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSDurabilityPolicy

qos_profile = QoSProfile(
    depth=10,
    reliability=QoSReliabilityPolicy.RELIABLE,  # Livraison garantie
    durability=QoSDurabilityPolicy.TRANSIENT_LOCAL  # Persistence des messages
)

class MotorController(Node):
    def __init__(self):
        super().__init__('biped_motor_ctl')
        # Publisher avec QoS configuré
        self.publisher_ = self.create_publisher(
            JointState, 
            'motor_commands',
            qos_profile=qos_profile
        )
        # Timer haute précision
        self.timer = self.create_timer(0.01, self.control_loop)  # 100Hz
        
    def control_loop(self):
        msg = JointState()
        # ... calcul des positions articulaires
        self.publisher_.publish(msg)</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir ROS2 ?</h2>
<div class="pid-application">
    <div class="application-card">
        <h3>Fusion capteurs</h3>
        <p style="text-align:justify;">La fusion de capteurs consiste à combiner les données de plusieurs capteurs (comme des IMU, des encodeurs, des caméras, etc.) pour obtenir une information plus précise et complète.</p>
        <p style="text-align:justify;">Dans ROS2, cela permet de créer une estimation d'état (position, vitesse, orientation) en temps réel, en corrigeant les défauts de chaque capteur (ex : un IMU seul dérive avec le temps, mais couplé à un encodeur ou une caméra, on améliore la précision).</p>
        <p style="text-align: justify;"><strong>Exemple pratique :</strong>
        Un robot utilise ses capteurs (IMU, encodeurs, caméra) pour corriger en temps réel sa position. ROS2 fusionne leurs données à 500Hz, évitant les erreurs et améliorant la précision.</p>            
                    <div class="goal">
            <span class="label">Objectif :</span> Fournir une estimation précise de la cinématique globale à 500Hz
        </div>        
    </div>
</div>

    <h3>Références Techniques Avancées</h3>
    <ul>
      <li>ROS2 Real-Time Programming <cite>https://design.ros2.org/articles/realtime_background.html</cite></li>
      <li>ROS2 Performance Analysis <cite>https://arxiv.org/abs/2101.05404</cite></li>
      <li>ROS-Industrial Standards <cite>https://rosindustrial.org/</cite></li>
      <li>ROS2 Security Working Group <cite>https://github.com/ros2/sros2</cite></li>
    </ul>
</div>