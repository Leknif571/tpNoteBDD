# BOUKADA Adel - TP note BDD
# Pour démarrer le projet
# 1. Installer les dépendances
```
pip install -r requirements.txt
```
## Ou manuellement
    pip install behave
    pip install selenium
    pip install webdriver-manager

### N'oublier pas d'installer le driver chrome disponible ici: https://chromedriver.chromium.org/downloads
# 2. Taper la commande suivante pour lancer les tests:
```
behave
```

### Pour tester un scénario particulier 
```
behave path/to/feature
```
### Exemple
```
behave features/change_secruity_level_after_connect.feature
```

# 3. Pour créer un nouveau scénario, il faut créer un fichier .feature dans le dossier features et y ajouter le scénario en Gherkin.

## Pour créer un nouveau step, il faut créer un fichier .py dans le dossier features/steps et y ajouter le step en python.
## Lancer la commade :
```
behave features/mon_feature.feature
```
Cela générera un code de base pour le step dans le fichier features/steps/mon_feature.py a copié et coller dans ce même fichier et à compléter.