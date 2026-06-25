import os
import streamlit as st
from dotenv import load_dotenv

# Import the core orchestration engine
import app

# Set page config
st.set_page_config(
    page_title="AI React App Generator & Deployer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables
load_dotenv()

# Inject Custom CSS for premium styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Space+Grotesk:wght@400;500;700&display=swap');

/* Apply modern font styles */
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

/* Stylize Streamlit main title */
.main-title {
    font-family: 'Space Grotesk', sans-serif;
    background: linear-gradient(135deg, #a78bfa 0%, #6366f1 50%, #3b82f6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    font-size: 2.8rem;
    margin-bottom: 0.5rem;
}

.subtitle {
    font-size: 1.15rem;
    color: #94a3b8;
    margin-bottom: 2rem;
}

/* Agent cards styling */
.agent-header {
    font-size: 1.1rem;
    font-weight: 600;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 1rem;
}

.agent-desc {
    font-size: 0.9rem;
    color: #94a3b8;
    margin-left: 1.8rem;
    margin-bottom: 0.5rem;
}

.badge-running {
    background-color: #3b82f6;
    color: white;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: bold;
}

.badge-done {
    background-color: #10b981;
    color: white;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: bold;
}

.badge-pending {
    background-color: #475569;
    color: #94a3b8;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: bold;
}

.badge-error {
    background-color: #ef4444;
    color: white;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Sidebar configurations
st.sidebar.markdown("### ⚙️ Engine Settings")

# Handle missing API keys gracefully by offering sidebar inputs
gemini_env = os.getenv("GEMINI_API_KEY", "")
netlify_env = os.getenv("NETLIFY_AUTH_TOKEN", "")

gemini_key = st.sidebar.text_input(
    "Google Gemini API Key", 
    value=gemini_env, 
    type="password",
    help="Needed for reasoning and code generation. Get it from Google AI Studio."
)
if gemini_key:
    os.environ["GEMINI_API_KEY"] = gemini_key

netlify_token = st.sidebar.text_input(
    "Netlify Auth Token", 
    value=netlify_env, 
    type="password",
    help="Needed to host and publish the React applications. Create one in your Netlify Account Settings."
)
if netlify_token:
    os.environ["NETLIFY_AUTH_TOKEN"] = netlify_token

# Credentials verification display in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔌 API Status")
if os.getenv("GEMINI_API_KEY"):
    st.sidebar.markdown("🟢 **Gemini API Key:** Configured")
else:
    st.sidebar.markdown("🔴 **Gemini API Key:** Missing")

if os.getenv("NETLIFY_AUTH_TOKEN"):
    st.sidebar.markdown("🟢 **Netlify Token:** Configured")
else:
    st.sidebar.markdown("🔴 **Netlify Token:** Missing")

st.sidebar.markdown("---")
st.sidebar.markdown("""
### 💡 Sample Prompts to Try:
- *A clean Pomodoro timer app with custom task input, list of completed tasks, and sound alert cues.*
- *A global time zone dashboard displaying selected cities with interactive analog clocks and search.*
- *A simple Kanban Board to drag/transfer task items between 'To Do', 'In Progress', and 'Completed' columns.*
- *A calculator layout with scientific buttons and history log drawer.*
""")

# Main Content Header
st.markdown('<div class="main-title">🤖 End-to-End React App Generator & Deployer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A multi-agent system that synthesizes, audits, self-heals, and deploys fully functional React applications.</div>', unsafe_allow_html=True)

# Layout: Split into Main and Side Panel
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("### 🔮 Describe your App Idea")
    user_prompt = st.text_area(
        "Enter features, pages, behaviors, and visual styles you want in your React application:",
        height=150,
        placeholder="e.g., A stylish recipe generator. Users can add recipes, filter by category (vegetarian, quick meal, dessert), search ingredients, and save their favorites in local storage."
    )
    
    # Validation warning
    creds_ok = bool(os.getenv("GEMINI_API_KEY")) and bool(os.getenv("NETLIFY_AUTH_TOKEN"))
    if not creds_ok:
        st.warning("⚠️ Please provide your API keys in the sidebar configuration to begin generating apps.")
        
    generate_btn = st.button("🚀 Build & Deploy Application", disabled=not creds_ok, use_container_width=True)

with col2:
    st.markdown("### 🏗️ Live Agent Orchestration Console")
    # Containers to display real-time agent execution
    console_area = st.container()

if generate_btn and user_prompt:
    with col2:
        # Create dynamic steps with st.status
        with st.status("🛠️ Pipeline Orchestrator running...", expanded=True) as status_box:
            
            # Placeholders for each agent block
            arch_status = st.empty()
            coder_status = st.empty()
            linter_status = st.empty()
            deployer_status = st.empty()

            # Initialize states
            arch_status.markdown('<div class="agent-header">🔎 Product Architect <span class="badge-pending">PENDING</span></div><div class="agent-desc">Translating prompt into system blueprints...</div>', unsafe_allow_html=True)
            coder_status.markdown('<div class="agent-header">💻 React Coder <span class="badge-pending">PENDING</span></div><div class="agent-desc">Synthesizing React 18 component structures...</div>', unsafe_allow_html=True)
            linter_status.markdown('<div class="agent-header">🛡️ Quality Linter <span class="badge-pending">PENDING</span></div><div class="agent-desc">Auditing code syntax & resolving variables...</div>', unsafe_allow_html=True)
            deployer_status.markdown('<div class="agent-header">🚀 DevOps Deployer <span class="badge-pending">PENDING</span></div><div class="agent-desc">Packaging site and pushing to Netlify...</div>', unsafe_allow_html=True)

            def pipeline_callback(step, data):
                msg = data.get("message", "")
                details = data.get("details", "")
                success = data.get("success", True)
                
                if step == "architect":
                    if success:
                        arch_status.markdown('<div class="agent-header">🔎 Product Architect <span class="badge-done">COMPLETED</span></div><div class="agent-desc">Blueprint created.</div>', unsafe_allow_html=True)
                        with st.expander("View Blueprint Map", expanded=False):
                            st.write(details)
                    else:
                        arch_status.markdown(f'<div class="agent-header">🔎 Product Architect <span class="badge-error">FAILED</span></div><div class="agent-desc">{msg}</div>', unsafe_allow_html=True)
                        
                elif step == "coder":
                    if success:
                        # Could be initial generation or a self-healing pass
                        if "self-healing" in msg:
                            coder_status.markdown(f'<div class="agent-header">💻 React Coder <span class="badge-running">SELF-HEALING</span></div><div class="agent-desc">{msg}</div>', unsafe_allow_html=True)
                        else:
                            coder_status.markdown('<div class="agent-header">💻 React Coder <span class="badge-done">COMPLETED</span></div><div class="agent-desc">Code asset generated.</div>', unsafe_allow_html=True)
                    else:
                        coder_status.markdown(f'<div class="agent-header">💻 React Coder <span class="badge-error">FAILED</span></div><div class="agent-desc">{msg}</div>', unsafe_allow_html=True)
                        
                elif step == "linter":
                    if success:
                        linter_status.markdown(f'<div class="agent-header">🛡️ Quality Linter <span class="badge-done">PASSED</span></div><div class="agent-desc">{msg}</div>', unsafe_allow_html=True)
                        if details:
                            with st.expander("View Quality Assessment Report", expanded=False):
                                st.code(details, language="json")
                    else:
                        linter_status.markdown(f'<div class="agent-header">🛡️ Quality Linter <span class="badge-running">REPAIRING</span></div><div class="agent-desc">{msg}</div>', unsafe_allow_html=True)
                        with st.expander("View Compile Errors", expanded=True):
                            st.code(details, language="json")
                            
                elif step == "deployer":
                    if success:
                        deployer_status.markdown('<div class="agent-header">🚀 DevOps Deployer <span class="badge-done">COMPLETED</span></div><div class="agent-desc">Netlify deployment succeeded.</div>', unsafe_allow_html=True)
                    else:
                        deployer_status.markdown(f'<div class="agent-header">🚀 DevOps Deployer <span class="badge-error">FAILED</span></div><div class="agent-desc">{msg}</div>', unsafe_allow_html=True)
                        if details:
                            st.error(details)

            # Run orchestration
            result = app.run_agent_pipeline(user_prompt, callback=pipeline_callback)
            
            if result.get("status") == "Success":
                status_box.update(label="🚀 Generation and Deployment complete!", state="complete", expanded=True)
                st.session_state["generation_result"] = result
            else:
                status_box.update(label="❌ Pipeline processing encountered errors", state="error", expanded=True)
                st.error(f"Application building failed: {result.get('message')}")

# If we have a successful result in state, render the code and iframe
if "generation_result" in st.session_state:
    res = st.session_state["generation_result"]
    url = res.get("url")
    code = res.get("code")
    
    st.markdown("---")
    st.markdown("## 🎉 Production Deployment Completed!")
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.success(f"🌐 Your application is live at: [{url}]({url})")
        st.info("💡 Tip: Click the URL link to open your live web application in a new tab, or interact with it below.")
        
        # Interactive iframe display
        st.markdown(f'<iframe src="{url}" style="width:100%; height:550px; border:3px solid #6366f1; border-radius:12px; background:white;"></iframe>', unsafe_allow_html=True)
        
    with col_right:
        st.markdown("### 🖥️ Synthesized Code (App.jsx)")
        st.code(code, language="jsx")
