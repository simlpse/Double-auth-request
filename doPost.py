import json
import requests


def doPost(request):
    # Converti la chaîne JSON en objet Python
    request_data = json.loads(request)
    link = request_data['link']
    header = request_data['header']
    content = request_data['content']

    # Effectue la requête POST
    response = requests.post(link, headers=header, data=content)

    # Récupère les en-têtes et le contenu de la réponse
    response_headers = response.headers
    response_body = response.text

    # Renvoie les en-têtes et le contenu de la réponse sous forme de dictionnaire
    responseData = {
        'headers': dict(response_headers),
        'body': response_body
    }

    # Converti le dictionnaire en chaîne JSON avant de renvoyer
    return json.dumps(responseData)


