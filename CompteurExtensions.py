# Demande à l'utilisateur de saisir le chemin d'un repertoire à analyser 
# Verifie sue le chemin saisi correspond à un repertoire valide sur le System
# Parcourir tous les fichiers dans ce repertoir et ses sous repertoire pour compter le nombre de fichier de chaque extension
# affiche le nombre de fichier par type ( extension) trouvé dans le repertoire


from pathlib import Path

chemin=input( "Coller le chemin du repertoire à analyser  " )
chemin_path =Path(chemin)

if chemin_path.is_dir():
    print("Le chemin saisi correspond à un répertoire valide sur le système.")
else:
    print("Le chemin saisi ne correspond pas à un répertoire valide sur le système.")

nombreFichierExtension={}

for fichier in Path(chemin).rglob('*'):
    extension=fichier.suffix[1:]    
    if extension in nombreFichierExtension:
        nombreFichierExtension[extension]+=1
        
    else :
        nombreFichierExtension[extension]=1

print(nombreFichierExtension)
# for extension, count in nombreFichierExtension.items():
#     print(f"Extension : {extension}, Nombre de fichier : {count}")


    


        


