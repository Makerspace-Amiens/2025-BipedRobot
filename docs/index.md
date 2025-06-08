---
layout: home
nav_order: 1
title: Accueil
---

<h1 style="color:rgb(0, 0, 0); margin-bottom: 20px;"><strong>Bienvenue dans l'Univers du Robot Bipède</strong></h1>

<div class="hero-banner" style="background-color: #1c5083; color:#ffffff; padding: 30px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <h2 style="margin-top: 0; color: #ffffff;">Explorez notre recherche en robotique</h2>
  <p style="font-size: 1.1em; margin-bottom: 0;">
    Documentation technique complète et résultats de nos travaux sur la conception d'un robot bipède autonome.
  </p>
</div>

<div style="text-align:justify;font-size: 1.25rem; font-weight: 300;">
  Les robots bipèdes représentent un défi majeur en robotique, combinant complexité mécanique et algorithmique. L'association UniMakers dispose de servomoteurs Dynamixel mais n'a jamais développé de plateforme bipède. Ce projet vise à combler cette lacune tout en créant une base évolutive pour des recherches futures.
</div>

<div class="project-overview" style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 40px; align-items: stretch;">
  <div style="flex: 1 1 300px; display: flex; flex-direction: column;">
    <h2 style="border-bottom: 2px solid #eee; padding-bottom: 10px; color: #1c5083;">Le Projet en Bref</h2>    
    <div class="card animated-entry" style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); flex-grow: 1; height: 100%; animation-delay: 0.2s;">
      <h3 style="margin-top: 0;">Objectifs et finalité</h3>
      <p style="text-align: justify; line-height: 1.6;">
        Concevoir un robot bipède fonctionnel capable de se déplacer de manière autonome dans divers environnements. 
        Ce projet vise à approfondir nos compétences en robotique tout en créant une base de connaissances ouverte 
        pour la communauté.
      </p>
    </div>
  </div>

  <div style="flex: 1 1 300px; display: flex; flex-direction: column;">
    <h2 style="border-bottom: 2px solid #eee; padding-bottom: 10px; color: #1c5083;">Public cible</h2>    
    <div class="card animated-entry" style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); flex-grow: 1; height: 100%; animation-delay: 0.4s;">
      <ul style="line-height: 1.6; padding-left: 20px; margin-bottom: 0;">
        <li>Étudiants et chercheur en robotique</li>
        <li>Communauté open-source, makers</li>
        <li>Ingénieurs en biomécanique, R&D robotique, startups tech</li>
      </ul>
    </div>
  </div>
</div>

<div style="display: flex; flex-wrap: wrap; gap: 30px; margin-top: 40px;">
  <div style="flex: 1; min-width: 300px;">
    <h2 style="color: #1c5083; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Ressources Clés</h2>
    <div class="highlight-box animated-entry" style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); animation-delay: 0.6s;">
      <h3 style="margin-top: 0;">Cahier des Charges</h3>
      <a href="assets/pdf/CAHIER_DES_CHARGES.pdf" class="pulse-on-hover" style="display: inline-block; margin-top: 10px; padding: 10px 15px; background-color: #f0f4f8; border-radius: 6px; color: #1c5083; text-decoration: none; font-weight: 500;">
        Télécharger le PDF
      </a>
      <h3 style="margin-top: 30px;">Livrables</h3>
      <ul style="line-height: 1.7; padding-left: 20px;">
        <li>Prototype fonctionnel</li>
        <li>Documentation technique</li>
        <li>Etudes des stratégies de marche </li>
        <li>Bibliothèque de contrôle</li>
      </ul>
    </div>
  </div>

  <div style="flex: 1; min-width: 300px;">
    <h2 style="color: #1c5083; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Médias du Projet</h2>
    <div style="display: flex; flex-direction: column; gap: 25px;">
      <div class="media-card animated-entry highlight-box" style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); animation-delay: 0.8s;">
        <h3 style="margin-top: 0; margin-bottom:15px;">Poster Scientifique</h3>
        <div class="poster-preview" onclick="openModal()" style="background: #f5f5f5; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 8px; overflow: hidden; cursor: pointer;">
          <img id="poster-img" src="{{ site.baseurl }}/assets/img/Poster_Robot_Bipede.jpg" alt="Poster scientifique du projet" 
               style="max-width: 100%; max-height: 100%; transition: transform 0.5s ease;">
        </div>
        <p style="text-align: center; margin-top: 10px; font-size: 0.9em;">
          <span onclick="openModal()" style="color: #1c5083; text-decoration: none; font-weight: 500; cursor: pointer;">
            Agrandir le poster
          </span>
        </p>
      </div>
      <div class="media-card animated-entry highlight-box" style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); animation-delay: 1s;">
        <h3 style="margin-top: 0; margin-bottom:15px;">Vidéo de Présentation</h3>
        <div style="background: #f5f5f5; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 8px; overflow: hidden; position: relative;">
          <video controls style="max-width: 100%; max-height: 100%; margin-top:15px; transition: transform 0.5s ease;" class="pulse-on-hover">
            <source src="{{ site.baseurl }}/assets/mp4/intro_amiens.mp4" type="video/mp4">
            Votre navigateur ne supporte pas la lecture de vidéos.
          </video>
          <div class="play-icon" style="position: absolute; width: 60px; height: 60px; background: rgba(28, 80, 131, 0.8); border-radius: 50%; display: flex; align-items: center; justify-content: center; pointer-events: none;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
              <path d="M8 5v14l11-7z"/>
            </svg>
          </div>
        </div>
        <p style="font-size: 0.9em; color: #888; text-align: center; margin-top: 10px;">Présentation, démonstration et résultats</p>
      </div>
    </div>
  </div>
