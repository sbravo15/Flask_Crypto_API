from flask import Flask
from api.routes import crypto_bp
from api.cache import cache, init_cache  # Import cache setup

def create_app():
    app = Flask(__name__)
    init_cache(app)  # Initialize caching before registering routes
    app.register_blueprint(crypto_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
