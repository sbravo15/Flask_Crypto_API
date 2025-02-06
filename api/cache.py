from flask_caching import Cache

cache = Cache()

def init_cache(app):
    """Initialize cache with the Flask app."""
    app.config['CACHE_TYPE'] = 'simple'  # Can be changed to 'redis' or other types later
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Cache timeout in seconds
    cache.init_app(app)