</div>

<div id="posterModal" class="modal" onclick="closeModal()">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="modalImage" src="{{ site.baseurl }}/assets/img/Poster_Robot_Bipede.jpg" alt="Poster scientifique en grand">
</div>

<div class="credits-note">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#1c5083" width="30px" height="30px">
        <path d="M12 4V2.21c0-.45-.54-.67-.85-.35l-2.8 2.79c-.2.2-.2.51 0 .71l2.79 2.79c.32.31.86.09.86-.36V6c3.31 0 6 2.69 6 6 0 .79-.15 1.56-.44 2.25-.15.36-.04.77.23 1.04.51.51 1.37.33 1.64-.34.37-.91.57-1.91.57-2.95 0-4.42-3.58-8-8-8zm0 14c-3.31 0-6-2.69-6-6 0-.79.15-1.56.44-2.25.15-.36.04-.77-.23-1.04-.51-.51-1.37-.33-1.64.34C4.2 9.96 4 10.96 4 12c0 4.42 3.58 8 8 8v1.79c0 .45.54.67.85.35l2.79-2.79c.2-.2.2-.51 0-.71l-2.79-2.79c-.31-.31-.85-.09-.85.36V18z"/>
    </svg>
    <p>L’intelligence artificielle a été utilisée pour assister la rédaction de cette documentation technique.</p>
</div>



<style>
  :root {
    --primary: #1c5083;
    --secondary: #4a89dc;
    --text: #333;
    --light-gray: #f5f7fa;
  }

hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
}

  .poster-preview:hover img {
    transform: scale(1.05);
  }

  .modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(59, 53, 75, 0.33);
    animation: fadeIn 0.3s ease-out;
    overflow: hidden;
  }

  .modal-content {
    display: block;
    margin: auto;
    max-width: 90%;
    max-height: 90%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    animation: zoomIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border-radius: 4px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
  }

  .close {
    position: absolute;
    top: 25px;
    right: 35px;
    color: #f1f1f1;
    font-size: 40px;
    font-weight: bold;
    cursor: pointer;
    z-index: 1001;
  }

  .close:hover {
    color: #fff;
    opacity: 1;
    text-shadow: 0 0 5px rgba(255,255,255,0.5);
  }

  .credits-note {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin: 2rem 0;
    padding: 1rem;
    background-color: rgba(28, 80, 131, 0.05);
    border-radius: 6px;
    font-size: 16px;
    color: #555;
    border-left: 3px solid var(--primary-color);
}

.credits-note svg {
    flex-shrink: 0;
}

.credits-note p {
    margin: 0;
    line-height: 1.5;
}

@media (max-width: 768px) {
    .credits-note {
        flex-direction: column;
        align-items: flex-start;
    }
}

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  @keyframes zoomIn {
    from { transform: translate(-50%, -50%) scale(0.95); opacity: 0; }
    to { transform: translate(-50%, -50%) scale(1); opacity: 1; }
  }
</style>

<script>
  function openModal() {
    const modal = document.getElementById("posterModal");
    modal.style.display = "block";
  }

  function closeModal() {
    const modal = document.getElementById("posterModal");
    modal.style.display = "none";
  }
</script>