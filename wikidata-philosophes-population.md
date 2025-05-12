
# 📚 Documentation – Wikidata : population des philosophes (projet Humanités)

## 🧠 Objectif
Ce document décrit les requêtes SPARQL utilisées pour extraire une base de données de philosophes nés après 1700 à partir de Wikidata, en lien avec 5 problématiques prosopographiques.

---

## 📌 Problématiques et requêtes associées

---

### 🧑‍🤝‍🧑 1. Profils socio-démographiques dominants

**Objectif :** explorer la distribution selon le sexe, la nationalité, le siècle de naissance, et la formation académique.

#### 🔎 Requête – Sexe, nationalité, naissance

```sparql
SELECT ?philosopher ?philosopherLabel ?birthDate ?sexLabel ?nationalityLabel
WHERE {
  ?philosopher wdt:P31 wd:Q5;
               wdt:P106 wd:Q4964182;
               wdt:P569 ?birthDate.
  FILTER(?birthDate >= "1700-01-01T00:00:00Z"^^xsd:dateTime)

  OPTIONAL { ?philosopher wdt:P21 ?sex. }
  OPTIONAL { ?philosopher wdt:P27 ?nationality. }

  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr,en". }
}
LIMIT 1000
```

#### 🔎 Requête – Études (formation académique)

```sparql
SELECT DISTINCT ?philosopher ?philosopherLabel ?birthDate ?universityLabel
WHERE {
  ?philosopher wdt:P31 wd:Q5;
               wdt:P106 wd:Q4964182;
               wdt:P569 ?birthDate;
               p:P69 ?statement.
  ?statement ps:P69 ?university.

  FILTER(?birthDate >= "1700-01-01T00:00:00Z"^^xsd:dateTime)

  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr,en". }
}
```

📌 *À faire dans le notebook 1 : Histogramme sexe / nationalité / siècle.*

---

### 🧬 2. Filiations maître–élève

**Objectif :** détecter les relations intellectuelles entre philosophes à travers les liens hiérarchiques.

```sparql
SELECT ?philosopher ?philosopherLabel ?student ?studentLabel
WHERE {
  ?philosopher wdt:P106 wd:Q4964182;
               wdt:P802 ?student.  # has student
  ?student wdt:P106 wd:Q4964182.

  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr,en". }
}
```

📌 *À visualiser dans notebook 3 (analyse de réseaux). Graphe avec maîtres et élèves.*

---

### 🏛️ 3. Appartenances institutionnelles

**Objectif :** analyser les affiliations à des institutions (universités, académies, etc.) et leur lien avec les individus.

```sparql
SELECT DISTINCT ?philosopher ?philosopherLabel ?organizationLabel ?startYear ?endYear
WHERE {
  ?philosopher wdt:P106 wd:Q4964182;
               p:P463 ?statement.  # member of
  ?statement ps:P463 ?organization.
  OPTIONAL { ?statement pq:P580 ?startTime. }
  OPTIONAL { ?statement pq:P582 ?endTime. }

  BIND(YEAR(?startTime) AS ?startYear)
  BIND(YEAR(?endTime) AS ?endYear)

  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr,en". }
}
```

📌 *À visualiser dans notebook 3 (analyse de réseaux bipartis : philosophes – institutions).*

---

### 🧭 4. Évolution des courants philosophiques

**Objectif :** observer les tendances dominantes dans le temps.

```sparql
SELECT ?philosopher ?philosopherLabel ?movementLabel ?birthDate
WHERE {
  ?philosopher wdt:P106 wd:Q4964182;
               wdt:P569 ?birthDate;
               wdt:P135 ?movement.  # movement
  FILTER(?birthDate >= "1700-01-01T00:00:00Z"^^xsd:dateTime)

  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr,en". }
}
```

📌 *À faire dans notebook 1 ou 2 : courbe temporelle ou heatmap par siècle / courant.*

---

### 🌍 5. Influence des origines géographiques sur les courants

**Objectif :** croiser pays d’origine avec école de pensée.

```sparql
SELECT ?philosopher ?philosopherLabel ?nationalityLabel ?movementLabel
WHERE {
  ?philosopher wdt:P106 wd:Q4964182;
               wdt:P27 ?nationality;
               wdt:P135 ?movement.

  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr,en". }
}
```

📌 *À faire dans notebook 2 : tableau croisé nationalité × courant, test du Chi².*

---

## 🔗 Outils et ressources

- [Wikidata SPARQL Endpoint](https://query.wikidata.org)
- [Query Builder](https://query.wikidata.org/querybuilder/?uselang=fr)
- [SPARQL 1.1](https://www.w3.org/TR/sparql11-query)
- [Zazuko Tutorial (FR)](https://www.zazuko.com/sparql)

---
