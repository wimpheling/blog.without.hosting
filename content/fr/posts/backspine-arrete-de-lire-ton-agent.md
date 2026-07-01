---
title: "Arrête de Lire Ce Que Ton Agent de Code Raconte"
date: 2026-07-01
tags: ["backspine", "hot takes"]
toc: true
translationKey: "backspine-dont-read-agent-text"
description: "Les agents de code sont là pour produire du code, pas pour en parler. Leur sortie textuelle est du bruit, et évaluer ce qu'ils disent plutôt que ce qu'ils implémentent crée une mauvaise boucle de feedback."
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

## La surface, c'est la sortie

La surface d'un agent de code, c'est le code. Pas un chat sur le code. Pas un plan pour le code. Pas un résumé du code.

Le code *est* l'interface. Le diff *est* la couche de présentation. La revue de l'artefact *est* la conversation avec l'agent.

Tout le reste — les tokens de raisonnement, les plans, les "je vais corriger ça en faisant X" — c'est du commentaire sur le travail, pas le travail. Et plus tu en lis, moins tu regardes ce qui a réellement été produit.

Arrête de lire ce que ton agent raconte. Lis ce qu'il produit.