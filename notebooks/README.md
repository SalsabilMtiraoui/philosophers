# Notebooks – Analyses prosopographiques

### `01_distribution_qualitative.ipynb`
**Analyse descriptive et temporelle** des variables qualitatives :
- Répartition des genres dans le temps par tranches de 25 ans (comem dans l'exemple proposé).
- Évolution historique des écoles de pensée dominantes.
- Visualisation interactive en `Plotly` + export `.html`.

### `02_analyse_bivariee_chi2.ipynb`
**Analyse bivariée de variables qualitatives** :
- Croisement entre nationalité et école de pensée.
- Tests d’indépendance du Chi-2.
- Visualisation sous forme de heatmaps et tableaux croisés.
- Export des visualisations interactives.

### `03_analyse_reseaux.ipynb`
**Analyse relationnelle (réseaux) autour des philosophes** :
- Graphe orienté des relations maître → élève (P184).
- Graphe biparti philosophes ↔ institutions (universités).
- Matrice d’adjacence du graphe.
- Visualisation interactive avec `pyvis`.

---

## Visualisations exportées

Des fichiers `.html` interactifs ont été générés pour permettre une exploration rapide des résultats :
- `plot_genre_par_25_ans.html` : évolution du genre.
- `fig_nationalites.html` : heatmap écoles/nationalités.
- `graph_maitre_eleve.html` : réseau maître ↔ élève.
- `distribution_regions.html`, `ecole_nationalite_interactive.html`

---

