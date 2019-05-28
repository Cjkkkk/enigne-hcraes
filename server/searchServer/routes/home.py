from flask import render_template
from searchServer import app


@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')
