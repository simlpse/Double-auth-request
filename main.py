from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)

@app.route('/doPost', methods=['POST'])
def doPost():
    # Récupérer les données envoyées par le raccourci
    request_data = request.get_json()
    link = request_data['link']
    header = request_data['header']
    content = request_data['content']

    # Effectuer la requête POST
    response = requests.post(link, headers=header, data=content)

    # Récupérer les en-têtes et le contenu de la réponse
    response_headers = response.headers
    response_body = response.text

    # Renvoyer les en-têtes et le contenu de la réponse au raccourci
    responseData = {
        'headers': dict(response_headers),
        'body': response_body
    }

    return jsonify(responseData)

if __name__ == '__main__':
    app.run(debug=True)
