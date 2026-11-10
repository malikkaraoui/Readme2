# scripts/ -- commandes et pièges

## Commandes
- Contrôle de taille et de largeur d'un ref, lecture seule : `sh "$(git config core.hooksPath)/pre-commit" --controle <ref> [--base <ref>] [--lignes]`
- Chaque ligne fautive, détaillée : `sh "$(git config core.hooksPath)/pre-commit" --controle --lignes`
- Limite d'un seul commit, sans trace versionnée : `ROTATION_LIMITE=<octets> git commit ...`

## Pièges
- `pre-merge-commit` refuse le merge si `pre-commit` n'est pas exécutable : `chmod +x` avant.
- `core.hooksPath` est relatif : les commandes ci-dessus se lancent depuis la racine du dépôt, pas depuis `scripts/`.
- `pre-commit` lit la config dans git, pas sur le disque : une config présente au disque mais absente de l'index (`HARNAIS_CONFIG` compris) ne compte pas, ce sont les défauts, avec une ligne sur stderr. `git add` d'abord.
- `commit-msg` et `pre-push` lisent la config sur le disque : une modification non committée s'y applique tout de suite.
- `ROTATION_LIMITE` invalide (zéro en tête, non numérique, plus de 9 chiffres) : la limite de la config s'applique, sinon 80000 octets, avec une ligne sur stderr.
- `INSTRUCTIONS_MAX_CARACTERES` qui relève le seuil : une ligne sur stderr, rien ne le trace dans le dépôt.
- `TRAILERS_RETIRES` défini mais vide : rien n'est retiré du message de commit.
- `commit-msg` sort toujours 0 : un trailer manquant ne bloque jamais un commit.
- `--controle` sort 2 hors d'un dépôt git ou si la ref est introuvable ; 1 signifie `BLOQUE`.
- Un merge en avance rapide ne lance aucun hook : le filet est `--controle --base`.
- Le plafond N1 de `pre-push` exige git 2.40 ou plus ; en dessous, le push est refusé avec un message.
