from watson_machine_learning_client import WatsonMachineLearningAPIClient
from flask import Flask, render_template, request, json, jsonify, send_from_directory
import os
import json
import numpy as np
import io
from PIL import Image
# from flask_cors import CORS O # Somente para evitar erros de CORS durante desenvolvimento local

app = Flask(__name__, static_folder="./public", static_url_path='')
app.config.from_object(__name__)
port = int(os.getenv('PORT', 8080))

# CORS(app) # Somente para desenvolvimento local

wml_credentials = {
  "your_credentials": "here"
}

@app.route("/", methods=['GET'])
def hello():
    error=None
    return send_from_directory('public', 'index.html')

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