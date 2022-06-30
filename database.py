import sqlite3
import os
conn = sqlite3.connect('annonce.db')
cursor = conn.cursor()

def database():
  empty = is_file_empty('annonce.db')
  if empty:
    try:
      cursor.execute('''CREATE TABLE batisse (
 id INTEGER PRIMARY KEY,
 `adresse` varchar(50) NOT NULL,
 `logement` int(11) NOT NULL,
 `representant` varchar(50) NOT NULL,
                     
 `telephone` varchar(12) NULL,
                     
 `courriel` varchar(25) NOT NULL,
                     
 `description` text NULL,
                     
 `superficie` int(11) NOT NULL,
 `paye` int(11) NOT NULL,
 `cadastre` varchar(8) NOT NULL,
 `terrain` int(11) NOT NULL,
                     
 `anneet` int(11) NULL,
                     
 `batiment` int(11) NOT NULL,
                     
 `anneeb` int(11) NULL,                     
 `reparation` text NULL,                 
 `construction` int(11) NULL,
                     
 `anneec` int(11) NOT NULL,                    
 `fondation` text NOT NULL,
 `categorie` text NOT NULL,
 `etage` int(11) NOT NULL,
                     
 `chauffage` text NULL,
 `eau` text NULL,
 `electrique` text NULL,
 `plomberie` text NULL,
 `toit` text NULL,
 `balcon` text NULL,
 `bathroom` text NULL,
 `fenetre` text NULL,
 `soussol` text NULL,
                     
 `creancier` text NOT NULL,
                     
 `bdv` text NULL,             
 `interet` text NULL,
                     
 `revenu` int(11) NOT NULL,                    
 `tmunicipal` int(11) NOT NULL,
 `tscolaire` int(11) NOT NULL,
                     
 `potentiel` int(11) NULL,
                     
 `justif` text NOT NULL,
 `prix` int(11) NOT NULL,
 `secret` text NOT NULL,
 `date` DATE NOT NULL                   
)
''')
    except Exception:
      return 404
def is_file_empty(file_path):
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0