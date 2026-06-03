---
title: "Ai Web Framework"
date: 2025-04-10T21:51:11+01:00
draft: true
---

For more efficiency with Cline and other programming agents, we need a franework that is more compatible with how agent works.

Agents like Cline operate this way:

Actors:
- User
- Agent software (cline etc)
    - commands (edit file, run command etc)
- MCP servers
- LLM


- User inputs a prompt
- Agent processes the prompt (formats, add its own prompt)
- Agent makes a list of allowed instructions, including the MCP servers
- Agent interacts with LLM to obtain instructions in the format it supports
- Agent executes the instructions (stand alone or using MCP servers)
- Agent returns the result to the user
- Agent prompts the user for next action.

Typically, when doing web development, we ask the LLM to generate code, through file-editing. The problem is that this is complex and forces the LLM to handle fine grained modifications with lots of technical overloads.

In programming in general, and in web programming environments too, a framework always has to navigate between two poles:
- letting the dev have freedom to customize the code
- efficacity by providing standard ways to do things, through libraries and tools.

It is not as simple as that, but we can link that polarity to the opposition code vs config.
- Configuration is not turing complete
    - usually in json, yaml, toml files 
    - static
    - limited possibilities

- Code is turing complete
    - more powerful
    - more complex

When it comes to agent, we could represent these two orientations this way:
- Configuration can be handled by a MCP servers that only accepts strict instructions
- Code can be handled directly by the LLM, which can be more powerful but also more complex to manage.

For that we need a framework that makes a clear distinction between what is configuration, and what is code.

Our postulate, inspired by Pareto's law, could be: 80% of the work in web development can be done with configuration.  This framework will focus on that 80%.  The remaining 20% will be handled by code, but in a way that is easily integrated with the configuration.

# What is config, what is code (Basics, server-side)

After 15+ years of experience in web development, here are my 2 cents about what should obviously be configurable:
- Routing
- Authentication. Login/logout/user creation/management
- Database structure
- Input and output of methods
- Database queries (80% of them)
- API calls

In a "MVC" type framework (quite obsolete term), if we handle that through config, it leaves us with the procedural code associated with the controller, with a given input and output.

Let's call this the procedure. What does it typically involve
- advanced validation (do the linked resources exist, do they satisfy conditions)
- complex logic (e.g., business rules)
- complex calculations
- complex data transformations
- complex interactions with external services (e.g., payment gateways)
- complex error handling
- complex logging
- complex reporting
- database operations

# What is config, what is code (Advanced)

Inside the procedural code, maybe some things could also be handled by config:

- simple DB queries

Maybe we can do some very limited code with a tool like Scratch/Blockly. The tool could help us define the utility methods, their input/outputs, and even write tests/specifications.

# How will the framework work?

- Define the elements of the framework
    - Entities
    - Database schema
    - Database queries
    - API calls
    - Authentication
    - Routing
    - Input/output validation
    - Error handling
    - Logging
    - Reporting

 - For each elements, provide MCP server endpoints to:
    - Edit
    - Create
    - Find
    - Delete

 - For each element, provide a documentation that allows the user and the agent to understand how it should function.

 - The framework should also include instructions on how to use the framework. More specifically, on how to analyse a new requirement and implement it in the framework.

 # How I will implement the framework

 - v0.
    - **Modular Design:** Break down the framework into independent modules (e.g., database, API, authentication). This promotes reusability and maintainability.
    - I will only implement the most basic requirements
        - Routing
        - Database schema
        - Tests