from flask import Flask, request
from doPost import doPost

app = Flask(__name__)

@app.route('/api/doPost', methods=['POST'])
def handle_doPost():
    return doPost(request.data)

if __name__ == '__main__':
    app.run()
