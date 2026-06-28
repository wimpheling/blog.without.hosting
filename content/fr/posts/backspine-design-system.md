---
title: "No Prompt, Just Linters"
date: 2026-06-28T00:00:00+00:00
unlisted: true
tags: ["backspine"]
toc: false
description: "Deux règles de composition enforceées par des linters custom — et un agent IA qui auto-gère un design system sans aucun prompt."
---

C'est le truc dont je suis le plus fier dans mon archi front.

Les générateurs de code IA produisent facilement du slop non structuré quand il s'agit d'UI. Demande à un agent de construire une page, et il va générer une constellation unique de `div` avec des classes Tailwind brutes — espacement différent, layout différent, tout légèrement différent — à chaque fois. Le même élément conceptuel rendu de douze façons dans douze fichiers parce qu'il n'y a aucune raison structurelle de faire autrement. Le coût en tokens d'écrire directement est zéro. Le coût de composer est non nul. L'IA optimise pour le coût token.

Ce n'est pas un problème de prompt. Tu ne peux pas demander à une IA d'être "cohérente avec les composants" et espérer que ça marche — l'incitation est mauvaise. L'IA va être d'accord et puis écrire directement quand même, parce que c'est ce à quoi ressemble l'optimisation de tokens à l'étape de génération.

La solution est structurelle : rendre l'erreur impossible.

J'ai construit deux règles de lint :

1. **Les composants** peuvent contenir du HTML, du CSS et des éléments JSX bruts.
2. **Les pages** ne peuvent que composer des composants. Rien d'autre.

Dix minutes, des linters customs écrits par le même agent qui écrivait le code. Pas de prompt sur la discipline du design system. Pas de "please follow this pattern" dans un fichier d'instruction. Juste deux règles qui cassent la build si une page essaie d'utiliser un `div` nu avec du style inline.

Et l'agent s'est adapté.

## Le comportement émergent

L'agent a arrêté le slop. Il a commencé à vérifier la librairie de composants avant d'en créer de nouveaux. Quand un composant fonctionnait presque, il l'étendait plutôt que d'en créer un frère. Il a composé ses pages avec une grammaire limitée d'éléments d'UI.

Ce n'était pas un accident — c'était le résultat attendu. Les contraintes ont été conçues pour inverser la surface de coût. Avant les linters, le chemin token le moins cher était d'écrire directement. Après les linters, le chemin le moins cher est le bon : du HTML brut dans une page = une erreur de build, qui signifie un cycle de régénération, qui coûte plus de tokens que de faire les choses correctement du premier coup. L'agent s'est adapté parce qu'il n'avait pas d'option moins coûteuse.

Le design system a émergé des contraintes, pas de la documentation. Les composants sont peu nombreux et généraux. Les pages sont des compositions. La cohérence visuelle n'est pas le résultat d'une palette curatée ou d'une échelle de spacing — c'est la conséquence mécanique du même petit ensemble de composants qui rend tout. La grammaire des éléments disponibles est petite. Le résultat est cohérent.

## L'enforcement

Les linters eux-mêmes sont triviaux. Ils vérifient deux choses :

- Un fichier en dehors du répertoire `components` contient-il des éléments JSX qui correspondent à des balises HTML brutes (`div`, `span`, `input`, etc.) ? Erreur.
- Un fichier en dehors du répertoire `components` importe-t-il des modules CSS ou utilise-t-il du style inline ? Erreur.

C'est tout. Le linter a été écrit par l'agent en dix minutes. Le générateur de code a construit la barrière qui se tient elle-même en respect.

Les linters tournent à chaque sauvegarde de fichier pendant le développement et dans l'étape de build. Une page qui utilise un `div` brut avec des styles inline ? Build cassée. L'agent reçoit une erreur de lint et s'auto-corrige. Il ne surcharge pas le linter — il compose différemment.

C'est la partie qui donne l'impression que ça ne devrait pas marcher : l'agent a écrit ses propres contraintes. Mais ça marche parce que les contraintes sont structurelles, pas rhétoriques. Le linter ne dit pas "please consider using a component." Il dit `exit code 1`. Il n'y a pas de négociation.

## L'implémentation

La structure de packages derrière tout ça est simple. Un package contract (`design-system-contract`) définit les APIs typées des composants. Une implémentation de base (`design-system-basic`) fournit les composants React plus le CSS. Un package facade (`design-system`) expose la surface d'import publique. Les linters se situent au sommet de cette stack.

Cette même architecture s'applique à un client React Native en cours. Le même contract, les mêmes linters, la même barrière composants-vs-pages — juste une cible de rendu différente. Les contraintes se traduisent sans modification.

## Pourquoi ça marche

C'est la vieille leçon sur l'ergonomie des langages de programmation appliquée à la génération de code IA : les contraintes produisent un meilleur comportement émergent que les instructions. Dis à l'IA ce qu'elle *ne peut pas* faire, et elle trouvera la bonne façon de faire ce qu'elle *peut* — sans que tu aies à décrire à quoi ressemble le "bien".

Les linters ne sont pas un design system. Ils sont une limite qui force un design system à exister. L'agent fait lui-même la curation, parce que l'alternative est une build qui échoue. Pas de prompts, pas d'exemples, pas de contexte de fenêtre gaspillé sur l'enforcement de conventions.

Le résultat est un codebase où l'IA gère sa propre librairie de composants avec le genre de discipline qu'on attendrait d'un ingénieur humain qui s'est fait brûler par la prolifération de composants. Et elle le fait sans jamais qu'on lui dise de le faire.