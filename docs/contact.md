---
layout: default
nav_order: 8
title: Contacts
has_children: true
---

# Contacts des Collaborateurs

<div style="text-align: center; font-size: 1.5em;">
    Venez découvrir nos profils en <strong>cliquant</strong> sur les cadres ci-dessous !
</div>

<div class="team-container">
  <div class="team-member">
    <img src="{{ site.baseurl }}/assets/img/collaborateur/houda.jpg" alt="Houda Hourie">
    <p><a href="javascript:void(0);" onclick="openModal('modal-houda')">Houda Hourie</a></p>
  </div>

  <div class="team-member">
    <img src="{{ site.baseurl }}/assets/img/collaborateur/Hubert.jpg" alt="Hubert Le Roy">
    <p><a href="javascript:void(0);" onclick="openModal('modal-hubert')">Hubert Le Roy</a></p>
  </div>

  <div class="team-member">
    <img src="{{ site.baseurl }}/assets/img/collaborateur/Clemence.jpg" alt="Clémence Leleu">
    <p><a href="javascript:void(0);" onclick="openModal('modal-clemence')">Clémence Leleu</a></p>
  </div>
</div>

<div class="modal-container">
  <div id="modal-houda" class="modal">
    <div class="modal-content">
      <span class="close" onclick="closeModal('modal-houda')">&times;</span>
      <h2>Hourie Houda</h2>
      <p style="font-size: 14px; text-align: justify;">Description ici</p>
      <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/houda-hourie-118502317/" target="_blank" rel="noopener noreferrer">Envie d'en découvir plus sur moi ?</a></p>
      <p><strong>GitHub:</strong> <a href="https://github.com/houdahourie" target="_blank" rel="noopener noreferrer">Venez découvir mes autres projets</a></p>
      <hr style="border: 1px solid #f2f2f2; margin: 5px 0;">
    </div>
  </div>
</div>

<div class="modal-container">
  <div id="modal-hubert" class="modal">
    <div class="modal-content">
      <span class="close" onclick="closeModal('modal-hubert')">&times;</span>
      <h2>Hubert Le Roy</h2>
      <p style="font-size: 14px; text-align: justify;">Description ici</p>
      <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/hubert-le-roy-743a4124a/" target="_blank" rel="noopener noreferrer">Envie d'en découvir plus sur moi ?</a></p>
      <p><strong>GitHub:</strong> <a href="https://github.com/HubertLeRoy1521" target="_blank" rel="noopener noreferrer">Venez découvir mes autres projets</a></p>
      <hr style="border: 1px solid #f2f2f2; margin: 5px 0;">
    </div>
  </div>
</div>

<div class="modal-container">
  <div id="modal-clemence" class="modal">
    <div class="modal-content">
      <span class="close" onclick="closeModal('modal-clemence')">&times;</span>
      <h2>Clémence Leleu</h2>
      <p style="font-size: 14px; text-align: justify;">En tant que responsable de la conception logicielle du projet, je souhaite me spécialiser en data science, robotique et objets connectés, dans l’objectif de développer des solutions innovantes.</p>
      <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/cl%C3%A9mence-l-558360282/" target="_blank" rel="noopener noreferrer">Envie d'en découvir plus sur moi ?</a></p>
      <p><strong>GitHub:</strong> <a href="https://github.com/celmnce" target="_blank" rel="noopener noreferrer">Venez découvir mes autres projets</a></p>
      <hr style="border: 1px solid #f2f2f2; margin: 5px 0;">
    </div>
  </div>
</div>

<style>
  .team-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 20px;
  }

  .team-member {
    background-color: rgb(247, 247, 247);
    width: 200px;
    height: 250px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .team-member:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  }

  .team-member img {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    object-fit: cover;
    object-position: center;
  }

  .team-member p a {
    margin: 15px 0 0;
    font-weight: bold;
    font-size: 16px;
    text-decoration: none;
    color: rgb(39, 39, 39);
  }

  .team-member p a:hover {
    text-decoration: underline;
  }

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
    max-width: 500px;
    width: 90%;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    position: relative;
    transform: scale(0.8);
    transition: transform 0.3s ease;
  }

  .modal.show .modal-content {
    transform: scale(1);
  }

  .close {
    font-size: 28px;
    font-weight: bold;
    position: absolute;
    top: 10px;
    right: 20px;
    color: #aaa;
  }

  .close:hover, .close:focus {
    color: black;
    cursor: pointer;
  }
</style>

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

