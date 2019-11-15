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
4. [Insert IBM Cloud Object Storage credentials](#4-insert-ibm-cloud-object-storage)
5. [Insert WML credentials](#5-insert-wml-credentials)
6. [Deploy the web app as a Cloud Foundry application](#4-deploy-the-web-app-as-a-cloud-foundry-application)
7. [Testing it!](#5-testing-it!)

### 1. Create a Watson Studio project.
* Log into IBM's [Watson Studio](https://dataplatform.cloud.ibm.com). Once in, you'll land on the dashboard.

* Create a new project by clicking `+ New project` and choosing `Data Science`:

![WS](/doc/source/images/02.png)

* Enter a name for the project name and click `Create`.

* **NOTE**: By creating a project in Watson Studio a free tier `Object Storage` service and `Watson Machine Learning` service will be created in your IBM Cloud account. Select the `Free` storage type to avoid fees.

![WS-dashboard](/doc/source/images/03.png)

### 2. Upload the dataset to IBM Cloud Object Storage

* In the right section of the dashboard...

### 3. Create the model and deploy it with jupyter notebook

* From the new project `Overview` panel, click `+ Add to project` on the top right and choose the `Notebook` asset type.

![jupyter-notebook](/doc/source/images/04.png)

* Fill in the following information:

  * Select the `From URL` tab. [1]
  * Enter a `Name` for the notebook and optionally a description. [2]
  * Under `Notebook URL` provide the following url: [https://github.com/JoaoPedroPP/Sky-Zoo/blob/master/model-jupyter/skyzoo.ipynb](https://raw.githubusercontent.com/JoaoPedroPP/Sky-Zoo/master/model-jupyter/skyzoo.ipynb) [3]
  * For `Runtime` select the `Python 3.5` option. [4]

![config-notebook](/doc/source/images/05.png)

* Click the `Create` button.

* TIP: Once successfully imported, the notebook should appear in the `Notebooks` section of the `Assets` tab.

From now on the Python Notebook is ready and can be started by clicking at the `Run` button indicated in the picture below. You can read the instructions and comments in the notebook and start executing cell by cell. If you wish, you can select the first cell by clicking on it run each cell individually pressing `shift+enter` on your keyboard,

![running-notebook](/doc/source/images/06.png)

To be able to run the entire jupyter notebook, two steps are required: insert the credentials for IBM Cloud Object Storage and WML.

### 4. Insert IBM Cloud Object Storage credentials

This step is required for we be able to download the data from IBM Cloud Object Storage for train and test our model. We can do that using the API avaible for this service and manipulating it through the specifically library.

In the indicated cell at the picture below, you must fufil the `cos_credentials` varaible with your IBM Cloud Object Storage credentials.

![cell-OS](/doc/source/images/07.png)

The easy way to insert the credentials is firts click at the indicated button in the top right corner of the screen and browser for 

### 5. Insert WML credentials
### 6. Deploy the web app as a Cloud Foundry application
### 7. Testing it!