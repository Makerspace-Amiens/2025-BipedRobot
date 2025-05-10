---
layout: default
nav_order: 2
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
    --angle-color: #1c5083;
    --speed-color: #dd6b20;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, var(--primary-color), rgba(28, 80, 131, 0.2));
    margin: 1.5rem 0;
}

.table-container {
    overflow-x: auto;
    margin: 2rem 0;
    border-radius: 10px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    background: white;
    max-width: 100%;
}

h2, h3{
    color:var(--primary-color)
}

.tg {
    border-collapse: collapse;
    width: 100%;
    font-size: 0.9rem;
    table-layout: fixed;
}

.tg thead {
    position: sticky;
    top: 0;
}


.tg th {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    padding: 10px 8px;
    font-weight: 600;
    text-align: left;
    border: none;
}

.tg th:first-child {
    border-top-left-radius: 10px;
}

.tg th:last-child {
    border-top-right-radius: 10px;
}

.tg td {
    padding: 8px 8px;
    border-bottom: 1px solid var(--border-color);
    vertical-align: middle;
    word-wrap: break-word;
}

.tg tr:nth-child(even) {
    background-color: var(--light-bg);
}

.tg tr:hover td {
    background-color: var(--accent-color);
}

/* Style spécifique */
.tg .angle {
    color: var(--angle-color);
    font-weight: 500;
    text-align: center;
}

.tg .speed {
    color: var(--speed-color);
    font-weight: 500;
    text-align: center;


}

/* Ajustement des largeurs de colonnes */
.tg th:nth-child(1), .tg td:nth-child(1) { width: 5%; }  /* Colonne # */
.tg th:nth-child(2), .tg td:nth-child(2) { width: 20%; } /* Servomoteur */
.tg th:nth-child(3), .tg td:nth-child(3) { width: 15%; } /* Position */
.tg th:nth-child(4), .tg td:nth-child(4) { width: 12%; } /* Axe */
.tg th:nth-child(5), .tg td:nth-child(5) { width: 10%; } /* Min */
.tg th:nth-child(6), .tg td:nth-child(6) { width: 10%; } /* Max */
.tg th:nth-child(7), .tg td:nth-child(7) { width: 10%; } /* Vitesse */

/* Ajustement pour petits écrans */
@media (max-width: 768px) {
    .tg {
        font-size: 0.8rem;
    }
    .tg th, .tg td {
        padding: 6px 4px;
    }
}
</style>

# Architecture Logicielle

<hr>

## Logigramme

## Contraintes

<h3 style="text-indent: 30px;">● Paramètres des servomoteurs</h3>

<div class="table-container">
<table class="tg">
  <colgroup>
    <col>
    <col>
    <col>
    <col>
    <col>
    <col>
    <col>
  </colgroup>
  <thead>
    <tr>
      <th>#</th>
      <th>Servomoteur</th>
      <th>Position</th>
      <th>Axe</th>
      <th>Min</th>
      <th>Max</th>
      <th>Vitesse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Genou gauche</td>
      <td>Articulation</td>
      <td>Pitch</td>
      <td class="angle">0°</td>
      <td class="angle">90°</td>
      <td class="speed">60°/s</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Genou droit</td>
      <td>Articulation</td>
      <td>Pitch</td>
      <td class="angle">0°</td>
      <td class="angle">90°</td>
      <td class="speed">60°/s</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Hanche G. Pitch</td>
      <td>Bassin</td>
      <td>Av/Ar</td>
      <td class="angle">-45°</td>
      <td class="angle">+45°</td>
      <td class="speed">50°/s</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Hanche G. Roll</td>
      <td>Bassin</td>
      <td>Latéral</td>
      <td class="angle">-20°</td>
      <td class="angle">+20°</td>
      <td class="speed">40°/s</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Hanche G. Yaw</td>
      <td>Bassin</td>
      <td>Rotation</td>
      <td class="angle">-25°</td>
      <td class="angle">+25°</td>
      <td class="speed">40°/s</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Hanche D. Pitch</td>
      <td>Bassin</td>
      <td>Av/Ar</td>
      <td class="angle">-45°</td>
      <td class="angle">+45°</td>
      <td class="speed">50°/s</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Hanche D. Roll</td>
      <td>Bassin</td>
      <td>Latéral</td>
      <td class="angle">-20°</td>
      <td class="angle">+20°</td>
      <td class="speed">40°/s</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Hanche D. Yaw</td>
      <td>Bassin</td>
      <td>Rotation</td>
      <td class="angle">-25°</td>
      <td class="angle">+25°</td>
      <td class="speed">40°/s</td>
    </tr>
  </tbody>
</table>
</div>

<h3 style="text-indent: 30px;"> ● Contrôle de la tension d'almentation </h3>

<h3 style="text-indent: 30px;">● Système d'arrêt urgence </h3>

<h3 style="text-indent: 30px;"> ● Détection de collision ou surcharge mécanique </h3>
