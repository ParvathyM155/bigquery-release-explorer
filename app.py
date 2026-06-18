from flask import Flask, render_template, jsonify
import urllib.request
import xml.etree.ElementTree as ET
import re

app = Flask(__name__)

# Namespace for Atom feeds
NAMESPACES = {'atom': 'http://www.w3.org/2005/Atom'}

def fetch_and_parse_release_notes():
    url = "https://docs.cloud.google.com/feeds/bigquery-release-notes.xml"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
    except Exception as e:
        print(f"Error fetching release notes: {e}")
        return []

    try:
        root = ET.fromstring(xml_data)
        entries = []
        
        for entry in root.findall('atom:entry', NAMESPACES):
            title = entry.find('atom:title', NAMESPACES)
            date_str = title.text.strip() if title is not None else "Unknown Date"
            
            updated = entry.find('atom:updated', NAMESPACES)
            updated_str = updated.text.strip() if updated is not None else ""
            
            link_elem = entry.find("atom:link[@rel='alternate']", NAMESPACES)
            link_url = link_elem.attrib.get('href', '') if link_elem is not None else ""
            
            content_elem = entry.find('atom:content', NAMESPACES)
            content_html = content_elem.text if content_elem is not None else ""
            
            # Parse sub-items by splitting on <h3>Category</h3>
            items = []
            if content_html:
                # Find all <h3>Category</h3> content
                parts = re.split(r'<h3>(.*?)</h3>', content_html)
                # First element is prefix before first <h3>, rest are pairs of (category, body)
                for i in range(1, len(parts), 2):
                    category = parts[i].strip()
                    body = parts[i+1].strip() if i+1 < len(parts) else ""
                    items.append({
                        'category': category,
                        'body': body
                    })
                
                # If splitting didn't yield items, put raw HTML as general
                if not items:
                    items.append({
                        'category': 'General',
                        'body': content_html
                    })
            
            entries.append({
                'date': date_str,
                'updated': updated_str,
                'link': link_url,
                'items': items,
                'raw_content': content_html
            })
        return entries
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/release-notes')
def api_release_notes():
    notes = fetch_and_parse_release_notes()
    return jsonify({
        'status': 'success',
        'count': len(notes),
        'data': notes
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
