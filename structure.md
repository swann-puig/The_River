Structure du code
==

Pour ce projet j'ai choisi un modèle MVC (Modèles Vue Contrôleur).

La légende pour ce fichier est :

_attribut_
- méthode

Librairies utilisés
-
**Graphique:**
 Pygame

**Réseau:**
 Socket
 
 Liens utile
 -
 
 Install librairie dans le script : https://stackoverflow.com/questions/12332975/installing-python-module-within-code
 
 Pygame: https://www.pygame.org/docs/py-modindex.html
 
 Socket: https://stackoverflow.com/questions/12332975/installing-python-module-within-code

# Contrôleur

Contrôle/effectue toutes les interactions avec les objets, active les fonctions d'affichage de la vue.

Tous les objets doivent avoir un attribut qui est le contrôleur.

_vue_

_main_

_terrain_

_deck normale_

_deck action_

_liste des cartes sur le terrain_

_liste des cartes non traversable_

_joueur_

_adversaire_

- Commencer la partie
- Piocher carte normale
- Piocher carte action
- Placer une carte sur le terrain
- Déplacer une carte sur le terrain
- Mode déplacement
- Déplacement validé
- Placer piège
- Utiliser carte magique
- Utiliser carte action
- Sélectionner carte
- Désélectionner
- Confirmation d'attaque
- Attaquer carte adverse
- Fin du tour
- Vérifier collision à (x,y)
- Update (actualise les infos affichés, les effets des cartes)

# Vue

La vue reçois uniquement les élément à afficher par le contrôleur (en argument dans les méthodes).

La vue gère aussi les intéractions de l'utilisateur avec l'interface.

Les cartes dans la main sont représenté en tout petit en bas de l'écran, le passage de la souris dessus permet de voir les détailles.

**Code couleur:**
 Gris: carte créature;
 Bleu: carte magique;
 Rouge: carte piege;
 Vert: carte action;
 Jaune: carte sélectionné

_controleur_

_carte sélectionné_

_TOUTES LES POSITIONS, ZONES CONSTANTES_

- Afficher le background
- Afficher le plateau de jeu
- Afficher les deck de cartes
- Afficher la main
- Afficher informations
- Ajouter une carte à la main
- Carte sélectionné
- Désélectionner
- Clic gauche enfoncé / Clic gauche laché sur une carte de la main
- Clic droit enfoncé sur une carte de la main
- Souris déplacé
- Afficher détaille de la carte
- (Bouton suivant sélectionné / Bouton précédent sélectionné)
- (Molette de la souris avant / Molette de la souris arrière)
- Carte suivante
- Carte précédente
- Clic sur le terrain
- Afficher grillage de déplacement

# Modèles

Les modèles sont tous les objets du jeu.

Si un objet a besoin de faire une action qui implique d'autres objets, il doit passer par le contrôleur.

Si un objet doit effectuer une action/vérification tout le temps ou à des momant précis, il doit le mettre dans la fonction "update" qui est appelé à chaque bouvle du main.

### Main

_controleur_

_liste carte_

- Ajouter carte
- Retirer carte
- Obtenir carte
- Obtenir carte triée

### Joueur

_controleur_

_deck normal_

_deck action_

_main_

_chateau_

_nom_

_point de vie_

_point d'action_

_couleur_

- Piocher carte normale
- Piocher carte action
- Placer carte créature
- Utiliser carte magique
- Placer carte piège
- Uiliser carte action
- Perdre points de vie
- Gagner points de vie
- Update

### Deck

_controleur_

_nom_

_liste des cartes_

- Mélanger
- Piocher
- Chercher
- Retirer
- Filtrer par type
- Filtrer par nom
- Filtrer par famille

### Adversaire

_controleur_

_nom_

_nombre de carte en main_

_couleur_

_point de vie_

- Placer une carte

### Terrain

_controleur_

_image_

_dimension_

_nombre de case_

_zones interdites_

_liste des cartes_

_chateau1_

_chateau2_

- Obtenir position dans grille
- Case libre dans x,y
- Placer une carte
- Retirer une carte

### Carte

**Objet graphique**

_controleur_

_nom_

_famille_

_type_

_propriétaire_

(_image_)

_traversable_

_couleur_

- Déplacer
- Est dans les coordonnées x,y
- Afficher
- Cacher
- Destroy
- Update

### Carte créature

**Carte**

_stats de base (lors de la création)_

_puissance_

_déplacement_

_porté d'attaque_

_cartes équipées_

_capacité_

- GetXXX (avec les bonus inclues)
- Perdre point de vie
- Gagner point de vie
- Attaquer
- Activer effet passif (essaie sans arret de déclancher l'effet)
- Activer effet actif
- Update

### Carte magique

_puissance supplémentaire_

_vie chateau supplémentaire_

_déplacement supplémentaire_

_porté d'attaque supplémentaire_

_poid_

_nom effet_

- GetXXX

### Carte piège

_dégats_

_porté d'attaque_

_poid_

_nom effet_

- GetXXX

### Carte action

_point d'action_

_nom effet_

- GetXXX

### Fonction Effet

Prend en paramettre le **nom de l'effet**, **le nom du contexte** et optionnellement **les éléments impliqué dans le contexte**.

Retourne ...

- Vérifier activation
- Activer
