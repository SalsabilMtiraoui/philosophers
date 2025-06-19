# Profils socio-démographiques des philosophes

## Objectif
Analyser la répartition des philosophes par sexe, nationalité et siècle de naissance à partir des données Wikidata.

## Méthodologie
Les données ont été extraites via des requêtes SPARQL ciblant les philosophes nés après 1700. Les colonnes d'intérêt sont le sexe, la nationalité et la date de naissance. Les visualisations ont été générées à partir de la base `philosophes_post1700.csv`.

## Résultats

### Répartition par sexe
![image](https://github.com/user-attachments/assets/3da2a01d-025f-449f-acd7-5595b4644c0a)

On observe une surreprésentation masculine marquée, traduisant des inégalités historiques dans l'accès aux carrières philosophiques.

### Répartition par nationalité
![Nationalité](../notebooks/images/plot_nationalite.png)

Les pays européens, notamment la France, l'Allemagne et le Royaume-Uni, concentrent une large part des philosophes référencés.

### Répartition par siècle de naissance
![Siècle](../notebooks/images/plot_siecle.png)

La production philosophique connaît un essor majeur au XVIIIe et XIXe siècle, avec un pic de naissances au XXe.
