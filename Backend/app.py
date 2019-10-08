from watson_machine_learning_client import WatsonMachineLearningAPIClient
from flask import Flask, render_template, request, json, jsonify, send_from_directory
# from flask_cors import CORS
import os
import json
import numpy as np
import io
from PIL import Image

app = Flask(__name__, static_folder="./public", static_url_path='')
app.config.from_object(__name__)
port = int(os.getenv('PORT', 8080))

# CORS(app)

wml_credentials = {
  "apikey": "p5INbMkXdfG-qLYDVnk_ROeX6CGnO4ZjWvCRe8Aqd0FJ",
  "iam_apikey_description": "Auto-generated for key 90ed576d-3d65-4183-85bb-87540d858eb5",
  "iam_apikey_name": "wdp-writer",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/5086f0d78cb04b3aabd7b046c5c84a10::serviceid:ServiceId-b8bc4703-8080-450e-b22d-796a604e677f",
  "instance_id": "a8f286bb-6e41-4ddf-a97b-340ffcd6d33e",
  "password": "33a1cc1e-1158-4486-924c-48e086ad159b",
  "url": "https://us-south.ml.cloud.ibm.com",
  "username": "90ed576d-3d65-4183-85bb-87540d858eb5"
}

@app.route("/", methods=['GET'])
def hello():
    error=None
    # return render_template('index.html', error=error)
    return send_from_directory('public', 'index.html')
    # return make_response(open('./public/index.html').read())

def prepare_image(image):
    image = image.resize(size=(96,96))
    image = np.array(image, dtype="float") / 255.0
    image = np.expand_dims(image,axis=0)
    image = image.tolist()
    return image

@app.route('/predict', methods=['POST'])
def predict():
    print(request)
    image = request.files["image"].read()
    image = Image.open(io.BytesIO(image))
    image = prepare_image(image)

    # Faça uma requisição para o serviço Watson Machine Learning aqui e retorne a classe detectada na variável 'resposta'
    client = WatsonMachineLearningAPIClient(wml_credentials)
    ai_parms = { "wml_credentials" : wml_credentials, "model_endpoint_url" : "https://us-south.ml.cloud.ibm.com/v3/wml_instances/a8f286bb-6e41-4ddf-a97b-340ffcd6d33e/deployments/aab63322-d564-477b-b8ea-731a139bd547/online" }
    model_payload = { "values" : image }
    model_result = client.deployments.score( ai_parms["model_endpoint_url"], model_payload )
    data = model_result

    classes = ['ELEFANTE', 'GIRAFA', 'LEAO']
    index = data['values'][0][0].index(max(data['values'][0][0]))
    print(data)

    resposta = {
        "class": classes[index]
    }
    return resposta

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)