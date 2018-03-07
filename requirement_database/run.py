"""
    This runs the requirements database API using a Flask webserver (not recommended for production use).
"""

from app import create_app

if __name__ == '__main__':
    APP = create_app()
    APP.run(debug=True)
