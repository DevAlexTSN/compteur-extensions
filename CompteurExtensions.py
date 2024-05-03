# Demande à l'utilisateur de saisir le chemin d'un repertoire à analyser 
# Verifie sue le chemin saisi correspond à un repertoire valide sur le System
# Parcourir tous les fichiers dans ce repertoir et ses sous repertoire pour compter le nombre de fichier de chaque extension
# affiche le nombre de fichier par type ( extension) trouvé dans le repertoire

# importer la librairie Path
from pathlib import Path

#Demander a l'utilisateur de coller le chemin du dossier à analyser
chemin=input( "Coller le chemin du repertoire à analyser  " )
#renvoyer l'url du chemin dans une variable chemin_path
chemin_path =Path(chemin)

# Verifie que le chemin saisi correspond à un repertoire valide sur le systeme
if chemin_path.is_dir():
    print("Le chemin saisi correspond à un répertoire valide sur le système.")
else:
    print("Le chemin saisi ne correspond pas à un répertoire valide sur le système.")

#creation du dictionnaire afin de contenir en clé : le nom de l'extension en valeur : le nombre de fichier portant cette extension
nombreFichierExtension={}

#Parcourir tous les fichiers dans ce repertoir et ses sous repertoire pour compter le nombre de fichier de chaque extension
for fichier in Path(chemin).rglob('*'):
    extension=fichier.suffix[1:]    # le [1:] permet de supprimer le "." du nom de l'extension
#Incremente le nombre de fois ou l'extension à été trouvé   
    if extension in nombreFichierExtension:
        nombreFichierExtension[extension]+=1
#creer le compteur de l'extension si l'extension apparait pour la premiere fois.        
    else :
        nombreFichierExtension[extension]=1

#Affiche le dictionnaire.
print(nombreFichierExtension)

#Bonus : permet d'afficher le dictionnaire sous une forme plus lisible et litterale.
# for extension, count in nombreFichierExtension.items():
#     print(f"Extension : {extension}, Nombre de fichier : {count}")


    


        


