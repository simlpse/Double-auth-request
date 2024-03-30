exports.handler = async function(event, context) {
  // Extraire les données de la requête
  const { url, headers, content } = JSON.parse(event.body);

  try {
    // Effectuer la requête POST
    const response = await fetch(url, {
      method: 'POST',
      headers: headers,
      body: content
    });

    // Extraire les en-têtes de la réponse
    const responseHeaders = {};
    for (let [key, value] of response.headers) {
      responseHeaders[key] = value;
    }

    // Lire le contenu de la réponse
    const responseBody = await response.text();

    // Renvoyer les en-têtes et le contenu de la réponse
    return {
      statusCode: 200,
      body: JSON.stringify({
        headers: responseHeaders,
        body: responseBody
      })
    };
  } catch (error) {
    // En cas d'erreur, renvoyer un message d'erreur
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message })
    };
  }
};
