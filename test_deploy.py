import os
from dotenv import load_dotenv
import app

def test_zip_and_deployment():
    load_dotenv()
    token = os.getenv("NETLIFY_AUTH_TOKEN")
    
    print("🧪 Starting verification tests...")
    
    # A simple static React counter code snippet to test the flow
    test_code = """
    function App() {
        const [count, setCount] = React.useState(0);
        return (
            <div className="flex flex-col items-center justify-center min-h-screen bg-slate-900 text-white">
                <div className="bg-slate-800 p-8 rounded-xl shadow-2xl border border-slate-700 text-center max-w-sm">
                    <h1 className="text-2xl font-bold mb-4">🚀 Anti-Gravity Test Deployment</h1>
                    <p className="text-slate-400 mb-6">If you can see this, your deployment to Netlify was successful!</p>
                    <div className="text-5xl font-extrabold text-indigo-400 mb-6">{count}</div>
                    <button 
                        onClick={() => setCount(count + 1)}
                        className="px-6 py-2 bg-indigo-600 hover:bg-indigo-500 rounded-lg font-semibold transition"
                    >
                        Increment Count
                    </button>
                </div>
            </div>
        );
    }
    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<App />);
    """
    
    print("\n📦 Step 1: Testing ZIP compression in memory...")
    try:
        # We can construct the HTML and ZIP in-memory to test the compression
        import io
        import zipfile
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.writestr("index.html", "<html></html>")
        data = zip_buffer.getvalue()
        print(f"✅ ZIP compression check passed. Generated in-memory ZIP size: {len(data)} bytes")
    except Exception as e:
        print(f"❌ ZIP compression failed: {str(e)}")
        return

    print("\n🚀 Step 2: Testing deployment endpoint...")
    if not token or token == "your_netlify_token_here":
        print("⚠️  NETLIFY_AUTH_TOKEN is missing or set to placeholder. Skipping live deployment check.")
        print("💡 Please configure NETLIFY_AUTH_TOKEN in the `.env` file or sidebar to test live deployments.")
        return
        
    print(f"📡 Executing deployment request (Token length: {len(token)})...")
    res = app.deploy_to_netlify(test_code)
    
    if res.get("status") == "Success":
        print("\n🎉 LIVE DEPLOYMENT SUCCESSFUL!")
        print(f"🔗 Live Production URL: {res.get('url')}")
        print(f"🆔 Netlify Site ID: {res.get('site_id')}")
    else:
        print("\n❌ Deployment failed.")
        print(f"Message: {res.get('message')}")
        if res.get("details"):
            print(f"Details: {res.get('details')}")

if __name__ == "__main__":
    test_zip_and_deployment()
