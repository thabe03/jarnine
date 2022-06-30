import sqlite3
conn = sqlite3.connect('annonce.db',check_same_thread=False)
cursor = conn.cursor()

def creer(adresse,logement,representant,telephone,courriel
          ,description,superficie,paye,cadastre,terrain,
          anneet,batiment,anneeb,reparation,construction,
          anneec,fondation,categorie,etage,chauffage
          ,eau,electrique,plomberie,toit,balcon,
          bathroom,fenetre,soussol,creancier,bdv,
          interet,revenu,tmunicipal,tscolaire,potentiel,
          justif,prix,secret,date):
            
  batisse = []
            
  batisse.append(adresse)
  batisse.append(logement)
  batisse.append(representant)
  batisse.append(telephone)           
  batisse.append(courriel)
            
  batisse.append(description)
  batisse.append(superficie)
  batisse.append(paye)
  batisse.append(cadastre)
  batisse.append(terrain)
            
  batisse.append(anneet)
  batisse.append(batiment)
  batisse.append(anneeb)
  batisse.append(reparation)
  batisse.append(construction)
            
  batisse.append(anneec)
  batisse.append(fondation)
  batisse.append(categorie)
  batisse.append(etage)
  batisse.append(chauffage)
            
  batisse.append(eau)
  batisse.append(electrique)
  batisse.append(plomberie)
  batisse.append(toit)
  batisse.append(balcon)
            
  batisse.append(bathroom)
  batisse.append(fenetre)
  batisse.append(soussol)
  batisse.append(creancier)
  batisse.append(bdv)
            
  batisse.append(interet)
  batisse.append(revenu)
  batisse.append(tmunicipal)
  batisse.append(tscolaire)
  batisse.append(potentiel)
            
  batisse.append(justif)
  batisse.append(prix)
  batisse.append(secret)
  batisse.append(date)          

  try:
    cursor.execute('INSERT INTO `batisse` (`adresse`, `logement`, `representant`, `telephone`, `courriel`, `description`, `superficie`, `paye`, `cadastre`, `terrain`, `anneet`, `batiment`, `anneeb`, `reparation`, `construction`, `anneec`, `fondation`, `categorie`, `etage`, `chauffage`, `eau`, `electrique`, `plomberie`, `toit`, `balcon`, `bathroom`, `fenetre`, `soussol`, `creancier`, `bdv`, `interet`, `revenu`, `tmunicipal`, `tscolaire`, `potentiel`, `justif`, `prix`,`secret`,`date`) VALUES (?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?)', batisse)
    conn.commit()
  except Exception as e:
    print(e)
