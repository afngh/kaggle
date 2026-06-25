


Here is the comprehensive, professional agents.md file for your codebase repository. It outlines your multi-agent architecture, tools, and execution loop using markdown elements for optimal readability by the Kaggle capstone judges. ------------------------------ ## 🤖 System Architecture & Agent

pasted




How can I help you today?

Pasted content
6.09 KB •110 lines
•
Formatting may be inconsistent from source

Here is the comprehensive, professional agents.md file for your codebase repository. It outlines your multi-agent architecture, tools, and execution loop using markdown elements for optimal readability by the Kaggle capstone judges.
------------------------------
## 🤖 System Architecture & Agent Orchestration (agents.md)
This document details the multi-agent orchestration framework powering the End-to-End React App Generator & Deployer. The system leverages the Google AI GenAI SDK alongside a custom execution loop to transition user ideas from natural language prompts into live, production-deployed React applications.
------------------------------
## 🏗️ Architectural Overview
The backend uses an asymmetrical pipeline architecture. High-level planning and code synthesis tasks utilize gemini-2.5-pro for deep reasoning, while structural validation passes leverage gemini-2.5-flash for fast computation speeds.

   [User App Input]
          │
          ▼
┌──────────────────┐
│Product Architect │  ──► Translates idea into component maps and states
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│   React Coder    │  ──► Generates functional React 18 / Tailwind code
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│  Quality Linter  │  ──► Validates code formatting & prevents compile bugs
└─────────┬────────┘
          │
          ├─── [Code Fails Validation] ──► (Routes back to Coder for self-healing)
          │
          └─── [Code Passes Validation]
                      │
                      ▼
            ┌──────────────────┐
            │  DevOps Deployer │ ──► Packages workspace & pushes to Netlify API
            └──────────────────┘

------------------------------
## 👥 Agent Directory & Persona Configurations## 1. Product Architect Agent

* Model Core: gemini-2.5-pro
* Role: Product Manager & Systems Architect
* Objective: Analyze unstructured user desires and turn them into explicit UI/UX engineering requirements.
* System Prompt Hook:

You are an expert Systems Architect specializing in React applications. 
Your task is to take a raw user concept and outline a component hierarchy tree. 
Identify necessary state structures, state hooks, and data layout flows. 
Ensure you specify interactive event flows (buttons, inputs) using Tailwind classes.


## 2. React Coder Agent

* Model Core: gemini-2.5-pro
* Role: Senior Frontend Software Engineer
* Objective: Code standalone, fully interactive single-file React configurations matching the Architect's requirements.
* System Prompt Hook:

You are an expert Frontend Developer. Review the provided architecture blueprint.
Generate a pure JavaScript asset using React 18 formatting rules.
Use inline Tailwind CSS styles exclusively for visual layout elements.
Do not output markdown block text or backticks. Start code strings directly with declarations.
Target mounting directly to ReactDOM.createRoot(document.getElementById('root')).


## 3. Quality Linter Agent

* Model Core: gemini-2.5-flash
* Role: Automated Code Quality Auditor
* Objective: Perform validation sweeps on generated files to ensure syntax errors don't cause deployment runtime breaks.
* System Prompt Hook:

You are a strict code verification system. 
Analyze the raw JavaScript code text block to check for bracket mismatches, unclosed tags, or unmapped state variables. 
If errors exist, explicitly list the bug lines so the development environment can trigger correction routines.


## 4. DevOps Deployer Agent

* Model Core: gemini-2.5-flash (augmented with custom Python system tools)
* Role: Site Reliability Engineer
* Objective: Collect verified code assets, structure the runtime directory wrappers, and call external network targets for live publication.

------------------------------
## 🛠️ Tool Specifications & Integrations
The system uses specialized custom tool frameworks to securely cross boundaries into external file and platform environments.
## deploy_to_netlify_tool

* Type: Operational System Call / Network Connector
* Parameters: js_content (string)
* Behavior:
1. Spins up an isolated operating system tempfile.TemporaryDirectory path block.
   2. Builds a static index.html wrapper configured with script engines for Babel compilation and React 18 execution layers.
   3. Runs an operational terminal zip subprocess to compile index bundles.
   4. Issues a securely signed POST multi-part form call directly to the Netlify API endpoint using an access token (NETLIFY_AUTH_TOKEN).
   5. Returns a structured JSON dictionary containing completion validation metadata and the unique production URL.

------------------------------
## 🔄 Self-Healing Compilation & Execution Loop
To ensure robust code outputs, the system runs an automated Self-Healing Loop if compilation issues occur:

   1. The React Coder creates an application iteration pass.
   2. The Quality Linter scans the output buffer string for syntax anomalies.
   3. If a violation is identified: The pipeline pauses standard forward routing, packages the faulty code code block with the compiler error message, and flags a correction request back to the React Coder.
   4. The Coder re-evaluates the script context, patches the variable or tag error, and submits it back to the linter.
   5. Once verified, the code moves to the DevOps Deployer for immediate live infrastructure provisioning.

------------------------------
## 🚀 Advance the Conversation
This agents.md document gives you a professional, structured breakdown ready for your Kaggle capstone presentation.
Would you like me to generate your README.md file next, or should we construct the Streamlit user dashboard app code (main.py) to wire up your UI?