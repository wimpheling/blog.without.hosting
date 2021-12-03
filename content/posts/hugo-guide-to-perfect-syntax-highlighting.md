---
title: "Definitive guide to syntax highlighting in Hugo"
date: 2020-08-20T21:10:40+02:00
draft: true
---

I've just started this coding blog that you're currently reading, and of course it will rely a lot on code excerpts. I use [Hugo](https://gohugo.io/), one of the most popular static blog engines, so let's see how we can make it work.

# Which highlighting engine to choose ?

The [Hugo official documentation for syntax highlighting](https://gohugo.io/content-management/syntax-highlighting/) details how to use the [Chroma](https://github.com/alecthomas/chroma) engine.

`Chroma`, like Hugo, is written in the Go language, so your code exceprts will be converted to nice-looking HTML at compile-time. It is good to know that Hugo also supports Javascript tools such as `highlight.js` which are maybe less performant, but have more features, are more battle-tested etc.

# How to set up Chroma

Unfortunately, I find **Hugo documentation for syntax highlighting to be quite misleading**. When just following their instructions I didn't manage to have the full syntax highlighting working. So here are my detailed steps.

## Create a hugo project
