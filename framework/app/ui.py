"""
This module contains API functionality.
"""

from flask import Blueprint, render_template

UI = Blueprint('ui', __name__)

@UI.route('/')
def home():
    """
    Render the home page.
    """
    return render_template('index.html')
