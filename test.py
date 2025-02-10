import csv

patients_dict = {}
with open("subjects.csv", 'r') as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            participant_id = ligne["participant_id"]
            patients_dict[participant_id] = {"sex": ligne["sex"], "age" : ligne["age"], "height" : ligne["height"], "weight" : ligne["weight"], "date_of_scan" : ligne["date_of_scan"], "pathology" : ligne["pathology"]}

print(patients_dict['sub-cmrra05'])


