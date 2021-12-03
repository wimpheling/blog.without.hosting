---
title: "A guide to contenteditable sanitization"
date: 2020-12-25T21:10:40+02:00
draft: true
---

I've been recently trying to create a custom contenteditable editor, that should output fine-grained data. That means you have to prevent the user from entering any unwanted content inside your element. If you start working on this, you will encounter two types of blog posts :

- Framework publishers (such as EditorJS, tinyMCE etc) explaining the broad lines of what they did
- Blog posts explaining why using contenteditable is hell.

It seems however that the big names are perfectly able to deliver a satisfactory experience using contenteditable. This post will give you a detailed guide of what events you need to catch to force your user to deliver only fine-grained, formatted content according to the rules you define.

For this project, I fortunately have the leisure to skip problematic browser support, and ignore IE11 or Safari.

# Different possible approaches

There is no standard library for controlling contendeditable, because if you want to implement your own version of it, you certainly have very specific needs. Here are some of the ones I had :

- Simple <input>s
  They cannot easily have auto-length, or use word-wrap. I wanted a very simple contendeditable, with only plain text, single-line content.

- Keyboard navigation between contenteditables.
  Several contenteditable elements are in the document, and I want the suer to browse through them using the keyboard as if in a Word document. In the normal behavior the caret gets stuck at the end of the contenteditable, so I needed to catch these.

# Paste events

The worst risk of unwanted content is of course pasting. You definitely don't want your user entering any HTML formatted by Word or any other barbarisms.

# Drag and drop events

By default images can't be dragged into contenteditable elements, so there is nothing to do concerning them. But a user can still drag and drop some text, or even worse, HTML content, within the element. You can disable them using the `dragover` and `drop` events.

You can also sanitize the content.

# Bold, Italics, Underline

# Enter

Because it creates new lines, sometimes with BR sometimes with DIV.

When dealing with single line inputs you can just prevent it.

If you allow multi-line content, you should catch it to control the HTML output. (insert br ? insert a new div/p ?)

You can also use the "External model" approach and just update your abstraction.

# Arrow Down/Up
