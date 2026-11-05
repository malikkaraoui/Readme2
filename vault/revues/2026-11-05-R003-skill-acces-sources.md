---
verdict: GO
tip: bcec8239475aeee1d92a077d3ca63afc344f1f8b
niveau: N2
---

# R003 : skill readme2-interview, accès aux sources en lecture seule

Périmètre : `git diff f0dfac3..bcec823`, 4 fichiers (`README.md`, `README.fr.md`, `skills/readme2-interview/SKILL.md`, `skills/readme2-interview/templates/00-framing.md`). Relecteur : sous-agent frais, worktree détaché, lecture seule. Tip vérifié par `git rev-parse HEAD`.

## Points

1. ✅ Empreinte du SKILL.md : `shasum -a 256 skills/readme2-interview/SKILL.md` = `06c2b80b3de11a32abe27f49872930c8ce7979e8c47d17ba8a50363d264512cc`, identique à l'attendu.

2. ✅ Gabarit `00-framing.md` : les 4 lignes ajoutées (Source folder read-only, Access granted date/time, Workspace folder, Length short/medium/long) correspondent à la phase 1 de SKILL.md (lignes 71-78 : dossier, date et heure, « read-only » ; longueur short/medium/long ; dossier de travail lignes 41-49). Champs existants conservés, l'en-tête et le `status:` inchangés.

3. ✅ README.md / README.fr.md fidèles au SKILL.md, parité EN/FR vérifiée phrase à phrase :
   - Phase 1 « accès en lecture seule d'abord » : SKILL.md:72 (étape 1) et règle 1 (ligne 17).
   - « audience, longueur, langues, angle » : SKILL.md:74-76.
   - « espace de travail hors du dossier source, en lecture seule » : SKILL.md:43-44.
   - Libellé Mermaid « Access and framing » / « Accès et cadrage » : SKILL.md phase 1 (ligne 71).
   - ⚠️ Remarque 3a : les deux READMEs disent que le skill crée `interviews/<slug>/` « dans votre projet » (README.md:77, README.fr.md:77). SKILL.md:43-45 dit « the folder where the skill is used », « NOT in the source folder ». Non faux, mais « votre projet » peut se lire comme le dossier source. Non bloquant.
   - ⚠️ Remarque 3b : la phrase « langues » des READMEs ne couvre que la langue de l'article ; SKILL.md règle 10 et le gabarit demandent aussi la langue de l'entretien. Omission, non bloquant.

4. ✅ Mermaid : seul le libellé de `P1` change (ligne 21 de README.md et README.fr.md). Le reste du bloc est identique. Validation par comparaison seulement (pas de moteur Mermaid disponible).

5. ✅ Hors périmètre et cohérence :
   - `git diff --name-only f0dfac3..HEAD` liste exactement les 4 fichiers attendus.
   - `git diff --check f0dfac3..HEAD` : rien (rc=0).
   - Frontmatter de SKILL.md : YAML valide.
   - Autres références au SKILL.md (`references/method.md:6`, `references/formats.md:32`, `scripts/check_article.py`) : cohérentes, aucune référence périmée.
   - ⚠️ Remarque 5a : `SKILL.md` n'a plus de saut de ligne final. C'est la copie exacte de la source (empreinte confirmée). Aucune action.

## Réserves bloquantes

Aucune. Aucun test rouge ni affirmation fausse ne prouve une réserve.

## Verdict

GO. Deux remarques non bloquantes (3a sur « dans votre projet », 3b sur la langue de l'entretien).
