# 🧭 Évolution des courants philosophiques selon la période

## 🎯 Objectif

Analyser l'évolution temporelle des grands mouvements philosophiques à partir de la date de naissance des philosophes, en s'appuyant sur les données Wikidata.

## 🔎 Méthodologie

Nous avons extrait les philosophes associés à un mouvement (`P135`) et une date de naissance (`P569`). Ces données ont été croisées pour déterminer la répartition des courants par tranche de 25 ans.

Les données sont issues du fichier `philosophes_post1700.csv`, enrichi par les propriétés issues de `wikidata_philosophes_properties.csv`.

## 📊 Résultats

### Représentation : genres et écoles par tranches de 25 ans

![Distribution des courants par période](../notebooks/plot_genre_par_25_ans.html)

- Une forte émergence des courants analytiques et existentialistes au XXe siècle.
- Les courants rationalistes, idéalistes et religieux dominent les périodes antérieures à 1850.
- Les femmes philosophes deviennent statistiquement visibles à partir du XXe siècle, notamment dans les courants féministes.

## ✅ Conclusion

Cette analyse permet de visualiser les dynamiques d’émergence des courants philosophiques. L’approche temporelle met en évidence les transitions historiques, les dominations idéologiques et l’évolution des profils sociologiques du champ intellectuel.