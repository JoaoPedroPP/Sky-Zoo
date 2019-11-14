# Sky-Zoo

This code pattern seeks to demostrate how easy is to create a deep learning model in IBM Watson Studio and export it to Watson Machine Learning Service(WML), making the model acessible though an API request. This pattern also provides a web application that receive an image as input, prepare and send it to to the model hosted on WML, once the models the returns a prediction of the image the app displays the calssification of the input.

Image classification has long been a challenge for Artificial inteligence(A.I). Identify animals in an image can be a funny way to prove concepts related to classification problems and extractation of correct features from an image. And also provides a nice first step to dive in A.I world.

At the end of this Code Pattern the reader will be able to understand hot to:
* Use Jupyter Notebooks in Watson Studio;
* Train, test and deploy a deeplearning model;
* Interact with IBM Cloud Obejct Storage to store the dataset;
* Use a Cloud Foudry application to create a web app to consume the model in  WML.

## Flow

1. Get the images to compse the dataset, it is strongly recommended to use this python library [google-images-download](https://github.com/hardikvasa/google-images-download). In the repository there is a section explaining how to use.
1. Create a Watson Studio project.
2. Assign a Cloud object storage to it.
3. Upload the dataset to IBM Cloud Object Storage
4. Run the jupyter notebook
5. Deploy the web app
6. Use the 

## Steps

1. [Create a new project in Watson Studio](#1-create-a-new-project-in-Watson-studio)
2. [Upload the dataset to IBM Cloud Object Storage](#2-upload-the-dataset-to-IBM-Cloud-Object-Storage)
3. [Create the model and deploy it with jupyter notebook](#3-create-the-model-and-deploy-it-with-jupyter-notebook)
4. [Deploy the web app as a Cloud Foundry application](#4-deploy-the-web-app-as-a-cloud-foundry-application)
5. [Testing it!](#5-testing-it!)

### 1. Create a Watson Studio project.
### 2. Upload the dataset to IBM Cloud Object Storage
### 3. Create the model and deploy it with jupyter notebook
### 4. Deploy the web app as a Cloud Foundry application
### 5. Testing it!