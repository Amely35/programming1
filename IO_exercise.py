import os

def kopieer_regels_met_voorwaarde(source, destination, voorwaarde):
   source_path = os.path.join(os.getcwd(), "source.txt")
   destination_path = os.path.join(os.getcwd(), "destination.txt")

   with open(source_path, 'r', encoding="utf-8") as src, open(destination_path, "w", encoding="utf-8") as dest: 
       for line in src: 
           if voorwaarde(line):
               dest.write(line)

def mijn_voorwaarde(regel):
    return len(regel.strip()) >= 10 and " " in regel

kopieer_regels_met_voorwaarde("source.txt", "destionation.txt", mijn_voorwaarde)


