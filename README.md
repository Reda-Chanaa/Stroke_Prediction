Group : Reda CHANAA et Kévin IBARES

github : https://github.com/Reda-Chanaa/Stroke_Prediction

Dataset: https://www.kaggle.com/fedesoriano/stroke-prediction-dataset

Goal of the project : The goal of this project was to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relavant information about the patient. After analyzing data and comparing and selecting with the package Pycaret the most suitable models for our problem, we built a pipeline using kedro and monitored our models using MLFlow.


Project Plan : 

I.Analyzing Data and Model Selection

	1st. Kevin works on the data, performs an EDA and first processings steps.
	2nd.Kevin Compares multiple models and select the ones that seems the more promising regarding our goal (efficiently predict if a patient is likely to get stroke).

II.Model deployment and monitoring 

	3rd.Reda builds the data engineering pipeline for data processing using Kedro.
	4th.Reda builds Data Science Pipeline
	5th.Reda deploys the selected models and monitors them using MLFlow.


Most of the challenge of this project was dealing with the imbalanced dataset, and thus achieving good results when training and fitting models.
