import firebase_admin
from firebase_admin import credentials, auth

config = {
  'apiKey': "AIzaSyB4D4mZeuXfT1fSCqpkSljotPWh3YfjCGY",
  'authDomain': "projetoflask-fb.firebaseapp.com",
  'databaseURL': "https://projetoflask-fb-default-rtdb.firebaseio.com",
  'projectId': "projetoflask-fb",
  'storageBucket': "projetoflask-fb.appspot.com",
  'messagingSenderId': "134324160615",
  'appId': "1:134324160615:web:8ed0bb84526c5c146b6cc2",
  'measurementId': "G-ZVZ9B7PQP3"
};

config = credentials.Certificate("C:\\Users\\ALUNO\\Downloads\\Nova pasta\\projetoflask\\chave_auth.json")
firebase_admin.initialize_app(config)