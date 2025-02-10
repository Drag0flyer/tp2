# TP2: Gestion de bases de données d'un hôpital

<img width="888" alt="tp_illustration" src="https://github.com/user-attachments/assets/672bddcb-34e0-41a7-a110-110a9dc62e57" />

Crédits: [DALLE 3](https://openai.com/index/dall-e/)

## Directives

⏰ Date de remise : Dimanche 16 février 2025 avant 23h59

📬 À remettre sur Moodle: créer un fichier .zip nommé LXX-YY-TP2.zip où XX est le numéro de votre section de laboratoire et YY le numéro de votre équipe.

## Objectifs

L'objectif de ce travail pratique est d'apprendre à manipuler une base de données en utilisant Python. Ce TP vous permettra de découvrir et de maîtriser :  

- Les structures de contrôle, telles que les structures conditionnelles (`if`, `else`, etc.) et les structures de répétition (`for`, `while`, etc.)  
- Les différentes structures de données, comme les listes, les dictionnaires, et les tuples.
- Le module python `csv` permettant d'ouvrir et d'enregister des fichiers csv.

Ces notions seront explorées à travers différentes parties présentant chacunes différentes utilisations pratiques de ces outils.

## Introduction

Vous avez récemment été engagé par un hôpital pour gérer plusieurs bases de données dont la liste de patients ayant été scannés dans le cadre de travaux de recherche en IRM. Cette base de données, accessible dans le fichier `subjects.csv`, contient les informations suivantes:
- `participant_id`: identifiant unique associé au patient
- `age`: âge du patient
- `sex`: sexe bilogique du patient
- `height`: taille du patient (cm)
- `weight`: masse du patient (kg)
- `date_of_scan`: date de scan (YYYY-MM-DD)
- `pathology`: pathologie
  - HC: Healthy Control (patient sain)
  - DCM: Degenerative Cervical Myelopathy (myelopathie cervicale degenerative)
  - MildCompression: Mild Spinal Cord Copression (compression moyenne de la moelle épinière)

## Partie 1: Initialisation des données (2 points)

Dans cette section, vous devrez charger les données contenues dans le fichier `subjects.csv` à l'aide du module python [csv](https://python-adv-web-apps.readthedocs.io/en/latest/csv.html) et constituer un dictionnaire python appelé `patients_dict` utilisant:
- `participant_id` comme clé principale
- un deuxième dictionnaire comprenant le reste des informations en guise de valeur.

Exemple:
```
> print(patients['sub-tokyoIngenia04'])
{'sex': 'F', 'age': '34', 'height': '161', 'weight': '65', 'date_of_scan': '2019-10-01', 'pathology': 'MildCompression'}
```

Pour ce faire, modifier la fonction `load_csv` prenant en argumant le chemin d'un fichier csv et retounant le dictionnaire `patients_dict`.

## Partie 2: Fusion des données (3 points)

Vous vous apercevez qu'un collègue à vous dispose également d'une liste de patients et vous souhaiteriez regrouper tous ces derniers au sein d'un unique dictionnaire python appelé `patients_dict` comme précédemment. Dans cette partie, vous devrez regrouper l'ensemble des patients provenant des fichiers `subjects.csv` et `extra_subjects.csv` en suivant la même construction que dans la partie 1.

Pour ce faire, modifier la fonction `load_multiple_csv` prenant en argumant les chemin de deux fichier csv et retournant un unique dictionnaire `patients_dict` composé de l'ensemble des patients.

> ⚠️ Certains patients apparaissent dans les deux dictionnaires, assurez-vous de ne pas les ajouter plusieurs fois.

## Partie 3: Changements de convention (4 points)

L'hôpital dans lequel vous travaillez décide de mettre à jour l'ensemble de ses bases de données pour suivre une nouvelle convention au niveau des **DATES**. Cette nouvelle convention impose:
- d'utiliser des slashs `/` à la place des tirets `-`
- de remplacer les mentions `n/a` par l'objet python **None**

Afin de respecter ces nouvelles conventions, modifier la fonction `update_convention` pour mettre à jour automatiquement un dictionnaire comme ceux (`patients_dict`) générés lors des parties 1 et 2.

## Partie 4: Recherche de candidats pour une étude (5 points)

Dans le cadre d'une nouvelle étude, un groupe de chercheurs de votre hôpital sollicite votre expertise pour identifier des patients pour de nouveaux scans IRM. Cependant, ces candidats doivent répondre aux critères suivants :
| Sexe | Âge | Taille |
|:---:|:---:|:---:|
|Feminin|25 ≤ âge ≤ 32| taille > 170|

En suivant ces critères, modifier la fonction `fetch_candidates` prenant en argument un dictionnaire `patients_dict` et retournant une liste des `participant_id` de l'ensemble des candidats éligibles.

## Partie 5: Statistiques (6 points)

L'hôpital souhaiterait obtenir les statistiques par sexe de votre base de données. Pour cela, calculez la moyenne et l'écart type de `l'âge`, de `la taille` et de `la masse` pour chacun des deux groupes. Les statistiques devront être rangées au sein d'un nouveau dictionnaire appelé `metrics` composé de 3 niveaux.

Par exemple:
- la moyenne de la taille dans le groupe masculin sera obtenue de la manière suivante:
```python
print(metrics['M']['height']['mean'])
```
- l'écart type de l'âge dans le groupe feminin sera obtenue de la manière suivante:
```python
print(metrics['F']['age']['std'])
```

Pour ce faire, modifier la fonction `fetch_statistics` prenant en argument un dictionnaire `patients_dict` et retournant un dictionnaire `metrics` comportant les moyennes et les écarts-types de `l'âge`, de `la taille` et de `la masse` pour chacun des sexes.

## Partie 6: Bonus (+2 points)

À partir du dictionnaire obtenu dans la partie 5, créer à l'aide du module [csv](https://python-adv-web-apps.readthedocs.io/en/latest/csv.html) deux fichiers appelés respectivement `F_metrics.csv` et `M_metrics.csv` pour chaques sexes. Ces csv devront être construits de la manière suivante:
```csv
stats,age,height,weight
mean,0.0,0.0,0.0
std,0.0,0.0,0.0
```

Pour ce faire, modifier la fonction `create_csv` prenant en argument le dictionnaire `metrics` et retournant les chemins vers les deux fichiers créés.

> ⚠️ Pour la correction de cette partie, les valeurs de moyenne et d'écart-type ne seront pas vérifiées, il est donc possible de faire cet exercice sans avoir réalisé la partie 5 !

## Références

Les données utilisées dans les fichiers csv de ce TP sont extraites de la base de données [data-multi-subject](https://github.com/spine-generic/data-multi-subject).  

 
