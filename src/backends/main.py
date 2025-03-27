from flask import Flask, request, jsonify
from flask_cors import CORS
from scripts.seo import analyze_seo, get_keyword_suggestions, optimize_metadata
from scripts.scraper import scrape_website
from scripts.rag_utils import vec_store, retrieval
from scripts.content_update import process_update
from scripts.content_addition import process_add
from scripts.error_link import process_links
import json
import subprocess
import pexpect

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/scrape', methods=["GET"])
def scrape():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400
    result = scrape_website(url)
    try:
        data = json.loads(result)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/update', methods=["GET"])
def update():
    url = request.args.get("url")
    if not url: 
        return jsonify({"error": "URL parameter is required"}), 400
    try:
        scraped = scrape_website(url)
        if isinstance(scraped, str):
            scraped = json.loads(scraped)
        suggestions = process_update(scraped)
        return jsonify(suggestions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add', methods=["GET"])
def add():
    url = request.args.get("url")
    if not url:
         return jsonify({"error": "URL parameter is required"}), 400
    try:
        scraped = scrape_website(url)
        if isinstance(scraped, str):
            scraped = json.loads(scraped)
        suggestions = process_add(scraped)
        return jsonify(suggestions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/errorlink', methods=["GET"])
def errorlink():
    url = request.args.get("url")
    if not url:
         return jsonify({"error": "URL parameter is required"}), 400
    try:
        scraped = scrape_website(url)
        try:
            scraped_data = json.loads(scraped)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON response from scraper"}), 500
        
        broken_links = process_links(scraped_data, base_url=url)
        return jsonify({"broken_links": broken_links})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/seo', methods=["GET"])
def seo():
    url = request.args.get("url")
    if not url:
         return jsonify({"error": "URL parameter is required"}), 400
    try:
         seo_report = analyze_seo(url)
         keyword_data = get_keyword_suggestions(url)
 
         current_html = "<html><head><title>Example</title></head><body></body></html>"
         optimized_html = optimize_metadata(current_html)
         
         return jsonify({
             "seo_report": seo_report,
             "keyword_data": keyword_data,
             "optimized_html": optimized_html
         })
    except Exception as e:
         app.logger.error(f"Error during SEO analysis: {e}")
         return jsonify({"error": str(e)}), 500

@app.route('/setup-aider', methods=["POST"])
def setup_aider():
    data = request.get_json()
    working_dir = data.get("workingDir")

    if not working_dir:
        return jsonify({"error": "Working directory is required."}), 400

    try:
        command = (
            f'cd "{working_dir}" && '
            'export GROQ_API_KEY=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 && '
            'echo "yes" | aider --model groq/llama3-70b-8192 --no-show-model-warnings --message "Update the navbar so that it looks more beautiful and elegant and do it according to yourself , make sure u only change one file tho . "'
        )

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=True
        )

        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500

        return jsonify({"stdout": result.stdout})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
