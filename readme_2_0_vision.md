# Spec Technique & Vision : README 2.0 (Dev-Ghostwriter)

Ce document formalise la vision et l'architecture du projet de plateforme de curation et d'extraction de connaissances pour développeurs.

---

## 🎯 La Vision du Projet
L'objectif est de créer le **README 2.0**. Un système interactif qui donne une voix et une visibilité aux codes cachés ou sous-cotés sur GitHub. 

La plateforme résout la corvée de rédaction et de marketing technique pour les développeurs en transformant un simple entretien oral en un écosystème de contenus complet, multimédia et multi-canal. Elle sert de hub de découverte ("à la Product Hunt") pour les investisseurs, porteurs de projets, recruteurs et passionnés de tech afin de dénicher les pépites de demain.

---

## 🛠️ Le Workflow Global (Le Pipeline)

```
┌─────────────────┐      ┌─────────────────────────┐      ┌───────────────────────────┐
│ 1. INTERVIEW IA │ ───> │ 2. EXTRACTION DE TEXTE  │ ───> │ 3. ARCHITECTURE & VISUEL  │
│ (Vocal ou Chat) │      │ (Blog SEO & Posts Social)│      │ (Schémas Mermaid + Flux)  │
└─────────────────┘      └─────────────────────────┘      └───────────────────────────┘
                                                                        │
                                                                        ▼
┌─────────────────┐      ┌─────────────────────────┐      ┌───────────────────────────┐
│ 6. HUB PUBLIC   │ <─── │ 5. PODCASTS EN 1 CLIC   │ <─── │ 4. SYNTHÈSE VOCALE (VOICE)│
│ (Readme 2.0 VCs)│      │ (Flux RSS, Spotify...)  │      │ (Clone ElevenLabs 30s)    │
└─────────────────┘      └─────────────────────────┘      └───────────────────────────┘
```

### 1. Phase d'Interview (Extraction)
* L'IA agit comme un journaliste tech et podcaster senior.
* Au lieu de faire face à une page blanche, le développeur est cuisiné de manière pointue sur son code, ses métriques et ses choix d'architecture.

### 2. Phase de Repositionnement (Génération Multi-Canal)
* **📝 Article Technique (Long-form) :** Rédaction d'un retour d'expérience structuré (Problème, Solution, Code, Performance).
* **📱 Posts Réseaux Sociaux :** Création de threads X/Twitter et de posts LinkedIn accrocheurs pour engager la communauté.
* **📊 Schématisation Automatique :** Génération de diagrammes d'architecture dynamiques (rendus via Mermaid.js dans le markdown) et d'images d'illustration via modèles génératifs (Flux / DALL-E 3).

### 3. Pipeline Audio & Clone de Voix ("En 1 Clic")
* **Clone Rapide (Instant Voice Cloning) :** Capture de 30 secondes de la voix du développeur pendant l'interview via API (ex: ElevenLabs).
* **Génération de Script & Audio :** Transformation de la transcription en un script de podcast dynamique (monologue ou interview croisée).
* **Distribution Automatisée :** Publication instantanée sur un flux RSS et les plateformes de streaming (Spotify, Apple Podcasts, Spreaker).

### 4. La Plateforme Finale (Le Hub des Pépites)
* Un site vitrine épuré mettant en avant chaque projet de manière ultra-visuelle et immédiate.
* Chaque fiche projet comprend : le lecteur du podcast vocalisé par le dev, le schéma d'architecture dynamique, le REX écrit et le lien vers le dépôt GitHub.
* Un filtre par tags et système de vote pour aider les investisseurs et porteurs de projets à cibler la valeur tech brute.

---

## 📝 Prompt Système de l'Agent Interviewer (V1)
Pour tester l'expérience immédiatement avec un LLM (ChatGPT / Claude), utilisez le prompt système suivant :

> *"Agis comme un journaliste tech et un podcaster senior. Ton but est de m'interviewer pour extraire mon expertise technique sur mon projet de code. Ne génère pas tout le contenu d'un coup. Pose-moi une seule question pointue à la fois, centrée sur mes choix techniques, mes défis ou mes métriques de performance. Attends ma réponse avant de rebondir. Après 5 à 6 questions, compile nos échanges pour générer : 1) Un article de blog technique Markdown complet avec structure claire, 2) Un post LinkedIn accrocheur, 3) Un script d'épisode de podcast dynamique à deux voix, et 4) Un schéma d'architecture au format de code Mermaid.js."*

---

## 🏷️ Idées de Noms pour le Repo GitHub
* **`dev-ghostwriter`** *(Recommandé — Évoque l'écrivain fantôme qui écrit pour le dev)*
* **`kill-the-blank-page`** *(Axé sur la suppression de la barrière de la rédaction)*
* **`devvox`** *(Mélange de Dev et de Voix)*
* **`readme-2.0`** *(Axé sur le positionnement du produit final)*