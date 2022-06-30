import lire
import creer
import sqlite3
import suppr
import database
from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import pytz

conn = sqlite3.connect('annonce.db', check_same_thread=False)
cursor = conn.cursor()
database.database()
row = lire.lire()

for r in row:
  print(r)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__) #__name__ self fichier __main__

@app.route('/') #run par défaut
def indexpage():
  return render_template('index.html',infos=row)

@app.route('/docs') #run par défaut
def docspage():
  return render_template('docs.html')




  
#action
@app.route('/supprimer', methods=['POST'])
def supprimerpage():
  secret = request.form.get('secret')
  res = cursor.execute("SELECT * FROM batisse where secret like '"+secret+"'")
  length = cursor.fetchall()
  for l in length:
    print(l)
  if len(length)>0:
      cursor.execute("SELECT id FROM batisse where secret like '"+secret+"'")
      ans = cursor.fetchone()
      for a in ans:
        element = a
      suppr.suppr(element)
      flash('Offre d\'achat supprimée.')
      return render_template('docs.html')
  else:
    flash('Le secret n\'existe pas.')

@app.route('/contact', methods=['POST'])
def contactpage():
  msg = request.form.get("qst")
  f = open("static/msg.txt", "a")
  utcmoment_naive = datetime.utcnow()
  utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
  localFormat = "%Y-%m-%d %H:%M:%S"
  localDatetime = utcmoment.astimezone(pytz.timezone("America/New_York"))
  f.write(msg+" Date:"+localDatetime.strftime(localFormat)+os.linesep)
  f.close()
  return render_template('docs.html')



@app.route('/creer', methods=['POST'])
def creerpage():
  adresse = request.form.get("adresse")
  logement = request.form.get("logement")
  representant = request.form.get("representant")
  telephone = request.form.get("telephone")
  courriel = request.form.get("courriel")

  description = request.form.get("description")
  superficie = request.form.get("superficie")
  paye = request.form.get("paye")
  cadastre = request.form.get("cadastre")
  terrain = request.form.get("terrain")
  
  anneet = request.form.get("anneet")
  batiment = request.form.get("batiment")
  anneeb = request.form.get("anneeb")
  reparation = request.form.get("reparation")
  construction = request.form.get("construction")
  
  anneec = request.form.get("anneec")
  fondation = request.form.get("fondation")
  categorie = request.form.get("categorie")
  etage = request.form.get("etage")
  chauffage = request.form.get("chauffage")
  
  eau = request.form.get("eau")
  electrique = request.form.get("electrique")
  plomberie = request.form.get("plomberie")
  toit = request.form.get("toit")
  balcon = request.form.get("balcon")
  
  bathroom = request.form.get("bathroom")
  fenetre = request.form.get("fenetre")
  soussol = request.form.get("soussol")
  creancier = request.form.get("creancier")
  bdv = request.form.get("bdv")
  
  interet = request.form.get("interet")
  revenu = request.form.get("revenu")
  tmunicipal = request.form.get("tmunicipal")
  tscolaire = request.form.get("tscolaire")
  potentiel = request.form.get("potentiel")
  
  justif = request.form.get("justif")
  prix = request.form.get("prix")
  secret = request.form.get("secret")
  utcmoment_naive = datetime.utcnow()
  utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
  localFormat = "%Y-%m-%d"
  localDatetime = utcmoment.astimezone(pytz.timezone("America/New_York"))
  creer.creer(adresse,logement,representant,telephone,courriel
          ,description,superficie,paye,cadastre,terrain,
          anneet,batiment,anneeb,reparation,construction,
          anneec,fondation,categorie,etage,chauffage
          ,eau,electrique,plomberie,toit,balcon,
          bathroom,fenetre,soussol,creancier,bdv,
          interet,revenu,tmunicipal,tscolaire,potentiel,
          justif,prix,secret,localDatetime.strftime(localFormat))
  return render_template('index.html')

app.secret_key = 'super secret key'
#app.run(host='0.0.0.0', port=5000)
 




