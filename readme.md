```
_|_|_|                                                    
_|    _|  _|  _|_|    _|_|    _|_|_|      _|_|    _|  _|_|
_|_|_|    _|_|      _|    _|  _|    _|  _|_|_|_|  _|_|    
_|        _|        _|    _|  _|    _|  _|        _|      
_|        _|          _|_|    _|_|_|      _|_|_|  _|      
                              _|                          
                              _|                                            

        _|_|_|_|_|                                
            _|      _|    _|  _|_|_|      _|_|    
            _|      _|    _|  _|    _|  _|_|_|_|  
            _|      _|    _|  _|    _|  _|        
            _|        _|_|_|  _|_|_|      _|_|_|  
                          _|  _|                  
                      _|_|    _|
```
                    
# Propertype

Machine a ecrire, de la typographie generative.


Fichier | Dependances | Description
--------|-------------|------------
read.py| collections, sys, time | lit l'input.txt et deduit des variables et constantes
curves.py|aucune| liste des fonctions qui dessinent les courbes de bezier en svg
draw-main.py| read, curves | rassemble les variables de read et les fonctions de curves

a faire :
- nettoyer toutes les lettres
- retirer les metas inutiles
- deduire des coordonnees variables et des dimensions basiques
- algorithme qui redistribue intelligemment les variables
- reappropriation des variables par les fonctions

problemes a resoudre :
- ~~sortie de la liste lue~~
- reparation de la courbe ouest-sud
- debug et catching exceptions
- gestion MEP et PDF
- gestion interface


rajout du dossier typo strokefont

###### Pour compter les listes de mots :

```python
from collections import Counter
import re

reg = re.compile('\S{4,}')

s = "hello this is hello this is baby baby baby baby hello"
c = Counter(ma.group() for ma in reg.finditer(s))
print c
```
[source](http://stackoverflow.com/questions/15238276/ddg#15238332)
