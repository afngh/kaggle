# 🤖 End-to-End React App Generator & Deployer

This repository contains a multi-agent AI system that translates natural language prompts into live, production-deployed React applications. Built with the Python stack and powered by Google Gemini, the system automates systems planning, frontend code generation, syntax validation, self-healing loop correction, and cloud hosting.

---

## 🏗️ Multi-Agent Architecture

```
   [User Prompt]
         │
         ▼
┌──────────────────┐
│Product Architect │  ──► Analyzes requirements & plans states (gemini-2.5-pro)
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│   React Coder    │  ──► Synthesizes React 18 & Tailwind CSS code (gemini-2.5-pro)
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│  Quality Linter  │  ──► Validates brackets, tags, & state hooks (gemini-2.5-flash)
└─────────┬────────┘
          │
          ├─── [Validation Fails] ──► (Routes back to Coder for Self-Healing Loop)
          │
          └─── [Validation Passes]
                      │
                      ▼
            ┌──────────────────┐
            │  DevOps Deployer │ ──► Packages ZIP buffer & pushes to Netlify API
            └──────────────────┘
```

1. **Product Architect Agent (`gemini-2.5-pro`)**: Refines requirements, designs component hierarchy, and maps states/props.
2. **React Coder Agent (`gemini-2.5-pro`)**: Generates modular React 18 frontend code styled with Tailwind CSS.
3. **Quality Linter Agent (`gemini-2.5-flash`)**: Audits syntax and structure. Returns issues in structured JSON format.
4. **Self-Healing Loop**: Automatically passes compiler/syntax errors back to the React Coder for repair (up to 3 attempts).
5. **DevOps Deployer Agent**: Bundles code into an in-memory ZIP package and deploys it directly using the Netlify Sites API.

---

## 🛠️ Requirements & Setup

### Prerequisites
- Python 3.8 or higher.
- A **Google Gemini API Key** (from [Google AI Studio](https://aistudio.google.com/)).
- A **Netlify Personal Access Token** (from Netlify Settings -> Applications -> Personal Access Tokens).

### Installation

1. Install the required python libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables in the [.env](file:///c:/AI%20AGENTS/kaggle/.env) file:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   NETLIFY_AUTH_TOKEN=your_netlify_token_here
   ```

---

## 🚀 Running the Project

### Step 1: Run the Deployment Test
Run the test script to verify that your memory ZIP compression and Netlify API connection are fully functional:
```bash
python test_deploy.py
```

### Step 2: Start the Web Dashboard
Launch the interactive Streamlit developer interface:
```bash
streamlit run main.py
```
*Your browser will automatically open to http://localhost:8501.*

---

## 📁 Key File Map

- [main.py](file:///c:/AI%20AGENTS/kaggle/main.py): Streamlit dashboard frontend, real-time logging console, and browser preview.
- [app.py](file:///c:/AI%20AGENTS/kaggle/app.py): Core backend orchestrating the agent pipelines, JSON linter schema, and self-healing loop.
- [test_deploy.py](file:///c:/AI%20AGENTS/kaggle/test_deploy.py): Verification CLI tool to test ZIP bundler and Netlify API endpoint.
- [AGENTS.md](file:///c:/AI%20AGENTS/kaggle/AGENTS.md): Architectural design paper detailing the personas and loops.
