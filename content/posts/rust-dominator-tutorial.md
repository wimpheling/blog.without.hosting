---
title: "Rust Dominator/Signals tutorial"
date: 2020-08-20T21:10:40+02:00
draft: true
---

> This is part of four-part articles about `rust-dominator`. Here are the links to the other articles:
>
> - Create a Dominator project _(you're here)_
> - Use an external web components UI library
> - Implement custom logic in Rust
> - Update the state and the DOM through events

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

Dominator:

- Minimalist Rust front-end librar
- _Zero cost declarative DOM library using FRP signals for Rust!_
- Based on the `web-sys` bindings for DOM
- Should be used with the [futures-signals](https://crates.io/crates/futures-signals) library to handle event messaging

# Let's install it

## Pre-requisites

To follow this tutorial, you will need:

- nodejs and npm
- Rust

To make it simple, we'll use the [unofficial boilerpate made by thienpow](https://github.com/thienpow/rust-dominator-boilerplate). If you want more detail on how to install it from scratch, you can follow [this tutorial by the same author](https://github.com/thienpow/rust-dominator-bootstrap).

## Installation

Run this in bash:

```bash
git clone https://github.com/thienpow/rust-dominator-boilerplate rust-dom
cd rust-dom
npm install
npm run start:dev
```

You should then see Cargo building the rust code, then webpack briefly running, and then this message :

```
ℹ ｢wdm｣: Compiled successfully.
```

You can now go to [http://localhost:8000](http://localhost:8000) and you should see something like this:

![Hello world](/img/rust-dominator-01.png)

Let's now have a look in how the project is organized.

## Project structure

### Javascript !

The first thing that one can see in our project is quite a surprise : we still need webpack and javascript to call our WASM file ! Webpack seems to be mostly here for launching the dev server though (and maybe unnecessary).

The `bootstrap.js` file is quite minimalistic :

```js
import("./pkg").then((module) => {
  // you can use the exported function from the module object
});
```

You can notice that the `import` ES6 keyword is not used in the standard `import { MyItem } from "./myfile"` syntax. Instead, it is called in a way that looks like a function call that returns a Promise. We won't go further with that as we won't rely on JS here, but just so you know, that's a huge pain point when integration WASM with JS build systems !

### wasm-bindgen / web-sys

As we saw earlier, Dominator uses [wasm-bindgen](https://rustwasm.github.io/wasm-bindgen/), which is the de facto standard for interacting with the DOM from WASM-compiled Rust. **Pauan**, the author of Dominator, is one of the contributors of `wasm-bindgen`.

`Wasm-bindgen` is the runtime that allows to export rust code to the WASM format, which is necessary for it to run in the browser. If you choose to develop front-end using Rust, you will need at some point to read the `wasm-bindgen` docs.

Dominator also uses [web-sys](https://rustwasm.github.io/wasm-bindgen/web-sys/index.html), a subset of `wasm-bindgen`, which allows us to import and call the Web standard libraries. In the `Cargo.toml` file of your new project, you will find these declarations that import the necessary bindings.

```toml
[dependencies.web-sys]
version = "0.3.33"
features = [
    "CharacterData",
    "Comment",
    "CssRule",
    "CssRuleList",
    "CssStyleDeclaration",
    "CssStyleRule",
    "CssStyleSheet",
    "Document",
    "DomTokenList",
    "Element",
    "Event",
    "EventTarget",
    "FocusEvent",
    "InputEvent",
    "History",
    "HtmlElement",
    "HtmlHeadElement",
    "HtmlInputElement",
    "HtmlStyleElement",
    "HtmlTextAreaElement",
    "KeyboardEvent",
    "Location",
    "MouseEvent",
    "Node",
    "Storage",
    "StyleSheet",
    "SvgElement",
    "Text",
    "UiEvent",
    "Url",
    "Window",
]
```

If you need to interact with other web APIs (for example `window.fetch`), importing the bindings declaratively allows you to add only the needed one to your project and thus optimize your program's size and performance.

## The actual code

The bootstrapped project just includes two rust files :

- `app.rs` is the front-end program, and is the part that uses `dominator`.
- `lib.rs` is the main project file, and is in charge of mouting the app to the DOM.

We'll now - finally - have a first look at how Dominator works more in detail.

### DOM Generation

### CSS classes generation

`dominator` provides helpers to create css classes inside your rust code, in a similar way to techniques used in JS such as [JSS](https://cssinjs.org/).

```rust (linenos=table,linenostart=18)
lazy_static! {
    static ref ROOT_CLASS: String = class! {
        .style("overflow-x", "hidden")
        .style("color", "red")
    };
}
```

# Sources

- [rust-dominator-bootstrap [Github]](https://github.com/thienpow/rust-dominator-bootstrap)

  Detailed instructions on how to set up a Dominator project from scratch.

- [Shipyard + Dominator + LitElement =](https://medium.com/@david.komer/shipyard-dominator-litelement-b4bcdc7ec42d)

  Nice Architecture idea which I follow : Rust for the whole app logic and some Typescript Web-Components for the UI.
