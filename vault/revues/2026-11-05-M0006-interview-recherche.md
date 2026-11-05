---
date: 2026-11-05
tags: [interview, recherche, M0006, genese-harnais]
session: F01
mandat: M0006
statut: rendu-partiel
---

# M0006 — Recherche documentaire, interview « genèse du harnais » (phase 2, lecture seule)

## Préconditions

- `main` et `origin/main` = `b775f6a7522c908080e71f9f442086cf3701415b` : OK.
- Branche courante `main` : OK.
- `interviews/genese-harnais/` contient `00-framing.md` (`status: done`) et `01-sources.md` : OK.

## Ce qui a été fait

- Recherche qmd : collections `harnais-vault` et `harnais-code`. Pas de collection 1RR dans qmd ; 1RR lu par `git log` et grep ciblé.
- `interviews/genese-harnais/01-sources.md` : complété, contenu précédent conservé, deux lignes fausses corrigées (heure UTC du 22/09 ; 19/09 qui ne vaut que pour SKILL.md V2.3). Frontmatter `status: draft` (raison en tête du fichier).
- Source 1RR `historique.md` et `changelog.md` : absents du dépôt depuis le commit `115b888` (04/10). Lus dans la version `115b888^` par `git show`.
- Aucune écriture dans `/Users/malik/Documents/orchestration` ni dans `/Users/malik/Documents/1RR`. Aucun `git` en écriture sur ces dépôts.
- Pas de sous-agent lancé.

## Ce qui est établi (détail et SHA dans `01-sources.md`)

- Nomenclature Bxx puis Fxx : `B1F3` (23/08), `B1F4` (24/08), `B1F1` (25/08) dans les messages 1RR ; premier `F02` le 06/09 (`4d9af72`). La note 06/09 de `historique.md` confirme le passage à Fxx.
- Premier superviseur déterministe dans 1RR : V3 du 18/09 (`519f3fa`, `4520fd2`), réveil Cowork par `send_later`, hooks par `--settings`. Décision de Malik « je ne veux pas dev pour une future dette technique » (`historique.md:931`).
- 19/09 : 1RR V2.0 (refonte), V2.3 de la convention. 22/09 14:04 UTC : premier commit d'orchestration `e235da7`.
- Lint de mandat : première trace dans orchestration (23/09, `53858d0`). Absente de 1RR.
- Réveil, « un réveil créé = un réveil supprimé » : orchestration 23/09 (`62ba19e`).

## Ce qui manque (trous, pour l'entretien)

- Nombre de bureaux et de fenêtres ; dates du 2e et du 3e bureau.
- Le geste manuel de lancement (`claude`, modèle, effort, « va lire ton mandat ») : aucune source écrite.
- Erreurs de lancement : une seule piste, `vault/revues/2026-09-23-R016-doublage-M0043-superviseur-1-4-0.md:113` (incident M9991→M9992), sans date.
- Atelier « Harness Engineering with Claude Code » : la date (22 ou 23/09) n'est attestée que par le prompt du 23/09. Barcelone et Alexio Cassani n'apparaissent dans aucune source lue (0 occurrence dans le vault d'orchestration). À obtenir de Malik.
- Le dossier `/Users/malik/he-workshop/code/`, cité par le prompt du 23/09, est hors des sources autorisées : non lu.

## Écarts et points à arbitrer

- Le brouillon « coûte dix fois moins cher / ne hallucine jamais » : aucune mesure dans les sources. À demander à Malik sur quoi repose son constat.
- « Patch de 3 500 caractères » (brouillon) : 3 500 est le plafond des leçons injectées (`lecons_injection.taille_max`). À corriger dans le brouillon.
- Le harnais existait avant l'atelier (superviseur 18/09, V2.0 19/09). L'atelier a durci un système existant. À confronter au récit de Malik.

## Choix faits sans arbitrage

- `01-sources.md` reste `status: draft` : les trois manques sont des faits que seul Malik peut donner. Aucune question n'a été posée pendant la session.
- Le fichier `01-sources.md` vit dans `interviews/`, hors suivi git, conformément au skill (fichiers de travail non commités).
- Aucun code modifié : pas de test à rejouer, pas de relecture indépendante.

## Tests

Aucun test : la mission ne touche aucun code. Vérifications exécutées : `git rev-parse` (préconditions), `git log` et `git show` en lecture sur les deux dépôts, grep ciblé.
