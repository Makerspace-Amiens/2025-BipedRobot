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

/* Styles améliorés pour les icônes */
.icons-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
    margin: 30px auto;
    max-width: 90%;
}

.icon-item {
    background-color: var(--primary-color);
    color: white;
    width: 120px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    text-align: center;
    cursor: pointer;
}

.icon-item:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    background-color: rgb(30, 33, 106);
}

.icon-item a {
    font-size: 15px;
    text-decoration: none;
    color: white;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.icon-item a:hover {
    text-decoration: underline;
}

/* Styles modaux améliorés */
.modal {
    opacity: 0;
    visibility: hidden;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(5, 25, 79, 0.53);
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: opacity 0.3s ease, visibility 0.3s ease;
  }

.modal.show {
    opacity: 1;
    visibility: visible;
}

.modal-content {
    background-color: rgba(250, 245, 245, 0.92);
    padding: 30px;
    border-radius: 8px;
    max-width: 600px;
    width: 90%;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.8);
    transition: transform 0.3s ease;
}

.modal.show .modal-content {
    transform: translate(-50%, -50%) scale(1);
}

.close {
    font-size: 28px;
    font-weight: bold;
    position: absolute;
    top: 10px;
    right: 20px;
    color: #aaa;
    cursor: pointer;
}

.close:hover, .close:focus {
    color: black;
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

<div style="text-align:justify">
    Vous retrouverez ci-dessous une explication détaillée de chaque étape du fonctionnement du robot.
</div>

<div class="icons-container">
    <div class="icon-item">
        <a href="javascript:void(0);" onclick="openModal('modal-initialisation')">Initialisation</a>
    </div>
    <div class="icon-item">
        <a href="javascript:void(0);" onclick="openModal('modal-lecture-data')">Lecture des données</a>
    </div>
    <div class="icon-item">
        <a href="javascript:void(0);" onclick="openModal('modal-verification_data')">Vérification des données</a>
    </div>
    <div class="icon-item">
        <a href="javascript:void(0);" onclick="openModal('modal-equilibre')">Gestion de l'équilibre</a>
    </div>
    <div class="icon-item">
        <a href="javascript:void(0);" onclick="openModal('modal-marche')">Cycle de Marche</a>
    </div>     
</div>

<!-- Modals -->
<div id="modal-initialisation" class="modal">
    <div class="modal-content">
        <span class="close" onclick="closeModal('modal-initialisation')">&times;</span>
        <h2>Initialisation</h2>
        <p>Contenu détaillé sur le processus d'initialisation...</p>
    </div>
</div>

<div id="modal-lecture-data" class="modal">
    <div class="modal-content">
        <span class="close" onclick="closeModal('modal-lecture-data')">&times;</span>
        <h2>Lecture des Données</h2>
        <p>Contenu détaillé sur la lecture des données...</p>
    </div>
</div>

<div id="modal-verification_data" class="modal">
    <div class="modal-content">
        <span class="close" onclick="closeModal('modal-verification_data')">&times;</span>
        <h2>Vérification des données</h2>
        <p>.....</p>
    </div>
</div>

<div id="modal-equilibre" class="modal">
    <div class="modal-content">
        <span class="close" onclick="closeModal('modal-equilibre')">&times;</span>
        <h2>Gestion de l'équilibre</h2>
        <p>Contenu d'exemple supplémentaire...</p>
    </div>
</div>

<div id="modal-marche" class="modal">
    <div class="modal-content">
        <span class="close" onclick="closeModal('modal-marche')">&times;</span>
        <h2>Cycle de Marche</h2>
        <p>Contenu détaillé sur le cycle de marche...</p>
    </div>
</div>


<script>
function openModal(modalId) {
  let modal = document.getElementById(modalId);
  modal.classList.add('show');
}

function closeModal(modalId) {
  let modal = document.getElementById(modalId);
  modal.classList.remove('show');
}

</script>