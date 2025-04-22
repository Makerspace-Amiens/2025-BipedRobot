<!-- TEMPLATE POUR LES NOTIONS IMPORTANTES ALGO BASE SUR K-MEANS -->

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

.kmeans-container {
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

<div class="kmeans-container">
    <!-- Introduction -->
    <section id="introduction">
        <h2>Qu'est-ce que l'algorithme K-means ?</h2>
        <hr>
        <p class="lead justified-text">
            K-means est un algorithme de clustering non supervisé qui partitionne un ensemble de données en k groupes distincts (clusters). Il est largement utilisé en apprentissage automatique pour la classification de données.
        </p>
        <p class="justified-text">
            L'algorithme fonctionne en itérant entre l'affectation des points aux centroïdes les plus proches et la mise à jour de la position des centroïdes jusqu'à convergence.
        </p>
        <div class="did-you-know">
            <h3>Le savais-tu ?</h3>
            <p>
                L'algorithme K-means a été proposé pour la première fois en 1957 par Stuart Lloyd, mais n'a été publié qu'en 1982. Il est aujourd'hui l'un des algorithmes de clustering les plus utilisés.
            </p>
        </div>
    </section>
    <!-- Principe Général -->
    <section id="principe">
        <h2>Principe Général de K-means</h2>
        <p class="justified-text">
            K-means fonctionne selon les étapes suivantes :
            1. Initialisation aléatoire des centroïdes
            2. Affectation de chaque point au centroïde le plus proche
            3. Recalcul des centroïdes comme moyenne des points du cluster
            4. Répétition jusqu'à convergence
        </p>
        <div class="math-equation">
            <p>$$ J = \sum_{i=1}^{k} \sum_{x \in C_i} \|x - \mu_i\|^2 $$</p>
        </div>
        <div class="diagram-container">
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
                <iframe width="560" height="315"  src="https://www.youtube.com/embed/R2e3Ls9H_fc" title="K-means vizualisation" frameborder="0"  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"  allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
            </div>
        </div>
        <p class="justified-text">
            La fonction de coût J (inertie) mesure la somme des distances au carré entre chaque point et son centroïde associé. L'algorithme cherche à minimiser cette valeur.
        </p>
    </section>
    <!-- Application au projet -->
    <section id="application_projet">
        <h2>Comment appliquer K-means au projet de robot bipède ?</h2>
        <p class="justified-text">
            Dans un robot bipède, K-means peut être utilisé pour classifier les différents états de marche ou pour regrouper des configurations articulaires similaires. Cela permet de simplifier la planification des mouvements et d'identifier des patterns de marche optimaux.
        </p>
    </section>
    <div class="code-container">
        <div class="code-header">
            <span>Implémentation K-means</span>
        </div>
        <pre><code>from sklearn.cluster import KMeans
import numpy as np

# Données des angles articulaires du robot
joint_angles = np.array([...])  # matrice n_samples x n_joints

# Application de K-means
kmeans = KMeans(n_clusters=5, random_state=0).fit(joint_angles)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_</code></pre>
    </div>
    <h2>Dans quelle partie du code peut intervenir K-means ?</h2>
    <div class="kmeans-application">
        <div class="application-card">
            <h3>Classification des patterns de marche</h3>
            <p>K-means peut être utilisé pour identifier et classifier les différents patterns de marche du robot bipède à partir des données des capteurs et des angles articulaires.</p>
            <p style="text-align: justify;"><strong>Exemple pratique :</strong></p>            
                <p style="text-align: justify;">En analysant les données historiques de marche, K-means peut découvrir des clusters naturels correspondant à différentes allures (lente, normale, rapide) ou différents types de terrain (plat, montée, descente).</p>
            <div class="goal">
                <span class="label">Objectif :</span> Optimiser la planification des mouvements en utilisant les centroïdes comme configurations articulaires de référence.
        </div>        
    </div>
</div>

<h3>Références</h3> <!--Style APA-->
<ul>
  <li>MacQueen, J. (1967). <cite>Some methods for classification and analysis of multivariate observations</cite>. Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability.</li>
  <li>Lloyd, S. (1982). <cite>Least squares quantization in PCM</cite>. IEEE Transactions on Information Theory.</li>
  <li>Arthur, D., & Vassilvitskii, S. (2007). <cite>k-means++: The advantages of careful seeding</cite>. Proceedings of the eighteenth annual ACM-SIAM symposium on Discrete algorithms.</li>
  <li>Pedregosa, F., et al. (2011). <cite>Scikit-learn: Machine Learning in Python</cite>. Journal of Machine Learning Research.</li>
</ul>