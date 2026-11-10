# scripts/ -- commandes et pièges

## Commandes
- Contrôle de taille et de largeur d'un ref, lecture seule : `sh "$(git config core.hooksPath)/pre-commit" --controle <ref> [--base <ref>] [--lignes]`
- Chaque ligne fautive, détaillée : `sh "$(git config core.hooksPath)/pre-commit" --controle --lignes`
- Limite d'un seul commit, sans trace versionnée : `ROTATION_LIMITE=<octets> git commit ...`

## Pièges
- `pre-merge-commit` refuse le merge si `pre-commit` n'est pas exécutable : `chmod +x` avant.
- Une config présente sur disque mais absente de l'index n'est pas lue (`HARNAIS_CONFIG` compris) : ce sont les défauts. `git add` d'abord, sinon ligne sur stderr.
- `ROTATION_LIMITE` invalide (zéro en tête, non numérique, plus de 9 chiffres) : limite par défaut, avec une ligne sur stderr.
- `INSTRUCTIONS_MAX_CARACTERES` qui relève le seuil : une ligne sur stderr, rien ne le trace dans le dépôt.
- `TRAILERS_RETIRES` défini mais vide : rien n'est retiré du message de commit.
- `commit-msg` sort toujours 0 : un trailer manquant ne bloque jamais un commit.
- `--controle` sort 2 hors d'un dépôt git ou si la ref est introuvable ; 1 signifie `BLOQUE`.
- Un merge en avance rapide ne lance aucun hook : le filet est `--controle --base`.
- Le plafond N1 de `pre-push` exige git 2.40 ou plus ; en dessous, le push est refusé avec un message.
