from flask import Flask, request, redirect, render_template_string
import random
import string

app = Flask(__name__)
url_map = {}

HTML_TEMPLATE = """
<!doctype html>
<title>URL Shortener</title>
<h2>🔗 Simple URL Shortener</h2>
<form method="POST">
  <label>Enter URL to shorten:</label><br>
  <input type="text" name="original_url" required style="width:300px;"><br><br>
  <input type="submit" value="Shorten">
</form>
{% if short_url %}
  <p>Shortened URL: <a href="{{ short_url }}">{{ short_url }}</a></p>
{% endif %}
"""

def generate_short_code(length=6):
    """Generates a random short code using letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_code = generate_short_code()
        url_map[short_code] = original_url
        short_url = request.host_url + short_code
    return render_template_string(HTML_TEMPLATE, short_url=short_url)

@app.route('/<short_code>')
def redirect_to_original(short_code):
    """Redirects to the original URL if the short code exists."""
    original_url = url_map.get(short_code)
    if original_url:
        return redirect(original_url)
    return "Invalid short URL", 404

if __name__ == '__main__':
    app.run(debug=True)
