---
layout: default
nav_exclude: true
title: Servomoteurs AX12
---

# Fiche Technique - Servomoteur AX12

<hr>

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

.intro {
    margin-bottom: 2.5em;
    line-height: 1.7;
    color: #4a5568;
    font-size: 1.05em;
}

.spec-table, .comm-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 1.5em 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    border-radius: 8px;
    overflow: hidden;
}

.spec-table th, .spec-table td,
.comm-table th, .comm-table td {
    padding: 12px 15px;
    text-align: left;
    border-right: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
}

.spec-table th {
    background-color: var(--primary-color);
    color: white;
    font-weight: 500;
    text-transform: uppercase;
    font-size: 0.85em;
    letter-spacing: 0.5px;
}

.comm-table th {
    background-color: var(--primary-color);
    color: white;
    font-weight: 500;
    width: 25%;
}

.spec-table tr:nth-child(even),
.comm-table tr:nth-child(even) {
    background-color: var(--light-bg);
}

.spec-table tr:hover,
.comm-table tr:hover {
    background-color: #f0f7ff;
}

.spec-table td:first-child {
    font-weight: 500;
    color: var(--primary-color);
}

h2 {
    margin-top: 1.8em;
    color: var(--primary-color);
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 0.4em;
    font-size: 1.4em;
}

</style>

<div class="intro">
<p style="text-align:justify;">Les servomoteurs AX12 et AX12+ sont des actionneurs intelligents fabriqués par ROBOTIS, conçus pour des applications robotiques exigeantes. Contrairement aux servomoteurs classiques, ils intègrent une communication série TTL et des capteurs embarqués, permettant un contrôle précis de la position, vitesse et couple.</p>

<p style="text-align:justify;">Utilisés dans des domaines variés (robotique humanoïde, bras articulés, systèmes automatisés), les AX12 se distinguent par leur robustesse mécanique (engrenages en métal) et leur capacité à être connectés en réseau via un bus Dynamixel, simplifiant le contrôle de plusieurs moteurs simultanément.</p>
</div>

## Caractéristiques Techniques 

<div class="notice" style="background:rgb(235, 237, 243);; padding: 1em; border-left: 4px solid #1c5083;">
    Les informations ci-dessous peuvent être retrouvées directement sur le site du constructeur<br>
    <a href="https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/" target="_blank">Cliquez ici pour y accéder</a>.
</div>

<table class="spec-table">
    <thead>
        <tr>
            <th>Paramètre</th>
            <th>AX12</th>
            <th>AX12+</th>
            <th>Unité</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Couple maximal</td>
            <td>16.5</td>
            <td>16.5</td>
            <td>kg·cm (à 12V)</td>
        </tr>
        <tr>
            <td>Vitesse de rotation</td>
            <td>0.17</td>
            <td>0.15</td>
            <td>sec/60° (à 12V)</td>
        </tr>
        <tr>
            <td>Angle de rotation</td>
            <td colspan="2">0° à 300°</td>
            <td>degrés</td>
        </tr>
        <tr>
            <td>Tension d'alimentation</td>
            <td colspan="2">9.0 ~ 12.0</td>
            <td>V (recommandé 11.1V)</td>
        </tr>
        <tr>
            <td>Consommation électrique</td>
            <td colspan="2">1.5 (veille), ~5 (en charge)</td>
            <td>W</td>
        </tr>
        <tr>
            <td>Température opérationnelle</td>
            <td colspan="2">-5°C à +70°C</td>
            <td></td>
        </tr>
    </tbody>
</table>

## Communication et Contrôle 

<table class="comm-table">
    <tr>
        <th>Protocole</th>
        <td>Half-Duplex Asynchronous Serial Communication (TTL Level)</td>
    </tr>
    <tr>
        <th>Vitesse de transmission</th>
        <td>7343 bps à 1 Mbps (configurable par logiciel)</td>
    </tr>
    <tr>
        <th>Connectivité réseau</th>
        <td>Bus Dynamixel (jusqu'à 254 appareils connectés en série avec adresses uniques)</td>
    </tr>
    <tr>
        <th>Paramètres contrôlables</th>
        <td>
            <ul style="margin:0;padding-left:20px;columns:2;">
                <li>Position angulaire</li>
                <li>Vitesse de rotation</li>
                <li>Couple maximum</li>
                <li>Température interne</li>
                <li>Tension d'alimentation</li>
                <li>LED de diagnostic</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Feedback</th>
        <td>Retour d'information en temps réel sur la position, température, charge et tension</td>
    </tr>
</table>

## Vérification du Matériel : Dynamixel Wizard 2.0

<div class="notice" style="background: rgb(235, 237, 243); padding: 1em; border-left: 4px solid #1c5083;">
<strong> Guide complet disponible :</strong>  
Pour une procédure détaillée d'installation, connexion et dépannage, consultez le <a href="{{site.baseurl}}/arborescence/hardware/electronique/dynamixel/wizard">Cliquez ici pour y accéder</a>
</div>

