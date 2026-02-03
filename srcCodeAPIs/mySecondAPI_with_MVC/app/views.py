from app import app
<<<<<<< HEAD
from flask import render_template, request, jsonify, redirect, url_for
=======
from flask import render_template, request, jsonify, redirect, url_for, abort
>>>>>>> 54e06c0 (Initial commit for the project)
from app import db
from app.models import Patient

### EXO1 - simple API
@app.route('/params', methods=['GET'])
def params():
    """Récupère name et surname en query string, ex: /params?name=Jean&surname=Dupont"""
    name = request.args.get('name', '')
    surname = request.args.get('surname', '')

    return jsonify({"message": f"Bonjour {name} {surname}"})

### EXO2 - API with simple display
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

### EXO3 - API with parameters display 
@app.route('/exo3', methods=['GET'])
def exo3():
    # Récupérer les paramètres dans l'URL : ?name=Jean&age=20
    name = request.args.get('name', 'Inconnu')
    age = request.args.get('age', 'Non précisé')

    # Retour JSON
    return jsonify(
        f"Bonjour {name}, tu as {age} ans"
    )
### EXO4 - API with parameters retrieved from URL
@app.route('/exo4/<name>/<int:age>', methods=['GET'])
def exo4(name, age):
    """
    Récupère les paramètres directement depuis l'URL, ex: /exo4/Jean/20
    """
    # Retour JSON
    return jsonify(f"Bonjour {name}, tu as {age} ans")

### EXO5 - Search health parameters in a dictionary
@app.route('/health', methods=['GET', 'POST'])
def health():
    # Dictionnaire contenant les données de santé
    health_data = {
        "Jean": {"height": 175, "weight": 70, "blood_type": "O+"},
        "Amanda": {"height": 165, "weight": 60, "blood_type": "A-"},
        "Paul": {"height": 180, "weight": 85, "blood_type": "B+"}
    }

    if request.method == 'POST':
        # Récupérer le nom soumis via le formulaire
        name = request.form.get('name', '').strip()

        # Recherche des données pour la personne donnée
        person_data = health_data.get(name)

        if person_data:
            # Rendre la page HTML avec les données de santé
            return render_template('health.html', name=name, health_parameters=person_data)
        else:
            # Rendre la page HTML avec un message d'erreur
            return render_template('health.html', name=name, health_parameters=None, error=f"Aucune donnée de santé trouvée pour {name}")

    # Si la méthode est GET, afficher simplement la page avec le formulaire
    return render_template('health.html', name=None, health_parameters=None)

@app.route('/new', methods=['GET', 'POST'])
def new_patient():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.form.get('n', '').strip()
        address = request.form.get('add', '').strip()
        pincode = request.form.get('pin', '').strip()

        # Vérifier si les champs sont remplis
        if not name or not address or not pincode:
            return "Tous les champs sont obligatoires !", 400

        # Ajouter le patient à la base de données
        new_patient = Patient(name=name, address=address, pincode=pincode)
        db.session.add(new_patient)
        db.session.commit()

        # Rediriger vers la liste des patients
        return redirect(url_for('list_patients'))

    # Afficher le formulaire d'ajout
    return render_template('add_patient.html')

@app.route('/patients', methods=['GET'])
def list_patients():
    # Query all patients from the database
    patients = Patient.query.all()
    # Render the template and pass the patients data
    return render_template('patients.html', patients=patients)

@app.route('/search', methods=['GET'])
def search_patient():
    # Récupérer le nom depuis la barre de recherche
    name = request.args.get('name', '').strip()

    # Rechercher les patients correspondant au nom
    patients = Patient.query.filter(Patient.name.like(f"%{name}%")).all()

    # Afficher les résultats dans une table
    return render_template('patients.html', patients=patients)
<<<<<<< HEAD
=======

# Updated the names in the data_sante dictionary to Jean, Amanda, and Paul
data_sante = {
    "jean": {
        "tension": "12/8", 
        "pouls": 75, 
        "poids": 69,
        "groupe": "A+"
    },
    "amanda": {
        "tension": "11/7", 
        "pouls": 70, 
        "poids": 55,
        "groupe": "O+"
    },
    "paul": {
        "tension": "13/8", 
        "pouls": 80, 
        "poids": 62,
        "groupe": "B+"
    }
}

# 2. La route pour afficher le site web
@app.route('/sante/<nom>/<mesure>')
def consulter_sante_web(nom, mesure):
    # On cherche la personne (en minuscule pour éviter les erreurs de frappe)
    personne = data_sante.get(nom.lower())
    
    if personne:
        # On cherche la mesure précise demandée (poids, tension, pouls, ou groupe)
        valeur = personne.get(mesure.lower())
        
        if valeur:
            # On envoie les données au fichier HTML 'sante.html'
            return render_template(
                'sante.html', 
                nom=nom, 
                type_donnee=mesure, 
                valeur=valeur
            )
    
    # Message si le nom ou la donnée n'existe pas
    return f"Désolé, aucune donnée trouvée pour {nom} concernant : {mesure}", 404
>>>>>>> 54e06c0 (Initial commit for the project)
