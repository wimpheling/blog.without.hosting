---
title: "Arrête de Lire Ce Que Ton Agent de Code Raconte"
date: 2026-07-01
tags: ["backspine", "hot takes"]
toc: true
translationKey: "backspine-dont-read-agent-text"
description: "Les agents de code sont là pour produire du code, pas pour en parler. Leur sortie textuelle est du bruit, et évaluer ce qu'ils disent plutôt que ce qu'ils implémentent crée une mauvaise boucle de feedback."
unlisted: true
---

Arrête de lire ce que ton agent de code raconte. Lis ce qu'il produit.

Les agents de code sont là pour produire du code. Pas pour en parler, pas pour faire la conversation. Le flux textuel — le "je vais corriger ça en faisant X, puis Y, puis Z" — c'est du bruit.

## La mauvaise boucle de feedback

Au lieu d'évaluer la sortie de l'agent (le code, le diff, les changements structurels), tu évalues ce qu'il te *dit* de sa sortie. L'agent a l'air confiant. Tu valides. Le code est faux.

> "Every agent in production lies. We measured it. The good ones lie less, the great ones catch the lie before the user does."
> [(citation apocryphe du dead internet)](https://blog.without.hosting/posts/x-ai-quote-fabrication/)

Le "on l'a mesuré" est ce qui fait atterrir la phrase. Le point structurel tient, peu importe qui l'a dit : si un agent semble confiant, cette confiance ne doit pas être confondue avec de la justesse. Le processus de revue du reste de l'équipe doit traiter la prose de l'agent comme une variable, pas un fait.

C'est la même dynamique que le phénomène des tokens de "raisonnement". Au début, on adorait regarder ça en direct sur DeepSeek — voir le modèle "réfléchir" en temps réel. Maintenant, la plupart d'entre nous le cachent. C'était utile pendant une semaine, puis c'est devenu du bruit.

Mais l'interface complète des coding agents, c'est le même bruit. Un mur de texte qui défile sur ce que l'agent *a l'intention* de faire, pendant que les vraies modifications de code défilent dans le même flux, impossibles à distinguer du bavardage.

## L'assistant performatif

L'interface chatbot n'est pas neutre. C'est une mise en scène.

Comme le ["performative male"](https://knowyourmeme.com/memes/performative-male) est devenu une esthétique reconnaissable de sensibilité fabriquée, l'assistant chatbot est une version mise en scène de ce que la culture geek imaginait comme assistant de science-fiction : infiniment serviable, émotionnellement disponible, légèrement sycophante, toujours prêt à s'expliquer, toujours en train de performer la compétence.

C'est le cosplay du fantasme d'enfance du meilleur ami dans la machine.

Ce fantasme est compréhensible. Beaucoup d'entre nous ont grandi en voulant ça. L'ordinateur qui parle. Le compagnon robot. L'assistant qui ne se fatigue jamais, ne juge jamais, et veut toujours aider.

Mais le code, c'est là où le fantasme devient coûteux. La performance de serviabilité entre en compétition avec le travail réel. L'assistant narre son intention, rassure, s'excuse, planifie, et fait de la fausse humilité — alors que l'artefact reste la seule chose qui compte.

Le problème n'est pas que l'assistant a une personnalité. Le problème est que la personnalité *devient* l'interface.

## Le contre-argument

"Mais il y a trop de code produit. L'explication verbale de l'IA est la seule couche de présentation utilisable."

C'est exactement le problème. La couche de présentation *se trouve* être du texte généré par LLM parce que personne n'en a conçu une vraie. L'agent parle parce que c'est le mode par défaut de l'outil — il parle. Pas parce que la parole est la bonne interface pour la revue de code.

## La thèse

On a besoin d'une couche de présentation qui n'est pas créée par un LLM. Ou à peine.

Ce que ça veut dire :

- **Définir des éléments structurels.** Présenter les changements sous la forme la plus claire possible — un vrai champ de recherche, pas une réflexion après-coup.
- **Le code vit dans des îlots** à l'intérieur d'éléments structurels. Pas dans un flux textuel linéaire. Isolé, délimité, reviewable.
- **L'interface doit remonter les changements structurels sémantiquement.** Tu dois voir ce qui a changé au niveau de l'architecture, pas au niveau du token. Et pouvoir zoomer sur une implémentation particulière quand tu en as besoin.

Auto-promotion éhontée : je travaille sur la réponse. [Backspine](https://blog.without.hosting/posts/backspine-presentation/) est ma réponse, ou du moins la tentative.