from flask import Blueprint, render_template, send_from_directory, current_app
import os

main = Blueprint('main', __name__)


@main.route('/')
def home():
    """Renders the home page."""
    return render_template("index.html")


@main.route('/data/<path:filename>')
def download_file(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, 'data'), filename)
