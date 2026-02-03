from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/salutation', methods=['GET'])
def salutation():
    return jsonify({"message": "helloworld"})

## EXO2: API POST: renvoyer un nom fourni en parametre
@app.route('/api/utilisateurs', methods=['POST'])
def utilisateurs():
    # On récupère les données JSON envoyées par l'utilisateur
    donnees = request.get_json()
    
    # On extrait la valeur associée à la clé "nom"
    nom_extrait = donnees.get('nom', 'Nom non fourni')
    
    # On renvoie la réponse en JSON
    return jsonify({"nom_recu": nom_extrait})

if __name__ == '__main__':
    app.run(debug=True)