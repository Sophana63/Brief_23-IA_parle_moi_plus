# Brief 21 - Projet de reconnaissance vocale avec OpenAI

Ce projet est une démonstration de l'utilisation de l'API OpenAI pour améliorer la reconnaissance vocale avec SpeechRecognition.

## Diagramme de Gantt

Vous pouvez le trouver avec  [ce lien](https://docs.google.com/spreadsheets/d/1U7PahCY9NehvHT8dV7NhH_jdbRzrr0N1pgEKsDt4Lks/edit#gid=1115838130).

## Installation

Pour installer les dépendances nécessaires, utilisez la commande suivante :

```
pip install -r requirements.txt
```
Fichier [requiements.txt](https://github.com/Sophana63/Brief_23-IA_parle_moi_plus/blob/master/requirements.txt)

A la racine du projet, créer un nouveau fichier .env et y mettre :
``` 
OPENAI_API_KEY=votre_api_key
```

Ensuite, pour lancer l'application, vous pouvez appuyer le bouton lecture de VS Code lorsque vous êtes sur le fichier main.py ou vous pouvez utiliser la commande suivante :
```
python main.py
```

## Utilisation

Pour utiliser l'application, rendez-vous sur http://localhost:5000/ dans votre navigateur web. Cliquez sur le bouton "Parlez maintenant" et parlez dans votre microphone. Une fois que vous avez fini de parler, l'application affichera le texte reconnu ainsi qu'une réponse générée par l'API OpenAI.

## Personnalisation

Si vous voulez personnaliser la grammaire utilisée pour la reconnaissance vocale, vous pouvez modifier le fichier grammar.txt et test.py. Cette partie est en cours de test.

Si vous voulez personnaliser la réponse générée par OpenAI, vous pouvez modifier le code dans la fonction recognize() de main.py.


# Partie 1 

Dans le dossier `projet1`, lancer le fichier test.py et parler avec votre microphone dans le terminal.
Voici les paramètres à modifier pour pouvoir le lancer :
``` python
# Configure OpenAI API
openai.api_key = "votre_key"

# Configure Azure Speech Services
speech_config = speechsdk.SpeechConfig(
    subscription="votre_key",
    region="votre_region"
)
```

