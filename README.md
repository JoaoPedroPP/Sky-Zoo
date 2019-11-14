# Sky-Zoo

This code pattern seeks to demostrate how easy is to create a deep learning model in IBM Watson Studio and export it to Watson Machine Learning Service(WML), making the model acessible though an API request. This pattern also provides a web application that receive an image as input, prepare and send it to to the model hosted on WML, once the models the returns a prediction of the image the app displays the calssification of the input.

Image classification has long been a challenge for Artificial inteligence(A.I). Identify animals in an image can be a funny way to prove concepts related to classification problems and extractation of correct features from an image. And also provides a nice first step to dive in A.I world.

At the end of this Code Pattern the reader will be able to understand hot to:
* Use Jupyter Notebooks in Watson Studio;
* Train, test and deploy a deeplearning model;
* Interact with IBM Cloud Obejct Storage to store the dataset;
* Use a Cloud Foudry application to create a web app to consume the model in  WML.