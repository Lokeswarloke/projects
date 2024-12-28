from flask import render_template, jsonify
from app import app
from app.scraper import TwitterScraper

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    try:
        scraper = TwitterScraper()
        result = scraper.get_trends()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500