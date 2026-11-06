---
date: 2026-11-06
tags: [interview, recherche, M0007, 1RR, harnais, genese]
session: F01
mandat: M0007
niveau: N2
verdict: non-revu
---

# M0007 — Interview « genèse du harnais » : recherche complémentaire 1RR → harnais

Lecture seule sur `/Users/malik/Documents/1RR` et `/Users/malik/Documents/orchestration`. Aucun code, aucun commit hors `vault/`. Résultats détaillés et citations : `interviews/genese-harnais/01-sources.md`, section « Recherche complémentaire (M0007, 06/11) » (fichier non suivi, non commité).

Gardes : `main` = `origin/main` = `ee1f429f320e3cca099937b1091b62b27363cf39` ; branche `main` ; `01-sources.md`, `04-transcript.md`, `05-debrief.md` présents. Toutes passées.

## Résultats

### 1. Bureaux

- B1 : première signature `f2ac7e4` (23/08, B1F3). B1F4 et B1F1 : 24/08 et 25/08, selon `01-sources.md` (non re-vérifiés ici).
- B2 : première trace `18da646` (02/09), suivie de `0952806`, `6c38a6a`, `f5e50f2`, `2d93bfe`, tous 02/09.
- B3 : 0 occurrence dans les sujets de commit 1RR.
- Fenêtres par bureau (occurrences dans les sujets, non un décompte de sessions) : B1F1 21, B1F2 32, B1F3 12, B1F4 14 ; B2F1 5, B2F2 3, B2F3 2, B2F4 2.
- Dernières mentions B1Fx/B2Fx avant `Fxx` : 06/09 (`d0d16a2`, `ae839fe`, `af01e9a`, `1488b21`). La mention postérieure `28614a1` (02/10, M0459) liste des fichiers archivés : pas une activité.
- Premier `Fxx` : `4d9af72` (06/09, F02), puis `05ea09d` (F03, 06/09).

### 2. 1RR, 06/09 au 22/09

- 06/09 : nomenclature `Fxx`, bloc de lancement unique (`historique.md`, note V1.10 ; `4d9af72`).
- 07/09 : SKILL.md V1.10 et V1.11 (`f4d25a2`). 08/09 : V1.12 garde horloge, V1.14-V1.15 (`bf39994`, `c811360`).
- 12/09 : V1.16, interdiction de git-écriture de l'orchestrateur violée en pratique (`changelog.md:50`).
- 13/09 : V1.20, découpage du skill (`efc589b`). 15/09 : V1.22, une seule session d'orchestration par projet (`changelog.md:56`).
- 18/09 : superviseur V3, lancement et fin de fenêtre cmux par script (`4520fd2`, revue `519f3fa`). Verbatim Malik 09h59 : « Ce qu'il me faudrait, c'est que je ne sois plus nécessaire » (`historique.md:915-935`). Hooks via `--settings` (`68c71e8`). Fichier `vault/decisions/2026-09-18-superviseur-v3-bureau-autonome.md` : premier commit `c41f8a3`.
- 18/09 : commit `da5b7df` « orchestration-bureau V2.0 -- refonte parent, superviseur par defaut », daté 18/09. Le changelog donne V2.0 au 19/09 (M0272, `changelog.md:60-61`). Voir Contradictions.
- 19/09 : superviseur 1RR `VERSION = '1.0.4'` (`INVENTAIRE.md:33`, côté orchestration).
- 21/09 : décision de cadre « Du harnais qui se souvient au harnais qui empêche » (`8e1f2e9`) : 95 leçons en prose, 3 gardes exécutables. Le document cite « Barcelone » (l.9).
- 22/09 : superviseur 1.0.4 activé (`60c7250`), garde `sortie-sans-rendu` (`43869d8`).

### 3. Contrôle de la commande de lancement

- 1RR, premier refus `LANCEMENT_REFUSE liste-blanche` (modele/effort hors liste) : `4520fd2`, 18/09, documentation superviseur.
- 1RR, `commande-invalide` : première trace `3bfba82` (14/10, mise à jour harnais v1.3.0 → v1.4.3). Présent à `references/gabarits.md:41` à HEAD.
- 1RR, `sonet` : aucune occurrence dans l'historique. La capture du 24/08 reste la seule source.
- Orchestration, premier refus `liste-blanche` : `a4af137`, 22/09, `SKILL-orchestration-maison/SKILL.md` diff l.141-142.
- Orchestration, contrôle structurel `controlerCommande` : `superviseur/lancement.mjs:162`.
- Orchestration, retrait du contrôle du modèle : `ce9af8e`, 12/10 (M0266). `superviseur/lancement.mjs:82-84` : « le choix du modèle et de l'effort n'est plus jugé ici (plus de refus `liste-blanche`). Seule la FORME est contrôlée. »

### 4. La décision d'extraire

- Aucune source ne donne la raison. `e235da7` (22/09) décrit la méthode d'inventaire, pas le motif.
- `INVENTAIRE.md:1-10` : statut `a-valider-par-malik`, sans motif.
- `README.md` d'orchestration : « extrait après coup d'un projet réel… puis vidé ». Il décrit l'état, pas la décision.
- Contexte le plus proche, sans lien écrit : `8e1f2e9` (21/09) et `60c7250` / `43869d8` (22/09).
- qmd `harnais-vault`, « pourquoi le harnais a été extrait de 1RR » : aucun passage pertinent.

## Trous

- Nombre de bureaux, date du troisième (B3 absent de 1RR).
- Geste manuel de lancement et copier-coller : aucune trace 1RR.
- « Va lire ton prompt… » : première trace 1RR `8ca28be` (27/08). La capture du 23/08 reste sans source écrite.
- Motif de l'extraction (22/09) et motif du retrait du contrôle du modèle (12/10).

## Contradictions avec `05-debrief.md` et `01-sources.md`

1. Débrief : « seul B1 est attesté ». Faux : B2 est attesté (F1-F4) dès le 02/09. Seul B3 manque.
2. Débrief : le contrôle strict de la commande « viendra plus tard ». Attesté dès 18/09 (1RR) et 22/09 (orchestration), puis assoupli le 12/10 : seule la forme est contrôlée.
3. `01-sources.md` : « Barcelone » non attesté. `vault/decisions/2026-09-21-harnais-lecon-vers-garde-executable.md:9` (1RR) le cite. La recherche de `01-sources.md` ne couvrait que le dépôt orchestration.
4. `01-sources.md` : V2.0 le 19/09. Le commit `da5b7df` est daté 18/09. Le changelog dit 19/09 (M0272). À trancher.

## Décisions prises en cours de mandat

- Recherche 1RR par `git log`/`grep` : pas de collection qmd pour 1RR (conforme au mandat).
- Aucun sous-agent lancé. Aucune revue indépendante (mandat : pas de relecture).
- Commit du vault sur `main` (chemins `vault/` seulement), puis push, conformément à `git.pousser_vault: true`.

## Preuves

- Gardes : `git rev-parse main origin/main` (deux fois `ee1f429…`), `git branch --show-current` = `main`.
- Commandes de recherche : `git --no-optional-locks log/show/grep` sur 1RR et orchestration, et `qmd query` sur `harnais-vault`.
