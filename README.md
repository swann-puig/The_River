Règles du jeu de carte
==

Le jeu est en mode tour par tour.

On dispose de carte de différents types (créature, magique, piège) dans notre main.
Les cartes peuvent être posée et déplacé sur le plateau de jeu.
Le plateau de jeu est similaire à une grande grille quadrillé, les cartes se posent sur les cases de la grille.

Le but est de détruire le "château" adverse à l'opposé de son propre "château" en traversant le plateau.

Les déplacement sont gérés par des points d'actions, chaque action prend 1 point d'action dont le déplacement. (sauf poser des cartes)
Les carte ne peuvent que être poser dans son propre camp autour du château.

Chaque tour on peut piocher une carte action et une carte normal.

# Installer le projet The River (Windows / Linux / (iOS))

Il faut en premier télécharger Python 3.7+ (https://www.python.org/downloads/) **Cochet l'option "add to PATH"** au début de l'installation.

Une fois Python installé suivre les étapes suivantes:

Avec l'application **GitHub Desktop** avec un compte GitHub :
-

Avec cette méthode la modification est possible (si droits de modifs possédés).

- Télécharger l'application
- Aller dans **File > clone repository**
- S'authentifier
- Sélectionner le répertoire **The_River** puis **clone**

Avec l'application **GitHub Desktop** sans compte GitHub :
-

Avec cette méthode aucune modification n'est possible.

- Télécharger l'application
- Aller dans **File > clone repository**
- Sélectionner l'onglet URL
- Coller l'URL du git: https://github.com/swann-puig/The_River.git
- Clone

Sans rien... :
-

Cliquer sur le bouton vert **clone or download** et télécharger en .ZIP

Une fois The_River cloné/téléchargé :
-

Ouvrir le dossier **The_River** puis lancer le fichier **auto_install.py** avec python (Ouvrir avec... > Plus d'application > Python).

Exécuter **main.py** et FINI!!

# Gameplay (version actuel)

Il n'y a pas de "partie" actuellement développé.

On peut piocher des cartes depuis les deux decks en haut de l'écran. Les cartes piochés se trouvent dans notre main en bas de l'écran sous forme d'image.

En survolant une carte avec la souris, on peut voir ses détails comme son nom et sa famille (pas nécessairement) en haut de la carte et la description. En bas de la carte, pour une créature, se trouve dans l'ordre: la puissance (power), les points de mouvements (M), la portée d'attaque (R) et la capacité d'équipement (C).

On peut placer une carte sur le plateau de jeu dans sa zone de placement/invocation en vert en la glissant avec la souris dessus (drag and drop). Ensuite la même action se fait pour déplacer la carte sur le plateau.

Un mauvais placement de la carte la fera revenir à son emplacement d'origine.
