"""
TP2 : Gestion d'une base de données d'un hôpital

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

import csv

########################################################################################################## 
# PARTIE 1 : Initialisation des données (2 points)
##########################################################################################################

def load_csv(csv_path):
    """
    Fonction python dont l'objectif est de venir créer un dictionnaire "patients_dict" à partir d'un fichier csv

    Paramètres
    ----------
    csv_path : chaîne de caractères (str)
        Chemin vers le fichier csv (exemple: "/home/data/fichier.csv")
    
    Résultats
    ---------
    patients_dict : dictionnaire python (dict)
        Dictionnaire composé des informations contenues dans le fichier csv
    """
    patients_dict = {}

    # TODO : Écrire votre code ici


    with open(csv_path, 'r') as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            participant_id = ligne["participant_id"].strip()
            patients_dict[participant_id] = {"sex": ligne["sex"], "age" : ligne["age"], "height" : ligne["height"], \
                                             "weight" : ligne["weight"], "date_of_scan" : ligne["date_of_scan"], \
                                                "pathology" : ligne["pathology"]}
                

    # Fin du code

    return patients_dict

########################################################################################################## 
# PARTIE 2 : Fusion des données (3 points)
########################################################################################################## 

def load_multiple_csv(csv_path1, csv_path2):
    """
    Fonction python dont l'objectif est de venir créer un unique dictionnaire "patients" à partir de deux fichier csv

    Paramètres
    ----------
    csv_path1 : chaîne de caractères (str)
        Chemin vers le premier fichier csv (exemple: "/home/data/fichier1.csv")
    
    csv_path2 : chaîne de caractères (str)
        Chemin vers le second fichier csv (exemple: "/home/data/fichier2.csv")
    
    Résultats
    ---------
    patients_dict : dictionnaire python (dict)
        Dictionnaire composé des informations contenues dans les deux fichier csv SANS DUPLICATIONS
    """
    patients_dict = {}

    # TODO : Écrire votre code ici

    with open(csv_path1, 'r') as fichier1, open(csv_path2, 'r') as fichier2:
        patients_dict1 = {}
        patients_dict2 = {}
        lecteur1 = csv.DictReader(fichier1)
        lecteur2 = csv.DictReader(fichier2)
        for ligne1 in lecteur1:
            participant_id1 = ligne1["participant_id"]
            patients_dict1[participant_id1] = {"sex": ligne1["sex"], "age" : ligne1["age"], "height" : ligne1["height"],\
                                              "weight" : ligne1["weight"], "date_of_scan" : ligne1["date_of_scan"],\
                                                  "pathology" : ligne1["pathology"]}

        for ligne2 in lecteur2:
            participant_id2 = ligne2["participant_id"]
            patients_dict2[participant_id2] = {"sex": ligne2["sex"], "age" : ligne2["age"], "height" : ligne2["height"],\
                                              "weight" : ligne2["weight"], "date_of_scan" : ligne2["date_of_scan"],\
                                                  "pathology" : ligne2["pathology"]}
            
        for key in patients_dict1.keys():
            if key not in patients_dict2.keys():
                patients_dict[key] = patients_dict1[key]
            
        for key in patients_dict2.keys():
            if key not in patients_dict1.keys():
                patients_dict[key] = patients_dict2[key]
            else:
                patients_dict[key] = {**patients_dict1[key], **patients_dict2[key]}

    
        
   
   
   
    # Fin du code

    return patients_dict

########################################################################################################## 
# PARTIE 3 : Changements de convention (4 points)
########################################################################################################## 

def update_convention(old_convention_dict):
    """
    Fonction python dont l'objectif est de mettre à jour la convention d'un dictionnaire. Pour ce faire, un nouveau dictionnaire
    est généré à partir d'un dictionnaire d'entré.

    Paramètres
    ----------
    old_convention_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients" suivant l'ancienne convention
    
    Résultats
    ---------
    new_convention_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients" suivant la nouvelle convention
    """
    new_convention_dict = {}

    # TODO : Écrire votre code ici




    for participant_id in old_convention_dict.keys():
        new_convention_dict[participant_id] = {}
        for key, valeursscan in old_convention_dict[participant_id].items():
            if key == "date_of_scan":
                if valeursscan == "n/a":
                    new_convention_dict[participant_id][key] = None
                else:
                    new_convention_dict[participant_id][key] = valeursscan.replace("-", "/")
            else:
                new_convention_dict[participant_id][key] = valeursscan
                
            




        
    # Fin du code

    return new_convention_dict

########################################################################################################## 
# PARTIE 4 : Recherche de candidats pour une étude (5 points)
########################################################################################################## 

def fetch_candidates(patients_dict):
    """
    Fonction python dont l'objectif est de venir sélectionner des candidats à partir d'un dictionnaire patients et 3 critères:
    - sexe = femme
    - 25 <= âge <= 32
    - taille > 170

    Paramètres
    ----------
    patients_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients"
    
    Résultats
    ---------
    candidates_list : liste python (list)
        Liste composée des `participant_id` de l'ensemble des candidats suivant les critères
    """
    candidates_list = []

    # TODO : Écrire votre code ici

    for participant_id in patients_dict.keys():
        for key, value in patients_dict[participant_id].items():
            if patients_dict[participant_id][key] == "F" and 25 <= int(patients_dict[participant_id]["age"]) <= 32 and int(patients_dict[participant_id]["height"]) > 170:
                candidates_list.append(participant_id)

    # Fin du code

    return candidates_list

########################################################################################################## 
# PARTIE 5 : Statistiques (6 points)
########################################################################################################## 

def fetch_statistics(patients_dict):
    """
    Fonction python dont l'objectif est de venir calculer et ranger dans un nouveau dictionnaire "metrics" la moyenne et 
    l'écart type de l'âge, de la taille et de la masse pour chacun des sexes présents dans le dictionnaire "patients_dict".

    Paramètres
    ----------
    patients_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients"
    
    Résultats
    ---------
    metrics : dictionnaire python (dict)
        Dictionnaire à 3 niveaux contenant:
            - au premier niveau: le sexe --> metrics.keys() == ['M', 'F']
            - au deuxième niveau: les métriques --> metrics['M'].keys() == ['age', 'height', 'weight'] et metrics['F'].keys() == ['age', 'height', 'weight']
            - au troisième niveau: la moyenne et l'écart type --> metrics['M']['age'].keys() == ['mean', 'std'] ...
    
    """
    metrics = {'M':{}, 'F':{}}

    # TODO : Écrire votre code ici

    metrics = {
        'M': {'age': {'mean': 0, 'std': 0}, 'height': {'mean': 0, 'std': 0}, 'weight': {'mean': 0, 'std': 0}},
        'F': {'age': {'mean': 0, 'std': 0}, 'height': {'mean': 0, 'std': 0}, 'weight': {'mean': 0, 'std': 0}}
    }

    countfemale = {"age": 0, "height": 0, "weight": 0}
    countmale = {"age": 0, "height": 0, "weight": 0}

    for participant_id, base_value in patients_dict.items():
        sex = base_value["sex"]
        if sex == "F":
            if base_value["age"] != "n/a":
                countfemale["age"] += 1
                metrics["F"]["age"]["mean"] += int(base_value["age"])
            if base_value["height"] != "n/a":
                countfemale["height"] += 1
                metrics["F"]["height"]["mean"] += float(base_value["height"])
            if base_value["weight"] != "n/a":
                countfemale["weight"] += 1
                metrics["F"]["weight"]["mean"] += float(base_value["weight"])

        elif sex == "M":
            countmale["age"] += 1
            countmale["height"] += 1
            countmale["weight"] += 1
            if base_value["age"] != "n/a":
                metrics["M"]["age"]["mean"] += int(base_value["age"])
            if base_value["height"] != "n/a":
                metrics["M"]["height"]["mean"] += float(base_value["height"])
            if base_value["weight"] != "n/a":
                metrics["M"]["weight"]["mean"] += float(base_value["weight"])
                
    
    if countfemale["age"] != 0:
        metrics["F"]["age"]["mean"] = metrics["F"]["age"]["mean"] / countfemale["age"]
    if countfemale["height"] != 0:
        metrics["F"]["height"]["mean"] = metrics["F"]["height"]["mean"] / countfemale["height"]
    if countfemale["weight"] != 0:
        metrics["F"]["weight"]["mean"] = metrics["F"]["weight"]["mean"] / countfemale["weight"]
    if countmale["age"] != 0:
        metrics["M"]["age"]["mean"] = metrics["M"]["age"]["mean"] / countmale["age"]
    if countmale["height"] != 0:
        metrics["M"]["height"]["mean"] = metrics["M"]["height"]["mean"] / countmale["height"]
    if countmale["weight"] != 0:
        metrics["M"]["weight"]["mean"] = metrics["M"]["weight"]["mean"] / countmale["weight"]

    fsumage = 0
    fsumheight = 0
    fsumweight = 0
    msumage = 0
    msumheight = 0
    msumweight = 0

    for participant_id, base_value in patients_dict.items():
        sex = base_value["sex"]
        age = base_value["age"]
        height = base_value["height"]
        weight = base_value["weight"]
        if age != "n/a":
            age = int(base_value["age"])
        if height != "n/a":    
            height = float(base_value["height"])
        if weight != "n/a":
            weight = float(base_value["weight"])
        if sex == "F":
            if age != "n/a":
                fsumage += (age - float(metrics["F"]["age"]["mean"])) ** 2
            if height != "n/a":
                fsumheight += (height - float(metrics["F"]["height"]["mean"])) ** 2
            if weight != "n/a":
                fsumweight += (weight - float(metrics["F"]["weight"]["mean"])) ** 2
        elif sex == "M":
            if age != "n/a":
                msumage += (age - float(metrics["M"]["age"]["mean"])) ** 2
            if height != "n/a":
                msumheight += (height - float(metrics["M"]["height"]["mean"])) ** 2
            if weight != "n/a":
                msumweight += (weight - float(metrics["M"]["weight"]["mean"])) ** 2


    metrics["F"]["age"]["std"] = (1/countfemale["age"] * fsumage) ** 0.5
    metrics["F"]["height"]["std"] = (1/countfemale["height"] * fsumheight) ** 0.5
    metrics["F"]["weight"]["std"] = (1/countfemale["weight"] * fsumweight) ** 0.5
    metrics["M"]["age"]["std"] = (1/countmale["age"] * msumage) ** 0.5
    metrics["M"]["height"]["std"] = (1/countmale["height"] * msumheight) ** 0.5
    metrics["M"]["weight"]["std"] = (1/countmale["weight"] * msumweight) ** 0.5
    

    # Fin du code

    return metrics

########################################################################################################## 
# PARTIE 6 : Bonus (+2 points)
########################################################################################################## 

def create_csv(metrics):
    """
    Fonction python dont l'objectif est d'enregister le dictionnaire "metrics" au sein de deux fichier csv appelés
    "F_metrics.csv" et "M_metrics.csv" respectivement pour les deux sexes.

    Paramètres
    ----------
    metrics : dictionnaire python (dict)
        Dictionnaire à 3 niveaux généré lors de la partie 5
    
    Résultats
    ---------
    paths_list : liste python (list)
        Liste contenant les chemins des deux fichiers "F_metrics.csv" et "M_metrics.csv"
    """
    paths_list = []

    # TODO : Écrire votre code ici

    with open("F_metrics.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["stats","age","height","weight"])
        writer.writerow(["mean", metrics["F"]["age"]["mean"], metrics["F"]["height"]["mean"], metrics["F"]["weight"]["mean"]])
        writer.writerow(["std", metrics["F"]["age"]["std"], metrics["F"]["height"]["std"], metrics["F"]["weight"]["std"]])

    with open("M_metrics.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["stats","age","height","weight"])
        writer.writerow(["mean", metrics["M"]["age"]["mean"], metrics["M"]["height"]["mean"], metrics["M"]["weight"]["mean"]])
        writer.writerow(["std", metrics["M"]["age"]["std"], metrics["M"]["height"]["std"], metrics["M"]["weight"]["std"]])

    paths_list = ["F_metrics.csv", "M_metrics.csv"]

    # Fin du code

    return paths_list

########################################################################################################## 
# TESTS : Le code qui suit permet de tester les différentes parties 
########################################################################################################## 

if __name__ == '__main__':
    ######################
    # Tester la partie 1 #
    ######################

    # Initialisation de l'argument
    csv_path = "subjects.csv"

    # Utilisation de la fonction
    patients_dict = load_csv(csv_path)

    # Affichage du résultat
    print("Partie 1: \n\n", patients_dict, "\n")

    ######################
    # Tester la partie 2 #
    ######################

    # Initialisation des arguments
    csv_path1 = "subjects.csv"
    csv_path2 = "extra_subjects.csv"

    # Utilisation de la fonction
    patients_dict_multi = load_multiple_csv(csv_path1=csv_path1, csv_path2=csv_path2)

    # Affichage du résultat
    print("Partie 2: \n\n", patients_dict_multi, "\n")

    ######################
    # Tester la partie 3 #
    ######################

    # Utilisation de la fonction
    patients_dict = update_convention(patients_dict)

    # Affichage du résultat
    print("Partie 3: \n\n", patients_dict, "\n")

    ######################
    # Tester la partie 4 #
    ######################

    # Utilisation de la fonction
    patients_list = fetch_candidates(patients_dict)

    # Affichage du résultat
    print("Partie 4: \n\n", patients_list, "\n")

    ######################
    # Tester la partie 5 #
    ######################

    # Utilisation de la fonction
    metrics = fetch_statistics(patients_dict)

    # Affichage du résultat
    print("Partie 5: \n\n", metrics, "\n")

    ######################
    # Tester la partie 6 #
    ######################

    # Initialisation des arguments
    dummy_metrics = {'M':{'age':{'mean':0,'std':0}, 'height':{'mean':0,'std':0}, 'weight':{'mean':0,'std':0}}, 
                     'F':{'age':{'mean':0,'std':0}, 'height':{'mean':0,'std':0}, 'weight':{'mean':0,'std':0}}}
    
    # Utilisation de la fonction
    paths_list = create_csv(metrics)

    # Affichage du résultat
    print("Partie 6: \n\n", paths_list, "\n")

