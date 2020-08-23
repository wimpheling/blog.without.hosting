---
title: "Rust Dominator/Signals tutorial"
date: 2020-08-20T21:10:40+02:00
draft: true
---

**The Virtual DOM pattern is inefficient.** When data mutates, you just want to update the DOM elements and values that needs to change. Why would you ever regenerate the whole DOM tree, even virtually, then do a global diff ?

These days, the front-end scene seems to have started following that trail. I've been having lots of fun with [Svelte](https://svelte.dev), a very performant JS framework which does exactly that :

- subscribe to events
- and upgrade the DOM surgically.

# Rust

On a personal level, I have also been learning Rust, and as a front-end developer, its WASM support is a big topic of interest, especially when it comes to implement strict models with performance in mind.

But working with Svelte + Rust still raises problems :

- JS/WASM integration is still difficult, especially if you want to use TypeScript

- Typescript support still isn't perfect with Svelte (better now, but still try to have ESLint in your template files...)

So why not develop the UI in Rust too, and benefit from its robust type-system ? [Yew](https://yew.rs/) seems to have become the standard front-end for Rust/WASM but to my great dismay, it is based on Virtual DOM too...

# Enters Dominator

To get Svelte's workflow with Rust, you have to dig deeper, turn to the threateningly named [Dominator](https://crates.io/crates/dominator) library, and face its terrible lack of clear documentation.

Dominator is

- is a minimalist Rust front-end library
- is based on the `web-sys` bindings for DOM
- should be used with the [futures-signals](https://crates.io/crates/futures-signals) library to handle event messaging

I will try in this article to help you through your journey towards total domination of the DOM in Rust.

In that tutorial we will :

- Create a Dominator project
- Use an external web components UI library
- Implement custom logic in Rust
- Update the DOM through events

# Let's install it

To make it simple, we'll use the [unofficial boilerpate made by thienpow](https://github.com/thienpow/rust-dominator-boilerplate)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>
```

git clone https://github.com/thienpow/rust-dominator-boilerplate

# Sources

- [rust-dominator-bootstrap [Github]](https://github.com/thienpow/rust-dominator-bootstrap)

  Detailed instructions on how to set up a Dominator project from scratch.

- [Shipyard + Dominator + LitElement =](https://medium.com/@david.komer/shipyard-dominator-litelement-b4bcdc7ec42d)

  Nice Architecture idea which I follow : Rust for the whole app logic and some Typescript Web-Components for the UI.
