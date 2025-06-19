
# Dossier RDF – Base de données des philosophes

Ce dossier contient la base RDF du projet Humanités et Data Science portant sur les philosophes nés après 1700, extraite depuis Wikidata et exportée au format Turtle pour import dans un triplestore AllegroGraph.

##  Contenu

- `philosophes.ttl` : fichier RDF au format Turtle 
- `philosophes.ttl.zip` : version compressée pour import dans AllegroGraph 
- `philosophes_post1700.csv` : export brut des philosophes (base de travail intermédiaire)
- `generate_rdf.py` : script Python permettant de générer le fichier `.ttl` à partir du CSV (j'ai eu quelques soucis avec l'export de base)
