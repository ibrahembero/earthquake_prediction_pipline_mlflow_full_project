# mlflow branch contains mlflow project with the required libs to run the mlflow which is exciting tool to track our experiments in python 🥇
# ise branch contains script made with windows powershell ise that change directory to pipeline project then execute it and we can let this script run automatically using task scheduler at specific time 🥇
# pipe branch contains pipeline project that read data, make preproccessing, train model, save it in pkl file to load it later 🥇
# django branch contains django project that involve html templates, url, views to load the model and take user input to predict and get nice result of magnitude of an earthquake 🥇
# steps to work all together ▶️
## 1. we should run mlflow project on localhost on port 5000 for example
## 2. we should run ise script that changes the directory to pipeline proejct and activate the venv then run the pipeline
## 3. ise script will run the pipeline from read dataset, preproccessing, split, training, save model to load it later in django project
## 4. django project to load the saved model (hint: you should update the path for existing model.pkl file to work correctly) and navigate to given url after activate venv and install requirements and run this command: python manage.py runserver will run on default port
## 5. navigate to website and click start it will take you to form to enter values then click predict to show result
## example of input: longitude= -28.3561, latitude= -55.7508 , depth= 10 , Timestamp= 2018-09-01T00:00:47.980Z
## Enjoy and break a leg 🥇
