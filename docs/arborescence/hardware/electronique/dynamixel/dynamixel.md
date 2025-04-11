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
            <td>59</td>
            <td>59</td>
            <td>tr/min (à 12V)</td>
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
            <td>°C</td>
        </tr>
        <tr>
            <td>Poids</td>
            <td>53.5</td>
            <td>53.5</td>
            <td>g</td>
        </tr>
        <tr>
            <td>Dimensions (L × H × P)</td>
            <td colspan="2">32 × 50 × 40</td>
            <td>mm</td>
        </tr>
        <tr>
            <td>Résolution</td>
            <td colspan="2">0.29</td>
            <td>°</td>
        </tr>
        <tr>
            <td>Mode rotation continue</td>
            <td colspan="2">Oui</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Type de moteur</td>
            <td colspan="2">Aimant permanent</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Rapport de réduction</td>
            <td colspan="2">254:1</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Couple de blocage</td>
            <td colspan="2">1.5</td>
            <td>N·m (à 12V, 1.5A)</td>
        </tr>
        <tr>
            <td>Vitesse à vide</td>
            <td colspan="2">59</td>
            <td>tr/min (à 12V)</td>
        </tr>
        <tr>
            <td>Protocole de communication</td>
            <td colspan="2">Paquet numérique</td>
            <td>-</td>
        </tr>
        <tr>
            <td>ID disponibles</td>
            <td colspan="2">254 (0-253)</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Retour d'information</td>
            <td colspan="2">Position, Température, Charge, Tension d'entrée</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Matériau des engrenages</td>
            <td colspan="2">Plastique technique (complet)</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Matériau du boîtier</td>
            <td colspan="2">Plastique technique (avant, milieu, arrière)</td>
            <td>-</td>
        </tr>
    </tbody>
</table>

## Avantages et Inconvénients

<div style="display: flex; gap: 20px; margin: 1.5em 0;">
    <div style="flex: 1; background: #f0f7f0; padding: 1em; border-radius: 8px; border-left: 4px solid #4CAF50;">
        <h3 style="color: #2E7D32; margin-top: 0;">✔ Avantages</h3>
        <ul style="padding-left: 20px;">
            <li><strong>Réseau facile</strong> - Contrôle de plusieurs moteurs en série via bus Dynamixel</li>
            <li><strong>Retour d'information complet</strong> - Position, température, charge en temps réel</li>
            <li><strong>Large plage de tension</strong> - Fonctionne de 9V à 12V</li>
        </ul>
    </div>    
    <div style="flex: 1; background: #fdf0f0; padding: 1em; border-radius: 8px; border-left: 4px solid #f44336;">
        <h3 style="color: #c62828; margin-top: 0;">✖ Inconvénients</h3>
        <ul style="padding-left: 20px;">
            <li><strong>Protocole propriétaire</strong> - Nécessite un convertisseur TTL/USB spécifique</li>
            <li><strong>Poids</strong> - Plus lourd que des servos standards (53.5g)</li>
            <li><strong>Prix</strong> - Plus coûteux qu'un servo classique</li>
        </ul>
    </div>
</div>

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

<div style="text-align: justify; font-size: 15px; line-height: 1.6; color: #333;">
    <p>Dynamixel Wizard est un logiciel de configuration et de diagnostic développé par ROBOTIS pour ses servomoteurs intelligents Dynamixel. Il permet de paramétrer, tester et dépanner facilement des moteurs Dynamixel via une interface intuitive.</p>
</div>

<div class="notice" style="background: #f8f9fa; padding: 1.2em; border-left: 4px solid #1c5083; margin: 1.5em 0; border-radius: 0 4px 4px 0; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
    <strong style="font-size: 15px; color: #1c5083;"> Guide complet disponible :</strong>
    <div style="margin-top: 8px;">
        <a href="{{ '/arborescence/hardware/electronique/dynamixel/wizard' | relative_url }}" style="color: #2a6496; text-decoration: none; font-weight: 500;">
            → Accéder au guide Dynamixel Wizard
        </a>
    </div>
</div>

<div style="text-align: justify; font-size: 15px; line-height: 1.6; color: #333; margin-bottom: 1.5em;">
    <p>Nous avons utilisé ce logiciel pour vérifier l'état de nos servomoteurs. Les tests portaient sur :</p>
    <ul style="margin-top: 0.5em; padding-left: 1.2em;">
        <li>La tension d'alimentation</li>
        <li>La qualité de la connexion</li>
        <li>La réactivité des moteurs</li>
        <li>La température en fonctionnement</li>
    </ul>
    <p>Ces vérifications ont été réalisées en suivant scrupuleusement le guide d'utilisation de Dynamixel Wizard 2.0.</p>
</div>

<div style="background-color: #f5f7fa; padding: 1em 1.2em; border-radius: 6px; margin-top: 1.5em; border-left: 3px solid #4a6ea9;">
    <div style="font-size: 14px; color: #555; margin-bottom: 6px;">
        <strong> Date des tests :</strong> 10/04/2025
    </div>
    <div style="font-size: 14px;">
        <a href="{{site.baseurl}}/assets/xlsx/Tests_Servomoteurs_Dynamixel.xlsx" style="color: #2a6496; text-decoration: none; font-weight: 500;">
            Télécharger les résultats complets (fichier Excel)
        </a>
    </div>
</div>