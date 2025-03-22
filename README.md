## VIDEO 



https://github.com/user-attachments/assets/ead223e2-cb77-43db-8603-170a7414c599



## Working and Structure
![diagram-export-3-22-2025-11_23_49-PM](https://github.com/user-attachments/assets/4109353b-60a1-41c0-b5d0-52247ae956f4)

# AgentX - AI-Powered Website Maintenance

🧰 **Overview**

AgentX is a cross-platform desktop application that automates website maintenance tasks using Google's Gemini LLM and a custom Retrieval-Augmented Generation (RAG) pipeline. It handles content updates, SEO optimization, error fixing, content generation, and performance monitoring—with minimal manual intervention.

✨ **Features**

* ✅ **Automated Content Updates:** Detects and refreshes outdated content.
* 🔍 **SEO Optimization:** Enhances metadata, keywords, and alt-text for better search visibility.
* 🛠️ **Error Detection & Fixing:** Identifies and repairs broken links and formatting issues.
* 📝 **AI-Powered Content Generation:** Fills content gaps with high-quality, human-like text.
* 📊 **Performance Monitoring:** Analyzes Core Web Vitals and suggests optimizations.

📐 **Tech Stack**

* **Frontend:** Next.js (React) + Mantine UI (for responsive design)
* **Backend:** Tauri (Rust) + Python (for specialized tasks)
* **AI Engine:** Google’s Gemini LLM + Custom RAG Pipeline
* **Data Management:** Local vector database + Web Crawling

🚀 **Installation & Setup**

✅ **Prerequisites**

Ensure you have the following installed:

* Node.js (Latest LTS)
* Rust (Stable version)
* Python (3.x)

🛠️ **Setup Instructions**

1.  **Clone the Repository**

    ```bash
    git clone [https://github.com/](https://github.com/)<username>/AgentX.git
    cd AgentX
    ```

2.  **Install Dependencies**

    ```bash
    pnpm install
    ```

3.  **Install Python Backend Dependencies and Run:**

    ```bash
    cd src/backend
    pip install -r requirements.txt
    python main.py # or how ever you run your python backend
    cd ../.. # Go back to the main directory
    ```

4.  **Run the Application**

    ```bash
    pnpm run tauri dev
    ```


