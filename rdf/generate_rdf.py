import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef

# Charger le fichier CSV
df = pd.read_csv("philosophes_post1700.csv")

# Préparer un graphe RDF
g = Graph()

# Définir un namespace pour ton projet
EX = Namespace("http://example.org/philosophes/")
SCHEMA = Namespace("http://schema.org/")

# Ajouter les namespaces
g.bind("ex", EX)
g.bind("schema", SCHEMA)

# Boucler sur chaque ligne du DataFrame
for _, row in df.iterrows():
    if pd.isna(row["philosopherLabel"]):
        continue  # Ignorer les lignes sans nom

    # Créer un URI unique pour chaque philosophe
    name = row["philosopherLabel"].strip().replace(" ", "_").replace(",", "")
    philosopher_uri = URIRef(EX + name)

    g.add((philosopher_uri, RDF.type, SCHEMA.Person))
    g.add((philosopher_uri, SCHEMA.name, Literal(row["philosopherLabel"])))

    # Ajouter les propriétés RDF si disponibles
    if pd.notna(row["birthDate"]):
        g.add((philosopher_uri, SCHEMA.birthDate, Literal(row["birthDate"])))

    if pd.notna(row["sexLabel"]):
        g.add((philosopher_uri, SCHEMA.gender, Literal(row["sexLabel"])))

    if pd.notna(row["nationalityLabel"]):
        g.add((philosopher_uri, SCHEMA.nationality, Literal(row["nationalityLabel"])))

    if pd.notna(row["movementLabel"]):
        g.add((philosopher_uri, SCHEMA.knowsAbout, Literal(row["movementLabel"])))

    if pd.notna(row["teacherLabel"]):
        g.add((philosopher_uri, SCHEMA.alumniOf, Literal(row["teacherLabel"])))

    if pd.notna(row["studentLabel"]):
        g.add((philosopher_uri, SCHEMA.knows, Literal(row["studentLabel"])))

# Sauvegarder le graphe au format Turtle
g.serialize(destination="philosophes.ttl", format="turtle")

print("✅ RDF exporté dans 'philosophes.ttl'")
