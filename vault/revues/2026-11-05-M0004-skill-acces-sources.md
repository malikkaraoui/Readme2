---
date: 2026-11-05
tags: [skill, docs, M0004, revue]
session: F01
mandat_id: M0004
branche: fix/skill-acces-sources
tip: bcec8239475aeee1d92a077d3ca63afc344f1f8b
merge_main: 2ce7251c27ddd0dc006ba359416e34760a8aa58a
revue: R003
verdict: GO
niveau: N2
---

# M0004 — Aligner le skill du dépôt sur la version du compte (accès aux sources en lecture seule)

## Gardes de précondition

- `main` et `origin/main` valaient `f0dfac3c394352df0ed773fa130f3a740ffa36ae` avant le travail (`git rev-parse`, après `git fetch origin`).
- Source synchronisée trouvée : `~/.claude/skills/synced/63893402-…/readme2-interview/SKILL.md`. Empreinte `06c2b80b3de11a32abe27f49872930c8ce7979e8c47d17ba8a50363d264512cc` vérifiée (copie puis `shasum -a 256` dans le worktree).

## Ce qui a été fait

- `skills/readme2-interview/SKILL.md` : copie exacte de la source synchronisée (empreinte vérifiée).
- `skills/readme2-interview/templates/00-framing.md` : quatre lignes ajoutées après `- Article language(s):` (`Source folder (read-only):`, `Access granted (date, time):`, `Workspace folder:`, `Length (short, medium, long):`). Champs existants conservés.
- `README.md` : libellé Mermaid de `P1` = « 1. Access and framing » ; phrase de la phase 1 (accès en lecture seule d'abord, puis public, longueur, langues, angle) ; phrase sur `interviews/<slug>/` (espace de travail hors du dossier source, en lecture seule).
- `README.fr.md` : équivalents en français (« 1. Accès et cadrage », mêmes affirmations).
- Commit de la branche : `bcec823` (4 fichiers, +58 −34). Poussé, `git ls-remote origin refs/heads/fix/skill-acces-sources` → `bcec8239475aeee1d92a077d3ca63afc344f1f8b`.

## Revue (N2, R003)

- Sous-agent frais, worktree détaché en lecture seule au tip `bcec823`. Verdict **GO**, aucune réserve bloquante.
- Remarques non bloquantes, sans issue (`lecons.issues: false` dans la config, aucune issue ouverte) :
  - 3a : les READMEs disent « dans votre projet » ; SKILL.md dit « the folder where the skill is used », « NOT in the source folder ». Formulation plus exacte possible.
  - 3b : la phrase « langues » des READMEs ne couvre que la langue de l'article ; SKILL.md (règle 10) et le gabarit demandent aussi la langue de l'entretien.
  - 5a : SKILL.md n'a pas de saut de ligne final. C'est la copie exacte de la source ; aucune action.
- Écart signalé : le rapport `vault/revues/2026-11-05-R003-skill-acces-sources.md` committé sur `main` a été **réécrit à la main** par l'orchestrateur à partir du rapport du relecteur, au lieu d'être copié tel quel. Verdict, `tip` et `niveau` sont identiques, mais le libellé de certains points diffère. L'original du relecteur est conservé hors dépôt : `/private/tmp/claude-501/-Users-malik-Documents-interview/253d875d-a2af-44d3-b7fd-1394194e2bfd/scratchpad/R003-original-relecteur.md`. Pas de réécriture d'historique (main déjà poussé).

## Fusion (gabarit §9)

- Scratch détaché depuis `origin/main` (`f0dfac3`), `merge --no-ff bcec823` → `2c5a3c8`.
- Rapport R003 committé dans le scratch → `2ce7251`, puis `merge --ff-only` à la racine (sans refus).
- `git push origin main` : `f0dfac3..2ce7251`. `git ls-remote origin refs/heads/main` → `2ce7251c27ddd0dc006ba359416e34760a8aa58a refs/heads/main`.
- Worktrees de travail, de revue et de scratch retirés. Le worktree de revue n'a été retiré qu'après déplacement de son rapport hors dépôt.

## Tests et vérifications

- Empreinte SKILL.md : OK.
- `git diff --check f0dfac3..bcec823` : rien.
- `git diff --name-only f0dfac3..bcec823` : exactement les 4 fichiers attendus.
- Aucun test automatisé n'existe pour ce skill ; la vérification repose sur les contrôles ci-dessus et sur la relecture R003. Le Mermaid n'a pas été rendu avec un moteur (validation par comparaison au tip précédent).

## Hors périmètre, non traité

- `vault/echanges/archive/20261105-175459-F01-avant-M0004.md`, `interviews/`, `.DS_Store` : fichiers non suivis de la racine, laissés tels quels.
- `vault/runtime/entretien.lock.478` : hors git, non touché.
