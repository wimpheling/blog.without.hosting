---
title: "Coder des Agents, C'est Juste du Code"
description: "Tool calling, MCP, boucles agentiques — rien de magique. Une simple boucle while. La vraie compétence, c'est concevoir la structure rigide autour du LLM, et c'est là que va le métier de dev."
date: 2026-07-01
---

J'ai récemment commencé à coder mes agents en TypeScript avec le SDK Vercel AI.

C'est une librairie bas niveau. Elle sait appeler des outils, parler MCP, streamer des tokens — mais elle n'a pas de boucle agentique préprogrammée. Pas de pipeline "plan-exécute-review" tout fait, pas d'opinion sur comment l'agent doit raisonner. Elle te donne `generateText`, `streamText`, `generateObject`, et `toolCall` comme primitives, et puis elle s'arrête.

Tout le reste — la boucle, la mémoire, les retries, la sélection d'outils, la gestion du contexte — c'est ton code.

Et c'est ça la révélation : **toutes les fonctionnalités impressionnantes de Codex, Claude Code, Cline et compagnie ne sont que des patterns de programmation basiques.**

- Un tool call, c'est un dispatch de fonction.
- Une boucle agentique, c'est un `while (agent.shouldContinue())` avec un garde-fou de max iterations.
- MCP, c'est un adaptateur de protocole qui map des schémas d'outils vers un transport.
- La compression de contexte, c'est un `if (context.length > limit) summarize(oldest)`.
- L'exécution parallèle d'outils, c'est `Promise.all(tools.map(call))`.
- Un cycle plan-exécute-review, c'est une machine à états à trois états.

Rien de nouveau là-dedans. Aucun besoin de recherche. C'est juste du code.

Tout développeur un peu expérimenté a écrit des event loops, des tables de dispatch, des machines à états et des wrappers de retry des centaines de fois. La seule différence, c'est que la fonction appelée se trouve maintenant être un modèle de langage.

## Des Prompts aux Programmes

Le profil Hermes avec lequel je travaille tous les jours [^1] est l'approche inverse. Des agents construits à partir de skills et de prompts — des fichiers markdown avec des instructions, chargés comme contexte à chaque tour. Ça marche, mais c'est un monde de comportement émergent. Tu ne peux pas unit-tester un skill. Tu ne peux pas mettre un point d'arrêt dans un template. Tu ne peux pas mesurer la latence d'une étape spécifique. La seule boucle de feedback, c'est l'auto-rapport de l'agent : "j'ai fait le truc."

Quand tu réécris la même logique en fonctions TypeScript, quelque chose change. La boucle devient explicite. Tu peux logger chaque étape. Tu peux mesurer la latence des outils et le coût en tokens par appel. Tu peux unit-tester la logique de routing. Tu peux ajouter un circuit breaker quand un outil retourne trois erreurs d'affilée. Tu peux sérialiser l'état de l'agent et le reprendre plus tard.

L'agent cesse d'être une boîte noire qui marche parfois. Il devient un programme que tu peux déboguer.

## La Partie Frustrante

Je vois ce monde s'ouvrir — la possibilité de construire des agents précis, testables, programmables — et j'ai l'impression que c'est une direction fondamentale pour le métier.

Ce qui est frustrant, c'est l'écart entre cette réalité et la conversation publique autour des coding agents. La narration dominante, c'est la boîte noire magique : "L'agent a raisonné, planifié, exécuté." On parle des agents comme s'ils étaient des entités mystérieuses, comme si leurs mécanismes internes étaient le domaine des chercheurs en ML.

Mais le ML est dans le modèle, pas dans la boucle. L'inférence, c'est le dur. La boucle, c'est juste du code.

Les entreprises qui construisent Codex et Claude Code résolvent de vrais problèmes — sandboxing, caching, sorties structurées à l'échelle, design de protocole. Mais le pattern de base "appelle LLM, parse la réponse, appelle peut-être un outil, répète" n'est pas un de ces problèmes difficiles. C'est la première chose que tu écris en ouvrant les docs de l'API.

Bref, l'écart entre le battage médiatique et la simplicité réelle du pattern — c'est ça qui est frustrant. Pas que personne ne voie. Beaucoup voient. Mais la conversation, elle, reste bloquée sur le storytelling agentique.

## La Vraie Compétence

C'est là que je vois la continuité du métier de développeur.

Le futur, ce n'est pas le prompt engineering. Ce n'est pas écrire de meilleures instructions markdown pour les agents. C'est **concevoir des structures rigides, simples et élégantes dans lesquelles les LLM peuvent être productifs**.

Le LLM est un moteur probabiliste. Tu ne peux pas le rendre déterministe. Mais tu peux contraindre sa surface d'action pour que chaque mauvaise réponse soit attrapée, chaque hallucination soit bornée, chaque appel coûteux soit caché, et chaque mode d'échec ait un handler.

C'est ce que des frameworks comme le SDK Vercel AI rendent évident : tu n'as pas besoin d'un framework. Tu as besoin de patterns. De bons patterns. Bien testés.

Le travail dur, ce n'est pas la boucle while. C'est :
- Concevoir le schema des outils pour que le modèle puisse s'exprimer clairement.
- Construire la machine à états pour que l'agent ne reste jamais bloqué.
- Écrire les tests qui prouvent que la boucle gère les cas limites.
- Décider quand laisser le modèle penser librement et quand le contraindre avec une sortie structurée.
- Reconnaître quelles décisions appartiennent au modèle et lesquelles appartiennent au code.

C'est ça, le métier. Ça a toujours été ça. Les outils ont changé, mais la compétence n'a pas changé : **construire des systèmes prévisibles, mesurables et ennuyeux**.

Le LLM est le composant le plus intéressant du système. Tout ce qui l'entoure devrait être aussi ennuyeux que possible.

[^1]: Le système Hermes qui gère mon blog et automatise mes workflows. Construit avec des prompts et des skills. Ça marche très bien. C'est aussi l'exemple parfait de pourquoi je veux aller dans l'autre direction.
