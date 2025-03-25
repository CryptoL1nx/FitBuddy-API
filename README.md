# Fit Buddy API
---
## NEXT STEPS !
* recevoir donnees bruts et analysées

* pouvoir renvoyer les deux a l'utilisateur

* api fonctionnel avec les données de elias
via aws IoT C ore quils puissent nous envoyer des données
créer bdd pour toutes les données brutes + analysées


##### BDD:
2 TABLES
- accélérations etc
- besoins de elias
- besoins des traitements de données

important : bon flux de données sur les données traitées (toutes les x)

envoi contsant a la Raspberry et la Raspberry decide d'envoyer tous les x selons plusieurs facteurs (ex possibles : mouvement activé etc)

* Faire une interface pour le showroom !! (1h environ pour mettre) --> quelques rep et hop ça s'affiche sur l'interface!

## Installation
```sh
pip install -r requirements.txt
```

Il faut aussi installer Mosquitto en local.
On peut télécharger Mosquitto depuis le [lien officiel](https://mosquitto.org/download/)
* lancer l'installateur et cocher "Install Service"
* ouvrir une invite de commande en mode adminstrateur
```sh
net start mosquitto
mosquitto -v
```
Si tout est ok, vous verrez MQTT démarrer et écouter sur localhost:1883 .

Il est possible que vous deviez ajouter Mosquitto au PATH si ça ne marche pas.
* ouvrir l'explorateur de fichiers
* aller dans C:\Program Files\mosquitto\ et copier le chemin
* Win + R --> taper sysdm.cpl --> Avancé --> Variables d'environnement
* Dans Variables système --> Path --> Modif --> Ajouter (C:\Program Files\mosquitto\ et coller le chemin)
* redémarrer le terminal et tester 
```sh
mosquitto -v
```

## Démarrer l’API
Après avoir installé toutes les dependances vous pouvez lancer le projet.

```sh
docker-compose build
```
Puis,
```sh
docker-compose up
```

L'API peut crasher si les modules sont manquants sur le container. Il faut donc les installer directement dans le container.


```sh
docker build -t fitbuddy_api .
docker rm fitbuddy_api
docker run --name fitbuddy_api -d -p 8000:8000 fitbuddy_api
```
Verifier que le conteneur tourne :
```sh
docker ps
```
Et vérifier les logs si des erreurs persistent
```sh
docker logs fitbuddy_api
```
Accède au conteneur :
```sh
docker exec -it fitbuddy_api bash
```
Et installe les modules dont tu as besoin avec :
```sh
pip install #puis nom du module
```
Sors du conteneur et redémarre le :
```sh
exit
docker restart fitbuddy_api
```

API disponible sur [(http://localhost:8000/docs)](http://localhost:8000/docs)

## Lancer les tests
### Avec pytest
```sh
pip install pytest
pytest -v
python -m pytest tests/
```

## Fermer proprement le projet FitBuddy API
Pour arrêter proprement tous les services Docker (API, base PostgreSQL, Mosquitto) et s’assurer qu’aucun processus ne reste actif :

```sh
docker-compose down
```